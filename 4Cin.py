#!/usr/bin/python

# Written by: Ibai Irastorza-Azcarate
# Universidad Pablo de Olavide, CABD, Sevilla. 

#Main script: check github.io/batxes/4Cin

import sys, os, re, inspect, glob
import getopt
import ConfigParser
import subprocess
from multiprocessing import Process, Lock, Pool, current_process
import argparse
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    import IMP.kernel
    import IMP.algebra
    import IMP.core
    import IMP.display
    import IMP.base
    import IMP.atom
    import IMP.rmf
    import IMP.container
    import RMF
#warnings.filterwarnings("ignore")
import time
from random import randint
import numpy as np
from collections import defaultdict
import operator
import shutil
from os import listdir, remove
from os.path import isfile, join
from itertools import combinations,izip, chain
import scipy.cluster.hierarchy as sch
from numpy import vstack,array
from numpy.random import rand
import matplotlib
try: 
    matplotlib.use('Agg')
    plot = True
except:
    plot = False
    print "\nPyplot is needed for the figures.\n"
    e = sys.exc_info()[1]
    print e
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from math import fabs
from scipy.stats.stats import spearmanr

putative_minimum_size = 0 #300A is the consensus but has no meaning when we have a big resolution
start_time = time.time()

# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

# use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"src")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
    
from data_manager import fileCheck, sizeReader,  calculateNWindowedDistances, calculate_fragment_number

def worker(instructions):
    p = subprocess.Popen(instructions)
    p.wait()

def chimera_worker(chimera_file):
    distance_output = subprocess.check_output(["chimera", "--nogui", chimera_file[0]])
    return distance_output,chimera_file[1],chimera_file[2],current_process().name
    
def chimera_worker_vhic(chimera_file):
    distance_output = subprocess.check_output(["chimera", "--nogui", chimera_file])
    return distance_output

def modeling((uZ, lZ, maxDis, starting_point, big_sampling)):
    y2 = maxDis
    if not big_sampling:
        number_of_models = pre_number_of_models
    else:
        number_of_models = total_number_of_models/number_of_cpus
    rmf_video = False #If we wanna create a video of the IMP optimization. Not checked since 2015
    evaluation = False #If we wanna see the evaluation of the restraints. 
    RESTRAINTS = [True,False,True,False] #4c counts, EV, HUB(connectivity), HLB(connectivity)
    RESTRAINTS_QUANTITY = [0,0,0,0]
    radius = 0
    k = 1
    if evaluation:
        std_dev = y2*0.2 #300 A #for evaluation #set a percentage of max distance. 20%
    if rmf_video:
        frames = 5000
    #optimization variables
    LSTEPS = 5
    STEPS = 1
    NROUNDS= 10000 
    endLoopCount = 0
    stopCount = 15
    endLoopValue = 0.00001
    hightemp = int (0.025 * NROUNDS )
    alpha = 1.0 * number_of_fragments #the weight of the fragments
    if big_sampling:
        storage_folder = working_dir+prefix+"/"+prefix+"_output_"+str(uZ)+"_"+str(lZ)+"_"+str(y2) #the dir where the data will be saved
    else:
        storage_folder = working_dir+prefix+"/"+"pre_modeling/"+prefix+"_output_"+str(uZ)+"_"+str(lZ)+"_"+str(y2) #the dir where the data will be saved
    score_file = storage_folder+"/score"+str(starting_point)+".txt"
    if os.path.exists(score_file): os.remove(score_file) 
    exv_values = []
    hub_values = []
    try:
        if not os.path.exists(storage_folder): os.makedirs(storage_folder)
    except OSError, e:
        if e.errno != 17:
            raise
        pass
    radius_scale = 0.0423 #Radius of 1 bp in A. for the IrxB models. It's the canonical value for 30 nm chromatin
    # radius_scale = 0.00055 #depending my calculations
    ## nucleosome = 200 bp. 30nm fiber -> 6-7 nucleosomes = 11 nm. -> then 1bp = 0.00846nm.
    ## string of beads  11nm = 200bp. 1bp = 0.055nm. 
    ## radius for both:
    ##                30nm : 0.00423nm = 0.0423A
    ##                string of beads : 0.0275nm = 0.275A
    #http://www.nature.com/nsmb/journal/v18/n1/pdf/nsmb.1936.pdf -> 0.01 occupancy
    #http://www.pnas.org/content/84/22/7802.full.pdf
    # dsDNA_1bp_size = 34 #Angstrom Double strand DNA 1 bp size
    ####### FACT: 10 NUCLEOTIDES = 34 aNGSTROMS IN LENGTH

    #to get the size of the fragments, we read any file
    reads_size = sizeReader(fileCheck(files[0]))

    #The sampling starts here
    ######################################################################
    for sample in range(starting_point, starting_point+number_of_models):
        movers = []
        n_restraints = []
        genome = []
        spheres = []
        restraints = []
        movers = []
        bead_radii = []
        fragment_bp_quantity =[]
        scores = []
        chimera_file = prefix+str(sample)+".py"
        verboseprint ("Generating {} ...".format(chimera_file))
        values_file = prefix+str(sample)+".txt"
        w = IMP.display.ChimeraWriter(storage_folder+"/"+chimera_file)
        m = IMP.Model()
        if rmf_video:
            hierarqy= IMP.atom.Hierarchy.setup_particle(IMP.Particle(m))
        ##########################    REPRESENTATION ##########################    REPRESENTATION
        for i in range(number_of_fragments):
                # Create "untyped" Particles
                p = IMP.kernel.Particle(m,"particle_"+str(i))
                radius_sum = 0
                for j in range(int(fragments_in_each_bead)):
                    radius_sum = radius_sum + reads_size[(i*int(fragments_in_each_bead))+j]
                radius = radius_scale * radius_sum #sphere radius proportional to fragments
                fragment_bp_quantity.append(radius_sum)
                #verboseprint ("Fragment number:{} size:{} radius:{}".format(i,radius_sum,radius))
                #decorator with sphere  
                #Creating very far away particles (10000) could alter the final result of the beads that are not restrained
                d = IMP.core.XYZR.setup_particle(p, IMP.algebra.Sphere3D(IMP.algebra.Vector3D(randint(0,int(y2)), randint(0,int(y2)), randint(0,int(y2))), radius)) 
                bead_radii.append(radius)
                #Coloring the beads
                if i in(viewpoint_fragments):
                    if i in(are_genes):
                        color = IMP.display.Color(1,0.7,0)
                    else: 
                        color = IMP.display.Color(0,1,0)
                    IMP.display.Colored.setup_particle(p, color)
                else:
                    #Coloring rest of beads
    #               #one theme of color #blue, purple, red (gradient)
                    #color = IMP.display.Color(1/float(number_of_fragments)*i,0.0,1-1/float(number_of_fragments)*i) 
                    #another theme (only grey)
                    color = IMP.display.Color(0.7,0.7,0.7) 
                    IMP.display.Colored.setup_particle(p, color)
                d.set_coordinates_are_optimized(True) #tHIS IS FOR Ball Mover. BallMover can't move non-optimized attribute
                genome.append(p)
                spheres.append(d)
                # to use with montecarlo
                movers.append(IMP.core.BallMover([p], radius*2))
        #         movers[-1].set_was_used(True) -> #what does this do?
                if (rmf_video):
                    IMP.atom.Mass.setup_particle(p,30)
                    IMP.atom.Diffusion.setup_particle(p)
                    hierarqy.add_child(IMP.atom.Hierarchy.setup_particle(p))
        ##########################  RESTRAINTS ##########################  RESTRAINTS
        #Restraint types:
        #Distances
        #Excluded volume
        #Connectivity (HUB and HLB)
        ############################################################################
        r_count = 0
        reads_values,reads_weights,start_windows, end_windows = calculateNWindowedDistances(int(fragments_in_each_bead),uZ,lZ, y2,files)
        for j in range(len(files)):
            reads_weight = reads_weights[j]
            reads_value = reads_values[j]
            #get the number of reads and their size from our files
            f = fileCheck(files[j])
            reads_size = sizeReader(f)
            n_fragments = len(reads_size)/int(fragments_in_each_bead)  
            ##########################################
            #### harmonic restraints are got from file
            counter = 0
            if (RESTRAINTS[0]):
                p1 = genome[viewpoint_fragments[j]]
                for i in range(n_fragments):
                    counter += 1
                    if i != viewpoint_fragments[j]:
                        if reads_value[i] != 0: 
                            if i not in ignore_beads:
                                #now, we dont set distance restraints for the beads near the viewpoint (if stated, default = 0)
                                if i < viewpoint_fragments[j]-ignore_viewpoint_beads or i > viewpoint_fragments[j]+ignore_viewpoint_beads:  
                                    p2 = genome[i]
                                    #We add the diameters of the beads to the distance
                                    # the real distance is not from the core, we need to add the diameter, all the dna sequence
                                    #distance = bead_radii[j] + bead_radii[i] + float(reads_value[i])
                                    distance = float(reads_value[i])
                                    if distance != float(y2):
                                        kk2 = fabs(reads_weight[i])
                                        #if it is not in the window of the 4C interactome
                                        if (start_windows[j] > counter or end_windows[j] < counter):
                                            f = IMP.core.HarmonicLowerBound(distance, k*kk2)
                                        else:     
                                            f = IMP.core.Harmonic(distance, k*kk2)                  
                                        s = IMP.core.DistancePairScore(f)
                                        r = IMP.core.PairRestraint(s, (p1, p2))  #this is the restraint
                                        restraints.append(r)
                                        m.add_restraint(r)
                                        r_count += 1
        n_restraints.append(r_count)  
        RESTRAINTS_QUANTITY[0] = r_count 
        ##############################################
        ###############################excluded volume
        if (RESTRAINTS[1]):
            mode = 1
            if mode == 1:
                r = IMP.core.ExcludedVolumeRestraint(genome,k) #we can remove k and 1 (genome,k,1) 
                restraints.append(r)
                m.add_restraint(r)
            if mode == 2:
                # this container lists all pairs that are close at the time of evaluation
                nbl= IMP.container.ClosePairContainer(genome, 0,2)
                h= IMP.core.HarmonicLowerBound(putative_minimum_size,1)
                sd= IMP.core.DistancePairScore(h)
                #sd= IMP.core.SphereDistancePairScore(h)
                # use the lower bound on the inter-sphere distance to push the spheres apart
                nbr= IMP.container.PairsRestraint(sd, nbl)
                m.add_restraint(nbr)
            RESTRAINTS_QUANTITY[1] = 1 
        #######################################################
        ##################String of beads. Harmonic Upper bound
        if (RESTRAINTS[2]):
            # using a HarmonicDistancePairScore for fixed length links is more
            # efficient than using a HarmonicSphereDistnacePairScore and works
            # better with the optimizer
            res_count = 0
            for i in range(len(genome)-1): 
                    #### Different std_dev
                kk = 1    
                hub = IMP.core.HarmonicUpperBound(bead_radii[i]+bead_radii[i+1],k*kk)
                p1 = genome[i]
                p2 = genome[i+1]
                s = IMP.core.DistancePairScore(hub)
                r = IMP.core.PairRestraint(s, (p1, p2))  #this is the restraint
                restraints.append(r)
                m.add_restraint(r)
                res_count += 1
            RESTRAINTS_QUANTITY[2] = res_count
        
        #######################################################
        ##################String of beads. Harmonic Lower bound
        if (RESTRAINTS[3]): 
            res_count = 0 
            hlb = IMP.core.HarmonicLowerBound(putative_minimum_size,k)
            for h in range(len(genome)):
                p1 = genome[h]
                for i in range(len(genome)):
                    if i != h and i != h-1 and i != h+1:
                        p2 = genome[i]
                        s = IMP.core.DistancePairScore(hlb)
                        r = IMP.core.PairRestraint(s, (p1, p2))  #this is the restraint
                        restraints.append(r)
                        m.add_restraint(r)  
                        res_count+=1    
            RESTRAINTS_QUANTITY[3] = res_count
        ##########################  SAMPLING ##########################  SAMPLING
        cg = IMP.core.ConjugateGradients(m) 
        mc = IMP.core.MonteCarloWithLocalOptimization(cg, LSTEPS) 
        mc.set_return_best(True) 
        mc.set_name("MC")
        sm = IMP.core.SerialMover(movers)
        mc.add_mover(sm)
         
        # sf = IMP.core.RestraintsScoringFunction(restraints, "RSF")
        # mc.set_scoring_function(sf) #monte carlo
        # cg.set_scoring_function(sf)     
        
        ######################RMF VIDEO, RMF must be installed from the IMP package!! ####################    
        if rmf_video:
        #create the RMF file to show the movie
            rmf= RMF.create_rmf_file('genome.rmf')
            rmf.set_description("Simulate genome.\n")
            bd = IMP.atom.BrownianDynamics(m)
            bd.set_log_level(IMP.base.SILENT)
			#bd.set_scoring_function(sf)
            bd.set_maximum_time_step(100)
            IMP.rmf.add_hierarchy(rmf, hierarqy)
            IMP.rmf.add_restraints(rmf, restraints)
            oss= IMP.rmf.SaveOptimizerState(m,rmf)
            oss.update_always("initial conformation")
            oss.set_log_level(IMP.base.SILENT)
            oss.set_simulator(bd)
            bd.add_optimizer_state(oss)
            print "Optimizing twith Brownian Dynamics for the RMF file (movie)."
            bd.optimize(frames)

        IMP.base.set_log_level(IMP.base.SILENT)
        #verboseprint( "Number of restraints: %i" % (len(restraints)))
        #first score
        scores.append(m.evaluate(False))
        #verboseprint ("Start score: {}".format(scores[-1]))
        #verboseprint ("\nStarts the optimization... ")
        #First hightemp iterations, do not stop the optimization
        #verboseprint ("High temp iterations")
        for i in range(0,hightemp):
            temperature = alpha * (1.1 * NROUNDS - i) / NROUNDS
            mc.set_kt(temperature)
            scores.append(mc.optimize(STEPS))
            # verboseprint ("{} {} temp:{}".format(i, scores[-1],mc.get_kt()))
        needed_time = time.time() - start_time
        lownrj = scores[-1]
        # verboseprint ("Time for High temp iterations {}".format(needed_time))
        # verboseprint ("Low temp iterations")
        for i in range(hightemp,NROUNDS): 
            temperature = alpha * (1.1 * NROUNDS - i) / NROUNDS
            mc.set_kt(temperature)
            scores.append(mc.optimize(STEPS))
            # verboseprint ("{} {} temp:{}".format(i, scores[-1],mc.get_kt()))
            # Calculate the score variation and check if the optimization
            # can be stopped or not
            if lownrj > 0:
                deltaE = fabs((scores[-1] - lownrj) / lownrj)
            else:
                deltaE = scores[-1]
            if (deltaE < endLoopValue and endLoopCount == stopCount):
                break
            elif (deltaE < endLoopValue and endLoopCount < stopCount):
                endLoopCount += 1
                lownrj = scores[-1]
            else:
                endLoopCount = 0
                lownrj = scores[-1]
        suma1 = suma2 = suma3 = suma4 = 0
        if RESTRAINTS[0]:
            for r in restraints[0:RESTRAINTS_QUANTITY[0]]:
                suma1 = suma1 + r.evaluate(False)
		#print RESTRAINTS_QUANTITY[0], "distance restraints: ",suma1
        if RESTRAINTS[1]:
            suma2 = restraints[RESTRAINTS_QUANTITY[0]].evaluate(False)
		#print 1, " excluded Volume restraint: ",suma2
        if RESTRAINTS[2]:    
            n = RESTRAINTS_QUANTITY[0]+RESTRAINTS_QUANTITY[1]
            n2 = RESTRAINTS_QUANTITY[0]+RESTRAINTS_QUANTITY[1]+RESTRAINTS_QUANTITY[2]
            for r in restraints[n:n2]:
                suma3 = suma3 + r.evaluate(False)
		#print n2-n, " connectivity HUB restraints: ",suma3
        if RESTRAINTS[3]:  
            n = RESTRAINTS_QUANTITY[0]+RESTRAINTS_QUANTITY[1]+RESTRAINTS_QUANTITY[2]
            n2 = RESTRAINTS_QUANTITY[0]+RESTRAINTS_QUANTITY[1]+RESTRAINTS_QUANTITY[2]+RESTRAINTS_QUANTITY[3]
            for r in restraints[n:n2]:
                suma4 = suma4 + r.evaluate(False)
		#print n-n2, " connectivity HLB restraints: ",suma4
        #verboseprint ("Total: ".format(suma1+suma2+suma3+suma4))
        #verboseprint ("------------------------\n")
        #verboseprint ("Number of restraints: %i" % (len(restraints)))
        needed_time = time.time() - start_time
        #verboseprint ("Time for Low temp iterations".format(needed_time))
        f1 = open (score_file,"a+")
        f1.write(str(sample)+"\t"+str(scores[-1])+"\n")
        f1.close()
        #EVALUATION
        if (evaluation):
            not_fulfilled = 0
            total_restraints = 0
            for i in range(len(files)):
                values = reads_values[i] 
                for j in range(n_fragments):
                    if j != viewpoint_fragments[i]:
                        # the distance is to the surface, not to the center, so add radius*2
                        real_d = IMP.core.get_distance(spheres[j],spheres[viewpoint_fragments[i]]) 
                        #real_d = real_d + radius*2
                        real_d = real_d + bead_radii[j] + bead_radii[viewpoint_fragments[i]]
                        should_be_d = values[j] #take out the Z score near 0 average values
                        if should_be_d != 0:
                            total_restraints += 1
                            should_be_d = values[j] + bead_radii[j] + bead_radii[viewpoint_fragments[i]]
                            if (should_be_d + std_dev < real_d  or should_be_d - std_dev > real_d):
                                not_fulfilled += 1
            verboseprint ("total: {}".format(total_restraints))
            verboseprint ("Not fulfilled restraints: {}/{} %{}".format(not_fulfilled,n_restraints[0],not_fulfilled*100/n_restraints[0]))
        # GENERATE THE TXT FILE WITH THE DATA
        f = open (storage_folder+"/"+values_file,"w")  
        for i in range(len(files)):
            for j in range(n_fragments):
                if j != viewpoint_fragments[i]:
                    real_d = IMP.core.get_distance(spheres[j],spheres[viewpoint_fragments[i]]) 
                    real_d = real_d + bead_radii[j] + bead_radii[viewpoint_fragments[i]]
                    f.write(str(real_d)+"\t")
                else:
                    f.write("0\t")
            f.write("\n")  
        f.close()
        for sphere in genome:
            g = IMP.core.XYZRGeometry(sphere)
            w.add_geometry(g)
        verboseprint ("\nModel number {}".format(sample))
        # Divide by large number because we have huge scores with the 3D chromatin. Which is perfectly normal :D
        verboseprint ("Score: ".format(scores[-1]/1000000))
        exv_value = suma2/1000000
        exv_values.append(exv_value)
        verboseprint ("EXV: {}".format(exv_value))
        hub_value = suma3/1000000
        hub_values.append(hub_value)
        verboseprint ("HUB: {}".format(hub_value))
        needed_time = time.time() - start_time         
        verboseprint ("{} seconds.".format(needed_time))       
        verboseprint ("Mean exv for distance {} is: {}".format(y2,np.mean(exv_values))) 
        verboseprint ("Mean hub for distance {} is: {}".format(y2,np.mean(hub_values)))  
        verboseprint ("\nModel number {} finished.".format(sample))
    verboseprint ("Modeling from {} to {} with variables {} {} {} finished".format(starting_point,starting_point+number_of_models,uZ,lZ,y2))
     
def calculate_best_maxd():
        ############# code that evaluates all the models with different distances and gives you which distance is the optimum
    #for each model (50 normally) we will get the length of the chromatin
    if not os.path.exists("{}{}".format(working_dir, prefix)):
        try:
            os.makedirs("{}{}".format(working_dir, prefix))
        except:
            print "\nError creating {} directories.".format(prefix)
            e = sys.exc_info()[1]
            print e
            sys.exit()
    results_path = "{}{}/pre_modeling/{}_best_maxd_results.txt".format(working_dir,prefix,prefix)
    aux_file = "get_genome_length.py"
    number_of_spheres = number_of_fragments - 1
    maxd_list = []
    size_list = []
    with open (results_path,"w") as output_results:
        for maxd in np.arange(from_dist,to_dist+1,dist_bins):
            root = "{}{}/pre_modeling/{}_output_0.1_-0.1_{}/".format(working_dir,prefix,prefix,maxd)
            all_distances = []
            for i in range(pre_number_of_models):
                ###### we get the lengths of all models
                with open (aux_file,'w') as output:
                    output.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"{}\")\n".format(root))
                    output.write("rc(\"open {}{}.py\")\n".format(prefix,i))
                    for j in range (number_of_spheres):
                        output.write("rc(\"distance #"+str(j)+" #"+str(j+1)+"\")\n")
                distance_output = subprocess.check_output(["chimera", "--nogui", aux_file])
                ## reformat the output and read the distances
                #Distance between #297:1@ and #298:1@: 1131.491
                distance_sum = 0
                string = ""
                lista = []
                for line2 in distance_output:
                    string = string + line2
                    if line2 == "\n":
                        lista.append(string)
                        string = ""
                for line2 in lista:
                    distance = re.search(r'Distance between',line2)
                    if distance:
                        distance = float(line2.split(' ')[5])
                        distance_sum = distance_sum + distance
                all_distances.append(distance_sum)
            size = np.mean(all_distances)
            output_results.write("With max distance {}: {}A Equivalent to a genome of {} Mbp\n".format(maxd,size,size/0.0846/1000000)) #in Mbp #number that comes from the radius of nucleotides. See Modeling function.
            maxd_list.append(maxd)
            size_list.append(size/0.0846/1000000)
            verboseprint ("With max distance {}: {}A Equivalent to a genome of {} Mbp".format(maxd,size,size/0.0846/1000000))
    if os.path.isfile(aux_file):
        os.remove(aux_file)
        os.remove(aux_file+"c")
    print "Log written in: {}".format(results_path)
    output_results.close()
    ####calculate best maxd
    locus_size_mbp = locus_size/1000000.0
    best_value = min(size_list, key=lambda x:abs(x-locus_size_mbp))
    best_maxd = maxd_list[size_list.index(best_value)]
    return best_maxd

def calculate_heatdifference(path, n_files_inside,files,plot):        
    #FIRST CALCULATE OUR MODELS HEATMAP
    y2 = re.split('_',path)[-1] 
    y2 = int(re.split('\.',y2)[0])
    all_data = []
    number_of_reads = 0
    for i in range(n_files_inside):
        all_modified_arrays = []
        with open("{0}/{1}{2}.txt".format(path,prefix,i),"r") as f: 
            five_arrays = []
            for line in f:
                array = re.split('\t',line)
                reads = np.genfromtxt(array)
                five_arrays.append(reads)
                number_of_reads = len(reads)
                #the data is independent so get the values for each array in five_arrays
            for array in five_arrays:
                x1 = min(array)
                x2 = max(array)
                y1 = putative_minimum_size  
                slope = (y2-y1) / (x2-x1)
                array_modified = [slope*(read-x1)+y1 for read in array]
                all_modified_arrays.append(array_modified)
            all_data.append(all_modified_arrays)
    #calculate mean of all arrays
    mean_all_data = []
    # first we will calculate the mean for a gen_array, so we need to to this 5 times.
    for i in range(len(files)): 
        mean_one_gene_array = []
        for j in range(number_of_reads):
            value = 0
            for k in range(len(all_data)): 
                current_array = all_data[k]
                value = value + current_array[i][j]
            mean = value/len(all_data)
            mean_one_gene_array.append(mean)
        mean_all_data.append(mean_one_gene_array)
    if plot:
        fig = plt.figure(figsize=(10,10))   
        ax = plt.subplot(2,1,2)
        z = np.array(mean_all_data)
        c = plt.pcolor(z,cmap=plt.cm.terrain_r)
        plt.colorbar()
        ax.set_yticks(np.arange(z.shape[1])+0.5, minor=False)
        plt.axis([0,z.shape[1],0,z.shape[0]])
        labels = [(x.split("/")[-1])[:15] for x in files]
        ax.set_yticklabels(labels)
        plt.xlabel("Beads")

    #NOW CALCULATE THE 4C DATA'S HEATMAP (WITHOUT APLLYING LOG)
    HEAT_MAP_DATA, HEATMAP_DATA_LOG= calculateNWindowedDistances(fragments_in_each_bead,0,0,y2,files,False,True) #stored in HEATMAP_DATA_LOG
    heatmap_data_modified = []
    for array in HEAT_MAP_DATA:
    # without log
        x1 = max(array)
        x2 = min(array)
        y1 = putative_minimum_size  
        slope = (y2-y1) / (x2-x1)
        array_modified = [slope*(read-x1)+y1 for read in array]
        heatmap_data_modified.append(array_modified)
    if plot: 
        plt.title("Top: Raw data reads per bear. \nBottom: Average distance between beads of the models.")
        ax = plt.subplot(2,1,1)
        z = np.array(heatmap_data_modified)
        c = plt.pcolor(z,cmap=plt.cm.terrain_r)
        plt.colorbar()
        ax.set_yticks(np.arange(z.shape[1])+0.5, minor=False)
        plt.axis([0,z.shape[1],0,z.shape[0]])
        labels = [(x.split("/")[-1])[:15] for x in files]
        ax.set_yticklabels(labels)
        plt.subplots_adjust(bottom=0.1, right=0.999, top=0.9, left=0.2)
        plt.savefig('{}_heatmap.png'.format(path))
        plt.close('all')
    #CALCULATE THE DIFFERENCE
    array2 = []
    for i in (mean_all_data):
        for j in i:
            array2.append(j)
    array1 = []
    for i in (heatmap_data_modified):
        for j in i:
            array1.append(j)
    spearman_value = spearmanr(array1,array2)[0]
    verboseprint("Spearman correlation for {}: {}".format(path,str(spearman_value)))
    return spearman_value

def calculate_best_zscores():
    results_path = "{}{}/pre_modeling/{}_heatmap_difference_results.txt".format(working_dir,prefix,prefix)
    with open (results_path,"w") as output_results:
        all_scores = []
        best_uZ = 0
        best_lZ = 0
        best_score = 0.0
        for uZ in np.arange(from_zscore,to_zscore+zscore_bins,zscore_bins):
            for lZ in np.arange(-from_zscore, -to_zscore-zscore_bins, -zscore_bins):
                score = calculate_heatdifference(working_dir+prefix+"/pre_modeling/"+prefix+"_output_"+str(uZ)+"_"+str(lZ)+"_"+str(max_distance),pre_number_of_models,files,plot)
                output_results.write(str(uZ)+","+str(lZ)+","+str(max_distance)+"\t"+str(score)+"\n")
                all_scores.append(score)
                if score > best_score :
                    best_uZ = uZ
                    best_lZ = lZ
                    best_score = score
        output_results.write("Max: {}".format(max(all_scores)))   
    if plot:
        print "\nFigures comparing raw data vs modeling were created in {}{}/".format(working_dir,prefix)
    return best_uZ,best_lZ

def run_analysis(std_dev,cut_off_percentage):
    models_subset = []
    std_dev = std_dev
    cut_off_percentage = cut_off_percentage
    root = "{}{}/{}_output_{}_{}_{}/".format(working_dir,prefix,prefix,uZ,lZ,max_distance)
    score_file = "{}/score.txt".format(root)
    pyfiles = [ f for f in listdir(root) if isfile(join(root,f)) and f.endswith(".py") ]
    number_of_models = len(pyfiles)
    try:
        os.remove(root+"score.txt")
    except OSError:
        pass
    scorefiles = [ f for f in listdir(root) if isfile(join(root,f)) and f.startswith("score") ]
    number_of_score_files = len(scorefiles)
    jump = total_number_of_models / number_of_score_files
    models = defaultdict(list) # dict: each model has a list of 2 values
    # first we create a unified score.txt
    with open (score_file,"w") as f:
        counter = 0
        for i in range(number_of_score_files):
            with open (root+"score"+str(counter)+".txt", "r") as f2:
                for line in f2:
                    f.write(line)
            counter = counter + jump
    # create the dictionary and populate it
    with open (score_file, "r") as f:
        counter = 0
        for line in f:
            counter += 1
            model = []
            values = re.split("\t", line)
            number = int(values[0])
            score = float(values[1])
            model.append(score)
            models[number] = model
            if counter == number_of_models:
                break
    # models = models[:number_of_models]    #take only the first ones 
    reads_values,reads_weights,start_windows, end_windows = calculateNWindowedDistances(int(fragments_in_each_bead),uZ,lZ, max_distance,files)
    ### get all distances from all the models
    print "getting best {} models".format(subset)
    all_distances_all_models = []
    for i in range(number_of_models):
        distances_in_model = []
        with open (root+prefix+str(i)+".txt","r") as f:
            for line in f:
                value = re.split("\t",line)
                distances_in_model.append(value[:-1]) #dont store "\n"
        all_distances_all_models.append(distances_in_model)
    ## Evaluation
    if std_dev == 0:
        std_dev = max_distance / 20  	
    increase_dev_or_cutoff = 0
    not_analyzed = True
    increase_dev_or_cutoff = 0
    stop_analysis_count = 1000
    while not_analyzed:   
        print "Running Analysis with:"
        print "Std_dev: {}".format(std_dev)
        print "cut_off_percentage: {}".format(cut_off_percentage)
        analized_models = 0
        ok_models = 0
        i = 0
        delete_models_list = []
        analysis_count = 0
        last_accumulative_percentage = 0
        for distances_in_model in all_distances_all_models:
            #EVALUATION
            not_fulfilled = 0
            total = 0
            for k in range(len(files)):
                values = reads_values[k]
                try: 
                    for j in range(number_of_fragments):
                        if j != viewpoint_fragments[k]:
                            real_d = distances_in_model[k][j]
                            should_be_d = values[j] 
                            if should_be_d != 0:
                                total += 1
                                if (should_be_d + std_dev < float(real_d)  or should_be_d - std_dev > float(real_d)):
                                    not_fulfilled += 1
                                    #verboseprint ("Restraint " +str(j)+"-"+str(viewpoint_fragments[k])+" is "+str(real_d)+" and should be "+str(should_be_d)+" +- "+str(std_dev)+". Difference: "+str(should_be_d-float(real_d)))
                except:
                    print "Something went wrong. Check --fragments_in_each_bead. Did you modify it in the modeling?"
                    sys.exit()
            not_fulfil_percentage = not_fulfilled*100/total
            verboseprint( "not_fulfilled -> {} out of {} restraints: {}% of all restraints are not fulfilled in this model.".format(not_fulfilled,total,not_fulfil_percentage))
            if not_fulfil_percentage <= cut_off_percentage:
                models[i].append(not_fulfilled)
                ok_models += 1
            else:
                delete_models_list.append(i)
            analized_models += 1
            accumulative_percentage = 100*ok_models/analized_models
            verboseprint ("Percentage of models that fulfill the threshold: {}%".format(accumulative_percentage))
            verboseprint ("{}/{}".format(ok_models,analized_models))
            #after poplating all and takign out the models out of the cut off, take the subset of models
            i += 1
            #Check if delta (difference with fulfil_percentage every round) changed analyzing 100 models. If it did not, loose more the threshold
            if last_accumulative_percentage == accumulative_percentage and accumulative_percentage <= subset*100.0/total_number_of_models:
                analysis_count += 1
            if stop_analysis_count == analysis_count:
                forced_break = True
                break
            last_accumulative_percentage = accumulative_percentage
            forced_break = False
            if (analized_models) % 1000 == 0:
                sys.stdout.write("\r{}%".format( analized_models*100/total_number_of_models))
        print	
        if not forced_break:	
            #take out models from dict
            for number in delete_models_list:
                try:
                    del models[number]
                except:
                    print "Can't delete model number {}. Are you working with the correct models? ".format(i)
                    sys.exit()
            #order the dictionary by score
            sorted_models = sorted(models.items(), key=operator.itemgetter(1))
            print "Number of models above cutoff: {}".format(len(sorted_models))
            if len(sorted_models) >= subset:
            # store them in a directory
                storage_folder = working_dir+prefix+"/"+prefix+"_final_output_"+str(uZ)+"_"+str(lZ)+"_"+str(max_distance)+"/" #the dir where the data will be saved
                if not os.path.exists(storage_folder): 
                    os.makedirs(storage_folder)
                try: 
                    models_subset = sorted_models [:subset]
                    for k in range(subset):
                        i = models_subset[k][0]
                        shutil.copyfile("{}{}{}.py".format(root,prefix,i), "{}{}{}.py".format(storage_folder,prefix,i) )
                        shutil.copyfile("{}{}{}.txt".format(root,prefix,i), "{}{}{}.txt".format(storage_folder,prefix,i) )
                    print "copied best {} models to {}.".format(subset,storage_folder)
                except:
                    print "Error copying best models."				
                not_analyzed = False
            else:
                print "! Can not get {} models. Relaxing the std_dev and cut_off_percentage...\n ".format(subset)	
                #Modify the cutoffs
                if increase_dev_or_cutoff == 0:
                    std_dev = std_dev + max_distance*0.01 #increase std_def
                    increase_dev_or_cutoff = 1
                else:
                    cut_off_percentage = cut_off_percentage+2 #increase #cut_off
                    increase_dev_or_cutoff = 0	 
        else:
            print "! Can not get {} models. Relaxing the std_dev and cut_off_percentage...\n ".format(subset)	
            #Modify the cutoffs
            if increase_dev_or_cutoff == 0:
                std_dev = std_dev + max_distance*0.01 #increase std_def
                increase_dev_or_cutoff = 1
            else:
                cut_off_percentage = cut_off_percentage+2 #increase #cut_off
                increase_dev_or_cutoff = 0	

    # create the file to open in chimera
    # superposition of the best models
    with open(working_dir+prefix+"_superposition.py","w") as f:
        f.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\""+root+"\")\n")
        f.write("rc(\"open {}{}.py\")\n".format(prefix,models_subset[0][0]))
        for k in range(1,subset):
            i = models_subset[k][0]
            f.write("rc(\"open {}{}.py\")\n".format(prefix,i))
            f.write("rc(\"match #{}-{} #0-{}\")\n".format(k*number_of_fragments,k*number_of_fragments+number_of_fragments-1,number_of_fragments-1))
    print "Superposition of {} models created in {}{}\n".format(subset,working_dir,prefix)
    return std_dev,cut_off_percentage,models_subset

def run_clustering(models_subset):
    number_of_beads = number_of_fragments
    root = "{}{}/{}_final_output_{}_{}_{}/".format(working_dir,prefix,prefix,uZ,lZ,max_distance)	
    matrix = np.zeros((subset,subset))
    only_python_files = []
    for model_number in models_subset:
        only_python_files.append(root+prefix+str(model_number[0])+".py") #took out root+
    if len(only_python_files) != subset:
        print "There are no {} models in {}. \nOnly {} models were found in the directory. Redo the analysis with a smaller subset or generate more models.".format(subset,root,len(only_python_files))
        sys.exit()
    # generate a chimera file with match. Chimera when matched, it calculates the RMSD 
    number_of_beads = number_of_beads -1
    combi = combinations(range(subset),2)
    instructions = []
    print "Generating instructions..."
    number_of_files = 0
    for pair in combi:
        instruction_files = []
        number_of_files += 1
        counter_line = pair[0]
        counter_column = pair[1]
        chimera_file = "{}_calculate_rmsd{}_{}.py".format(prefix,counter_line,counter_column)
        rmsd_file = open (chimera_file, "w")
        rmsd_file.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"{}\")\n".format(root))
        rmsd_file.write("rc(\"open {}\")\n".format(only_python_files[counter_line]))
        rmsd_file.write("rc(\"open {}\")\n".format(only_python_files[counter_column]))
        rmsd_file.write("rc(\"match #{}-{} #{}-{}\")\n".format((number_of_beads+1),(number_of_beads+1)+number_of_beads ,0,number_of_beads))
        rmsd_file.close()
        instruction_files.append(chimera_file)
        instruction_files.append(counter_line)
        instruction_files.append(counter_column)
        instructions.append(instruction_files)
    print "Populating matrix.txt ..."
    for core in range(0,number_of_files,number_of_cpus):
        if len(instructions) - core < number_of_cpus:
            execute = instructions[core:len(instructions)-core]
        else:
            execute = instructions[core:core+number_of_cpus] 
        # WE NEED TO EXECUTE THIS DEPENDING ON CPU SIZE
        rmsd_output = p.map(chimera_worker,execute)
        for i in range(len(execute)):
            string = ""
            lista = []
            for line2 in rmsd_output[i][0]:
                string = string + line2
                if line2 == "\n":
                    lista.append(string)
                    string = ""
            #regexp this: RMSD between 103 atom pairs is 4404.816 angstroms
            for line2 in lista:
                exp = re.search(r"(\d+\.\d+) angstroms",line2)
                if (exp):
                    value = exp.group(1)
                    matrix[rmsd_output[i][1]][rmsd_output[i][2]] = value
                    matrix[rmsd_output[i][2]][rmsd_output[i][1]] = value    
                    value = 0
        #delete files while we finish executing them
        for i in range(len(execute)):
            remove(execute[i][0])
            remove(execute[i][0]+"c")
        if core!= 0:
            sys.stdout.write("\r{}%".format( core*100/number_of_files))
            sys.stdout.flush()
    #write matrix       
    matrixtxt = open("{}matrix.txt".format(root), "w")      
    matrixtxt.write("\t")
    #leave only the name of the file
    only_python_files = [f.split("/")[-1] for f in only_python_files]
    for p_file in only_python_files:
        matrixtxt.write(p_file)
        matrixtxt.write("\t")
    matrixtxt.write("\n")
    counter_line = 0
    for line in only_python_files:
        counter_column = 0
        matrixtxt.write(line)
        matrixtxt.write("\t")
        for column in only_python_files:
            matrixtxt.write(str(matrix[counter_line][counter_column])+"\t")  
            counter_column += 1
        counter_line += 1
        matrixtxt.write("\n") 
    matrixtxt.close()
    print "\n\nmatrix.txt written! in {}".format(root)
    print "This is the whole RMSD matrix (all models vs all models)"
    #compute and plot dendogram
    D = matrix
    fig = plt.figure(figsize=(8,8))
    ax1 = fig.add_axes([0.09,0.1,0.2,0.6])
    Y = sch.linkage(D, method='average')
    Z1 = sch.dendrogram(Y, orientation='right')
    ax1.set_xticks([])
    ax1.set_yticks([])
    dendogra_colors = Z1['color_list']
    # Plot dendrogram.
    ax2 = fig.add_axes([0.3,0.71,0.6,0.2])
    Y = sch.linkage(D, method='average')
    Z2 = sch.dendrogram(Y,orientation='top')
    ax2.set_xticks([])
    ax2.set_yticks([])
    # Plot distance matrix.
    axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
    idx1 = Z1['leaves']
    idx2 = Z2['leaves']
    D = D[idx1,:]
    D = D[:,idx2]
    plt.xlabel("RMSD matrix in Angstroms.")
    im = axmatrix.matshow(D, aspect='auto', origin='lower', cmap=plt.cm.YlGnBu)
    axmatrix.set_xticks([])
    axmatrix.set_yticks([])
    # Plot colorbar.
    axcolor = fig.add_axes([0.91,0.1,0.02,0.6])
    plt.colorbar(im, cax=axcolor)
    try:
        fig.savefig('{}{}_heatmap.png'.format(root,prefix))
        print "\n clusters can be checked here: {}{}_heatmap.png".format(root,prefix)
    except:
        pass
    # Code to retrieve the clusters
    n = subset
    cluster_number = []
    cluster_dict = dict()
    solutions = [] #gather the clustering proccesses when we have the same number as kmeans 
    for i in range(subset-2): #descend branches until the bottom
        new_cluster_id = n+i
        old_cluster_id_0 = Y[i, 0]
        old_cluster_id_1 = Y[i, 1]
        combined_ids = list()
        if old_cluster_id_0 in cluster_dict:
            combined_ids += cluster_dict[old_cluster_id_0]
            del cluster_dict[old_cluster_id_0]
        else:
            combined_ids += [old_cluster_id_0]
        if old_cluster_id_1 in cluster_dict:
            combined_ids += cluster_dict[old_cluster_id_1]
            del cluster_dict[old_cluster_id_1]
        else:
            combined_ids += [old_cluster_id_1]
        cluster_dict[new_cluster_id] = combined_ids
        if len(cluster_dict) == k_mean:
            aux_dict = dict(cluster_dict)
            solutions.append(aux_dict)
    cluster_dict_def = solutions[-1]    
    #get only the last clustering, since it is the one with all models
    for i in cluster_dict_def:
        cluster_number.append(i)         
    number_of_beads = number_of_beads +1 
    # Write the matrix data in different files, k_mean times
    for i in cluster_number:
        matrixtxt = open("{}matrix{}.txt".format(root,i), "w")      
        matrixtxt.write("\t")
        cluster_values = [int(j) for j in cluster_dict_def[i]]
        cluster_models = [only_python_files[k] for k in cluster_values]
        for p_file in cluster_models:
            matrixtxt.write(p_file)
            matrixtxt.write("\t")
        matrixtxt.write("\n")
        counter_line = 0
        for line in cluster_models:
            counter_column = 0
            matrixtxt.write(line)
            matrixtxt.write("\t")
            for column in cluster_models:
                matrixtxt.write(str(matrix[counter_line][counter_column])+"\t")  
                counter_column += 1
            counter_line += 1
            matrixtxt.write("\n") 
        matrixtxt.close()
        print "\n------"
        print "\nmatrix{}.txt written! in {}".format(i,root)
        print "This is one of the clusters. These models are more similar between them." 
        # create the file to open in chimera
        # superposition of the best models
        print "Creating superposition of this cluster..."
        with open(working_dir+prefix+"/"+prefix+"_superposition_"+str(i)+".py","w") as f:
            f.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\""+root+"\")\n")
            f.write("rc(\"open {}\")\n".format(cluster_models[0]))
            for k in range(1,len(cluster_models)):
                imodel = cluster_models[k]
                f.write("rc(\"open {}\")\n".format(imodel))
                f.write("rc(\"match #{}-{} #0-{}\")\n".format(k*number_of_beads,k*number_of_beads+number_of_beads-1,number_of_beads-1))
        print "created in {}{}/{}_superposition".format(working_dir,prefix,prefix)
    n_clusters = len(set(dendogra_colors))-1
    print "\n{} clusters were found in the clustering process.".format(n_clusters)
    if k_mean != n_clusters:
        print "Number of clusters found (different conformations) and k means value (expected conformations, default is 2) set are different. " 
    lines_in_file = 0
    for m in cluster_number:
        num_lines = sum(1 for line in open('{}matrix{}.txt'.format(root,m)))
        if num_lines > lines_in_file:
            biggest_matrix = m
            lines_in_file = num_lines
    return n_clusters, biggest_matrix
    
def calculate_vhic(biggest_matrix,calculate_the_matrix):
    root = "{}{}/{}_final_output_{}_{}_{}/".format(working_dir,prefix,prefix,uZ,lZ,max_distance)
    matrix_path = "{}matrix{}.txt".format(root,biggest_matrix)
    distance_file = "get_genome_distance_{}".format(prefix)
    path = "{}vhic_{}.txt".format(root,prefix)
    start_time = time.time()
    if calculate_the_matrix:
        print "Calculating in chimera..."       
        models = []
            ## we get a file that (cmd) that we are gonna use it in chimera. It will write all distances in the model
        with open("{}".format(matrix_path), "r") as mtx:
            for line in mtx:
                models = re.split("\t", line)
                break
        models = models[1:-1]
        counter = 0
        matrix = np.zeros((number_of_fragments,number_of_fragments,len(models)))
        p = Pool(number_of_cpus)
        for model in models:
            verboseprint ("{} - {}".format(counter,model))
            chimera_files = []
            combi = combinations(range(0,number_of_fragments),2)
            instruction_list = []
            for pair in combi:
                instruction_list.append("rc(\"distance #"+str(pair[0])+" #"+str(pair[1])+"\")\n")
            for cpu in range(number_of_cpus):
                instru_start = (cpu) * (len(instruction_list)/number_of_cpus) 
                if cpu == number_of_cpus-1:
                    instru_end =  len(instruction_list)
                else:
                    instru_end =  (cpu+1) * (len(instruction_list)/number_of_cpus) 
                dis_file = distance_file+"cpu"+str(cpu)+".py"
                with open (dis_file,'w') as output:
                    output.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"{}\")\n".format(root))
                    output.write("rc(\"open {}\")\n".format(model))
                    for instru in instruction_list[instru_start:instru_end]:
                        output.write(instru)
                    chimera_files.append(dis_file)                
            distance_output = p.map(chimera_worker_vhic,chimera_files)
            final_distance_output = []
            for cha in range(len(distance_output)):   
                final_distance_output = chain(final_distance_output,distance_output[cha])
            string = ""
            lista = []
            for line2 in final_distance_output:
                string = string + line2
                if line2 == "\n":
                    lista.append(string)
                    string = ""
            #Distance between #209:1@ and #210:1@: 512.326
            for line2 in lista:
                distance = re.search(r'#(\d*).*#(\d*).*:\s?(\d*\.\d*)',line2)  
                if (distance):
                    matrix[int(distance.group(1))][int(distance.group(2))][counter] = float(distance.group(3))
                    matrix[int(distance.group(2))][int(distance.group(1))][counter] = float(distance.group(3))
            counter += 1        
            verboseprint ("{} seconds needed.".format(time.time() - start_time))
        f= open(path, 'w') #store the data in file
        matrix_mean = np.zeros((number_of_fragments,number_of_fragments))
        for line in range(number_of_fragments):
            for column in range(number_of_fragments):
                mean_value = np.mean(matrix[line][column])
	        #print "[{}][{}] = {}".format(line,column,mean_value)
                matrix_mean[line][column] = mean_value
		#matrix_mean[column][line] = mean_value
                f.write(str(line)+","+str(column)+","+str(mean_value))   
                f.write("\n")
        f.close()
        print "\nThe virtual Hi-C data is in {}.".format(path)
        for chi_file in chimera_files:
            os.remove(chi_file)
            os.remove(chi_file+"c")
    else:
        with open(path, 'r') as std_in:
            matrix_mean = np.zeros((number_of_fragments,number_of_fragments))
            for line in std_in:
                values = line.split(",")
                matrix_mean[int(values[0])][int(values[1])] = float(values[2])
    print "Generating virtual Hi-C plot..."     
    show_fragments_in_vhic_shifted = [c+0.5 for c in show_fragments_in_vhic] #to match the name_of_fragments in the matrix Since the ticks don't match with the heatmap.
    fig = plt.figure()
    plt.title("Virtual Hi-C")
    ax = plt.subplot(1,1,1)
    z = np.array(matrix_mean)
    cmap = plt.cm.get_cmap(colormap)
    c = plt.pcolor(z,cmap=cmap,vmax=maximum_hic_value, vmin=0)
    ax.set_frame_on(False)
    cb = plt.colorbar()
    cb.solids.set_edgecolor("face")
    plt.scatter(show_fragments_in_vhic_shifted, show_fragments_in_vhic_shifted, s=20, c=color_of_fragments,cmap=plt.cm.autumn)
    ax.set_yticks(show_fragments_in_vhic_shifted)
    ax.set_yticklabels(name_of_fragments, minor=False)
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.axis([0,z.shape[1],0,z.shape[0]])
    fig.set_facecolor('white')
    #to get pdf instead of png
    #pp = PdfPages('{}{}_vHiC.pdf'.format(root,prefix))
    #pp.savefig(fig)
    #pp.close()
    plt.savefig('{}{}_vHiC.png'.format(root,prefix),dpi=1000)
    print '\nVirtual HiC.pdf written in {}{}_HiC.pdf'.format(root,prefix)
    
def calculate_representative_model(biggest_matrix):
    number_of_beads = number_of_fragments
    root = "{}{}/{}_final_output_{}_{}_{}/".format(working_dir,prefix,prefix,uZ,lZ,max_distance)
    matrix_file = "{}matrix{}.txt".format(root,biggest_matrix)
    ########### FIRST GET THE PDB MODELS
    #pdb directory will be inside the final models directory
    pdb_output = "{}pdb_output/".format(root)
    if not os.path.exists(pdb_output): os.makedirs(pdb_output)
    write_pdb = "{}get_genome_pdbs.py".format(root)
    models = []
    with open(matrix_file, "r") as mtx:
        for line in mtx:
            models.append(re.split("\t", line)[0])
    models = models[1:]
    
    # in chimera:
    # open all files (half of matrix)
    # match all files
    # combine all files
    # write the pdb file
    
    counter = 1
    with open (write_pdb,'w') as output:
        verboseprint("Executing {}...".format(write_pdb))
        output.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"{}\")\n".format(root))
        verboseprint( "0 - {}".format(models[0]))
        output.write("rc(\"open {}\")\n".format(models[0]))
        for model in models[1:]:
        # for model in models[-2:]:
            verboseprint( "{} - {}".format(counter,model))
            output.write("rc(\"open {}\")\n".format(model))
            counter += 1       
        for model in range(len(models)-1):
            output.write("rc(\"match #{}-{} #0-{}\")\n".format((model+1)*number_of_beads,(model+1)*number_of_beads+number_of_beads-1,number_of_beads-1))
        start_id = len(models)*number_of_beads    
        for model in range(len(models)):
            output.write("rc(\"combine #{}-{} newchainids False name combine modelId {}\")\n".format(model*number_of_beads,(model*number_of_beads+number_of_beads-1),start_id))
            output.write("rc(\"write format pdb #{} {}{}.pdb\")\n".format(start_id,pdb_output,models[model][:-3])) #with -3 we take out the ".PY"
            start_id+=1      
    verboseprint("writting pdb-s... it can take time..." )       
    distance_output = subprocess.check_output(["chimera", "--nogui", write_pdb])
    verboseprint("Pdb's written. Calculating average model...")
    os.remove(write_pdb)         
    ########## NOW WE GET THE AVERAGE MODEL
    color_grey = "#b333b333b333"
    color_gene = "#ffffb3330000"
    #get the pdb files 
    pdbFiles = [ f for f in listdir(pdb_output) if isfile(join(pdb_output,f)) ]
    #get the x y and z position of all beads of all models
    all_models = []
    for pdbFile in pdbFiles:
        one_model = []
        with open("{}{}".format(pdb_output,pdbFile), "r") as f:
            for line in f:
                values = re.search(r'HETATM\s+\d+\s+\*{4}\s+\d+\s{4}(.{8})(.{8})(.{8})',line)  
                if values:
                    value_tuple = (float(values.group(1)),float(values.group(2)),float(values.group(3)))
                    one_model.append(value_tuple)
        all_models.append(one_model)
    mean_model = []
    for bead in range(number_of_beads):   
        lista_x = []
        lista_y = []
        lista_z = []           
        for model in all_models:
            lista_x.append(model[bead][0]) #get the X value of all models for each bead
            lista_y.append(model[bead][1])
            lista_z.append(model[bead][2])
        x_media = np.mean(lista_x)
        y_media = np.mean(lista_y)
        z_media = np.mean(lista_z)
        distance_tuple = (x_media,y_media,z_media)
        mean_model.append(distance_tuple)
    #mean model has the values in tuples of the mean for each bead
    #now get the model more similar to these mean values
    sum_of_distances = []
    for model in all_models:
        d_sum = 0
        for bead in range(number_of_beads):
            d = (model[bead][0]-mean_model[bead][0])**2 + (model[bead][1]-mean_model[bead][1])**2 + (model[bead][2]-mean_model[bead][2])**2
            square_d = np.sqrt(d)
            d_sum = d_sum + square_d
        sum_of_distances.append(d_sum)  
    print "\nModel closest to average (Representative):"
    # print sum_of_distances.index(min(sum_of_distances))
    print pdbFiles[sum_of_distances.index(min(sum_of_distances))][:-2]+"y"
    print "Most different model to average:"
    print pdbFiles[sum_of_distances.index(max(sum_of_distances))][:-2]+"y"
    #sum_of_distances.remove(max(sum_of_distances))
    #print "Second MAX:"
    #print pdbFiles[sum_of_distances.index(max(sum_of_distances))]
    # save all models of this matrix in another dir
    storage_folder =  "{}mtx1_models/".format(root)
    print "\nCopying models from the same cluster in: {}".format(storage_folder)
    if not os.path.exists(storage_folder): os.makedirs(storage_folder)   
    for i in pdbFiles:
        i = i[:-4] #take out ".pdb" suffix
        shutil.copyfile("{}/{}.py".format(root,i), "{}{}.py".format(storage_folder,i) )
        shutil.copyfile("{}/{}.txt".format(root,i), "{}{}.txt".format(storage_folder,i) ) 
    number_of_files_to_super = pdbFiles
    number_of_beads = number_of_beads - 1 
    with open("{}superposition.cmd".format(storage_folder),"w") as superposition:
        for i in number_of_files_to_super:
            i = i[:-4]
            superposition.write("open {}.py \n".format(i))
        for i in range(len(number_of_files_to_super)):
            for j in range(number_of_beads+1):
                if j in viewpoint_fragments:
                    superposition.write("color {} #{}\n".format(color_gene,j+i*(number_of_beads+1)))
                else:
                    superposition.write("color {} #{}\n".format(color_grey,j+i*(number_of_beads+1)))
            i += 1      
        for i in range(len(number_of_files_to_super)-1):
            i += 1
            superposition.write("match #{}-{} #0-{}\n".format(i*(number_of_beads+1),i*(number_of_beads+1)+number_of_beads,number_of_beads))
        for i in range(len(number_of_files_to_super)):
            superposition.write("shape tube #{}-{} radius 20 bandlength 10000\n".format(i*(number_of_beads+1),i*(number_of_beads+1)+number_of_beads))
        #if we want a model to be highlighted
    #     for i in range(len(number_of_files_to_super)):
    #         if number_of_files_to_super[i] == "HoxGenomeZebra21741.pdb":
    #             superposition.write("shape tube #{}-{} radius 100 bandlength 10000\n".format(i*(number_of_beads+1),i*(number_of_beads+1)+number_of_beads)) 
    #         else:
    #             superposition.write("shape tube #{}-{} radius 20 bandlength 10000\n".format(i*(number_of_beads+1),i*(number_of_beads+1)+number_of_beads))
            superposition.write("close #{}-{}\n".format(i*(number_of_beads+1),i*(number_of_beads+1)+number_of_beads))
    print "Superposition file generated in {}superposition.cmd. Open it with UCSF Chimera.".format(storage_folder)
    shutil.copyfile("{}{}".format(root,pdbFiles[sum_of_distances.index(min(sum_of_distances))][:-2]+"y"), "{}Representative.py".format(root,i) )
    shutil.copyfile("{}{}".format(root,pdbFiles[sum_of_distances.index(max(sum_of_distances))][:-2]+"y"), "{}LeastRepresentative.py".format(root,i) )
    print "Representative.py and LeastRepresentative.py models saved in: {}".format(root)
    with open ("{}Representative_tubes.cmd".format(root), "w") as out:
        out.write("open {}Representative.py\n".format(root,i))
        out.write("shape tube #0-{} radius 300 bandlength 10000\n".format(number_of_beads))
        out.write("close #0-{}\n".format(number_of_beads))
    with open ("{}LeastRepresentative_tubes.cmd".format(root), "w") as out:
        out.write("open {}LeastRepresentative.py\n".format(root,i))
        out.write("shape tube #0-{} radius 300 bandlength 10000\n".format(number_of_beads))
        out.write("close #0-{}\n".format(number_of_beads))
    print "Representative_tube.cmd and LeastRepresentative_tubes.cmd models saved in: {}".format(root)
    print "Open them with UCSF Chimera."

########################################## MAIN ##########################################
working_dir = (os.path.realpath(__file__)).split("/")[:-1]
working_dir = "/".join(working_dir)+"/"
max_distance = 0 #updated in calculate_best_maxd()
uZ = 0 #updated in calculate_best_zscores
lZ = 0 #updated in calculate_best_zscores
parser = argparse.ArgumentParser(
description='''Program that generates 3D models and a virtual Hi-C of your favourite region.''',
epilog= """Apart from the 4C data, a primers.txt file is needed in that folder, which has 4C file name and position of the gene. 
Optionaly, a primers_vhic.txt file can be also created to paint interesting positions in the virtual Hi-C. 
File needs to be like this: gene_name chrN:position color. Color written as yellow, red, green or other colors.""")
group1 = parser.add_argument_group('Pre-modeling', 'Parameters used in the pre-modeling')
group2 = parser.add_argument_group('Modeling', 'Parameters used in the modeling')
group3 = parser.add_argument_group('Analysis and clustering', 'Parameters used in the analysis and clustering')
group4 = parser.add_argument_group('Virtual Hi-C', 'Parameters used in the generation of the virtual Hi-C')
group5 = parser.add_argument_group('Global', 'Global parameters used in the modeling')
group1.add_argument("--preNmodels",
        type=int, 
        default=50, 
        action="store", 
        dest="pre_number_of_models",
        help='number of models that will be generated in the pre-modeling phase')
group1.add_argument("--from_dist",
        type=int, 
        metavar = "minimum_distance", 
        default=5000, 
        action="store", 
        dest="from_dist",
        help='minimum max-distance that will be used in the pre-modeling phase')
group1.add_argument("--to_dist",
        type=int, 
        metavar = "maximum_distance", 
        default=15000, 
        action="store", 
        dest="to_dist",
        help='maximum max-distance that will be used in the pre-modeling phase')
group1.add_argument("--dist_bins",
        type=int, 
        default=1000, 
        action="store", 
        dest="dist_bins",
        help='size of jump between from_dist and to_dist')
group1.add_argument("--from_zscore",
        type=float, 
        metavar = "minimum_Zscore", 
        default=0.1, 
        action="store", 
        dest="from_zscore",
        help='minimum Z-score that will be used in the pre-modeling phase')
group1.add_argument("--to_zscore",
        type=float, metavar = "maximum_Zscore",
        default=1.2, 
        action="store", 
        dest="to_zscore",
        help='maximum Z-score that will be used in the pre-modeling phase')
group1.add_argument("--zscore_bins",
        type=float, 
        default=0.1, 
        action="store", 
        dest="zscore_bins",
        help='size of jump between from_zscore and to_zscore')
group2.add_argument("--Nmodels",
        type=int, 
        default=50000, 
        action="store", 
        dest="number_of_models",
        help='number of models that will be generated in the modeling phase')
group2.add_argument("--ignore_beads",
        type=int, 
        action="store",
        nargs="+",
        default=[], 
        dest="ignore_beads",
        help='Beads that are not gonna have distance restraints. E.g. Beads that correspond to repetitive regions impossible to map. If many, separate with commas. Also affects the pre-modeling')
group2.add_argument("--number_of_beads_to_ignore_near_viewpoint", "-iv",
        type=int, 
        action="store",
        default=0, 
        dest="ignore_viewpoint_beads",
        help='Number of beads upstream and downstream of the viewpoint that will be ignored. E.g. Our 4C data is corrected near the viewpoint to normalize the reads biased by the PCR. Also affects the pre-modeling')
group3.add_argument("--subset",
        type=int, 
        action="store",
        default=200, 
        dest="subset",
        help='Number of best models out of the Modeling process')
group3.add_argument("--std_dev", 
        type=int,
        action="store",
        default=0, 
        dest="std_dev",
        help='Standard deviation of the distances between beads, to be considered fulfilled')
group3.add_argument("--cut_off_percentage",
        type=int, 
        action="store",
        default=10, 
        dest="cut_off_percentage",
        help='Percetange of fulfilled distances in each model to be a good model')
group3.add_argument("--k_value",
        type=int, 
        action="store",
        default=2, 
        dest="k_mean",
        help='Number of cluster to expect in the clustering.')
group4.add_argument("--maximum_hic_value", 
        type=int, 
        action="store",
        dest="maximum_hic_value", 
        default = 0,
        help='The virtual Hi-C gradient color will be from 0 to maximum_hic_value.')
group4.add_argument("--repaint_vhic", 
        action="store_true", 
        dest="repaint_vhic",
        help='repaint_vhic True to generate the virtual Hi-C again. Modify the --maximum_hic_value also.')
group4.add_argument("--colormap", 
        action="store", 
        dest="colormap",
        default = "PuRd_r", 
        help='The colormap of the virtual Hi-C. Matplotlib colormap.')
group5.add_argument("data_dir", 
        action="store",
        help='location of the 4C data. primers.txt needs tobe in there also')
group5.add_argument("prefix", 
        action="store",
        help='Name of the models')
group5.add_argument("--cpu",
        type=int, 
        default=1, 
        action="store", 
        dest="number_of_cpus",
        help='number of CPUs that will be used in this script')
group5.add_argument("--verbose", 
        action="store_true", 
        dest="verbose",
        help='Verbose True for more information while executing the script')
group5.add_argument("--working_dir", 
        action="store",
        default=working_dir, 
        dest="working_dir",
        help='location where the models will be generated')
group5.add_argument("--fragments_in_each_bead", 
        type= int, 
        default=0, 
        dest="fragments_in_each_bead" ,
        action="store",
        help='Number of fragments that will be represented with each bead')
group5.add_argument("--jump_step", 
        action="store",
        choices=['pre_modeling', 'modeling', 'analysis', 'vhic','representative'], 
        default= "None", 
        dest="jump_step",
        help='Jump the step and the previous ones. The steps in order are: Pre-Modeling, Modeling, Analysis & Clustering, virtual Hi-C calculation, most representative model')
group5.add_argument("--uZ",
        type=float, 
        action="store",
        dest="uZ", 
        help='Upper bound Z score (Only needed if jumping pre-modeling steps)')
group5.add_argument("--lZ", 
        type=float, 
        action="store",
        dest="lZ", 
        help='Lower bound Z score (Only needed if jumping pre-modeling steps)')
group5.add_argument("--max_distance","-max", 
        metavar="distance", 
        type=int, 
        action="store",
        dest="max_distance", 
        help='Maximum distance (Only needed if jumping pre-modeling steps)')
args = parser.parse_args()
number_of_cpus = args.number_of_cpus
pre_number_of_models = args.pre_number_of_models
total_number_of_models = args.number_of_models
from_dist = args.from_dist
to_dist = args.to_dist
dist_bins = args.dist_bins
from_zscore = args.from_zscore
to_zscore = args.to_zscore
zscore_bins = args.zscore_bins
verbose = args.verbose
data_dir = args.data_dir
working_dir = args.working_dir
prefix = args.prefix
fragments_in_each_bead = args.fragments_in_each_bead
k_mean = args.k_mean
jump_step = args.jump_step
step = jump_step
subset = args.subset
std_dev = args.std_dev
cut_off_percentage = args.cut_off_percentage
maximum_hic_value = args.maximum_hic_value
ignore_beads = args.ignore_beads
ignore_viewpoint_beads = args.ignore_viewpoint_beads
biggest_matrix = 0
repaint_vhic = args.repaint_vhic
colormap = args.colormap
jump_step = [1]*5
if step != "None":
    if step == "pre_modeling":
        jump_step[1] = 0
        jump_step[2] = 0
        jump_step[3] = 0
        jump_step[4] = 0
    else: 
        if step == "modeling":
            jump_step[2] = 0
            jump_step[3] = 0
            jump_step[4] = 0
        else: 
            if step == "analysis":
                jump_step[3] = 0
                jump_step[4] = 0
            else:
                if step == "vhic":
                    jump_step[4] = 0
else:
    jump_step = [0]*5
if data_dir[-1] != "/":
    data_dir = data_dir + "/"
if repaint_vhic:
    jump_step = [1]*5
try:
    if jump_step[0] :
        max_distance = args.max_distance
        uZ = args.uZ
        lZ = args.lZ
        if uZ == None or lZ == None or max_distance == None:
            raise Exception()
except:
    print "Since you are jumping the pre-modeling step, --max_distance, --uZ and --lZ flags are needed" 
    sys.exit()
# getting biggest_matrix
try:
    if jump_step[2] and (not jump_step[3] or not jump_step[4]):
        search_dir = "{}{}/{}_final_output_{}_{}_{}/".format(working_dir,prefix,prefix,uZ,lZ,max_distance)
        command =  "ls {} | egrep matrix[0-9]+".format(search_dir)
        matrix_files = subprocess.check_output(command,shell=True)
        aux = []
        for x in matrix_files:
            aux.append(x)
        aux = "".join(aux)
        matrix_files = aux.split("\n")[:-1]
        sizes = []
        for x in matrix_files:
            command = "wc {}".format(search_dir+x)
            matrix_sizes = subprocess.check_output(command,shell=True)
            aux = []
            for char in matrix_sizes:
                aux.append(char)
            aux = "".join(aux)
            sizes.append(int(aux.split()[0]))
        biggest_matrix = matrix_files[sizes.index(max(sizes))]
        biggest_matrix = int((re.findall(r'\d+',biggest_matrix))[0])
except:
    e = sys.exc_info()[1]
    print e
if verbose:
    def verboseprint(text):
        print text;
else:   
    verboseprint = lambda *a: None      # do-nothing function
# get the name and position from primers.txt
#primers.txt:  name chrN:position
primers = {}
viewpoint_positions = []
primers_file = fileCheck(data_dir+"primers.txt")
for line in primers_file:
    m = re.search('([^\s\t]+).*chr\w+:(\d+)', line)
    try:
        primers[m.group(1)] = int(m.group(2))
    except:
        break
print "\nPrimers.txt. These are the viewpoints that will be used in the modeling:"
for k,v in primers.iteritems():
    print "Viewpoint:{}\tposition:{}".format(k,v)
    viewpoint_positions.append(v)
print 
file_names = primers.keys()
files = [data_dir+f for f in file_names]
# read one of the files and get number of fragments and default fragments_in_each_bead
# a_4c_file: chrN start end value
start_frag = 0
end_frag = 0
number_of_fragments = 0
a_4c_file = fileCheck(data_dir+primers.keys()[0])
for line in a_4c_file:
    values = line.split()
    if len(values) != 4:
        continue
    if start_frag == 0:
        start_frag = int(values[1])
    end_frag = int(values[2])
    number_of_fragments += 1
locus_size = end_frag - start_frag
viewpoint_fragments = calculate_fragment_number(viewpoint_positions,files[0])
#default, we want 100 beads in each model
if fragments_in_each_bead == 0:
    fragments_in_each_bead = int(number_of_fragments / 100)
viewpoint_fragments = [int(i/fragments_in_each_bead) for i in viewpoint_fragments]
are_genes = viewpoint_fragments
# now get number of beads
number_of_fragments = int(number_of_fragments/fragments_in_each_bead)
#opening vhic primers
color_of_fragments = []
vhic_primers = {}
vhic_colors = {}
try:
    vhic_primers_file = open (data_dir+"primers_vhic.txt", 'r')
    for line in vhic_primers_file:
        m = re.search('([^\s\t]+).*chr\w+:(\d+)\s*(\w+)?', line)
        try:
            vhic_primers[m.group(1)] = int(m.group(2))
            if m.group(3) == None:
                vhic_colors[m.group(1)] = "yellow"
            else:
                vhic_colors[m.group(1)] = m.group(3)
        except:
            break
except IOError:
    print "\nError: File "+ data_dir+ " primers_vhic.txt does not appear to exist. Using primers.txt to paint positions in the virtual Hi-C\n"
    vhic_primers_file = fileCheck(data_dir+"primers.txt")
    for line in vhic_primers_file:
        m = re.search('([^\s\t]+).*chr\w+:(\d+)', line)
        try:
            vhic_primers[m.group(1)] = int(m.group(2))
            vhic_colors[m.group(1)] = "yellow"
        except:
            break
print "This positions will appear in the virtual Hi-C: "
show_fragments_in_vhic = []
show_fragments_in_vhic = vhic_primers.values()
name_of_fragments = vhic_primers.keys()
color_of_fragments = vhic_colors.values()
name_of_fragments = [x[:10] for x in name_of_fragments]
show_fragments_in_vhic = calculate_fragment_number(show_fragments_in_vhic,files[0])
show_fragments_in_vhic = [int(i/fragments_in_each_bead) for i in show_fragments_in_vhic]
counter = 0
for k,v in vhic_primers.iteritems():
    print "VHi-C name:{}\tposition:{}\tcolor:{}\tbead:{} ".format(k,v,vhic_colors[k],show_fragments_in_vhic[counter])
    counter += 1
print
p = Pool(number_of_cpus)
execute = []
########################################  Pipeline
######### pre-modeling 
if not jump_step[0]:
    print "Doing the pre-modeling..."
    print "Modeling with variable max_distance ranging {}:{}".format(from_dist,to_dist)
    for dist in range(from_dist,to_dist+dist_bins,dist_bins):
        instructions = (0.1 ,-0.1, dist,0 ,False)
        execute.append(instructions)
    p.map(modeling,execute)
    execute = []
    ######### max distance calculation
    print "Calculating optimal max_dist parameter for the modeling...\n"
    max_distance = calculate_best_maxd()
    print "maxD calculated: Optimal max_distance value is: {}".format(max_distance)
    print "Modeling with variables uZ and lZ ranging {}:{} and -{}:-{}".format(from_zscore,to_zscore,from_zscore,to_zscore)
    for zmax in np.arange(from_zscore,to_zscore+zscore_bins,zscore_bins):
        for zmin in np.arange(-from_zscore, -to_zscore-zscore_bins, -zscore_bins):
            instructions = (zmax, zmin, max_distance, 0 ,False)
            execute.append(instructions)
    p.map(modeling,execute)
    execute = []
    ######### z_scores calculation
    print "Now calculating best uz and lz"
    uZ, lZ = calculate_best_zscores()
    print "uZ and lZ calculated: Optimal values are {} and {}.".format(uZ,lZ)
    print "Pre-modeling finished"
pre_modeling_time = time.time() - start_time         
print "Pre-modeling took: {}".format(pre_modeling_time)
######### Modeling 	
if not jump_step[1]:
    print "Modeling started, modeling {} models...".format(total_number_of_models)
    number_of_models = total_number_of_models/number_of_cpus
    for cpu in range(number_of_cpus):
        instructions = ( uZ,lZ, max_distance, cpu*number_of_models ,True)
        execute.append(instructions)
    p.map(modeling,execute)
    execute = []
    print "Modeling finished"
modeling_time = time.time() - pre_modeling_time         
print "Modeling took: {}".format(modeling_time)
######### Analysis of models
############################################# anterior score files should be deleted
if not jump_step[2]:
    print "Analysis started"
    std_dev, cut_off_percentage, models_subset = run_analysis(std_dev,cut_off_percentage)
    print "Final analysis thresholds: "
    print "Std_dev: {}".format(std_dev)
    print "cut_off_percentage: {}".format(cut_off_percentage)
    ######### cluster models
    print "Running clustering..."
    n_clusters = 0
    n_clusters,biggest_matrix = run_clustering(models_subset)
    #if n_clusters != k_mean:
    #    print "Redoing the clustering expecting {} clusters.".format(n_clusters)
    #    n_clusters,biggest_matrix = run_clustering(models_subset)
    print "Clustering finished"
analysis_time = time.time() - modeling_time         
print "Analysis took: {}".format(analysis_time)
######### vhic calculation
if maximum_hic_value == 0: #set a default value
    maximum_hic_value = max_distance*0.8
if not jump_step[3]:
    print "Generating Virtual Hi-C"
    calculate_vhic(biggest_matrix,True)
    print "Virtual Hi-C generated"
if repaint_vhic and jump_step[3]: 
    print "RePainting Virtual Hi-C"
    calculate_vhic(biggest_matrix,False)
    print "Virtual Hi-C RePainted"
vhic_time = time.time() - analysis_time
print "Virtual Hi-C generation took: {}".format(vhic_time)
######### getting representative model
if not jump_step[4]:
    print "Calculating representative model..."
    calculate_representative_model(biggest_matrix)
representative_time = time.time() - vhic_time 
print "Representative modeling calculation took: {}".format(representative_time)
print """##################################################################################################################
\n What do you want to do now?:

 -If the virtual Hi-C is too red or white, rerun with --repaint_vhic, modify --maximum_hic_value and set --uZ, --lZ and --max_distance.

 -To paint a model with epigenetic marks (bam/bed file required):
    'python src/paint_model.py Representative_model.py data_dir bam/bed_file colormap'

 -To call the TAD boundaries, run:
    'python src/calculate_boundaries.py vhic'

#todo
 -To compare conserved regions between 2 virtual Hi-Cs (Different species or homolog regions), run:
    'python src/Evo_comp.py data_dir prefix VHiC distance data_dir2 prefix2 VHiC2 distance2'

#todo
 -To compare this virtual Hi-C to another one of the same region (Mutants), run:
    'python src/Mut_comp.py data_dir prefix VHiC distance prefix2 VHiC2 distance2'
\n##################################################################################################################
"""  
needed_time = time.time() - start_time
print "Total time spent: {}".format(needed_time)
