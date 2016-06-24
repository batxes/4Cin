#!/usr/bin/python

import sys
import time
import os
import re
from math import fabs
from random import randint
import IMP.kernel
import IMP.algebra
import IMP.core
import IMP.display
import IMP.base
import IMP.atom
import IMP.rmf
import IMP.container
import RMF
import numpy as np
import ConfigParser
from normal_distribution import fileCheck, sizeReader,  calculateNWindowedDistances

drome = False

number_of_arguments = len(sys.argv)
if number_of_arguments != 7:  
    print "Not enought parameters. uZ, lZ, maxDis, starting_point, config_file and is_big_sampling are required. You passed: ",sys.argv[1:]
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    uZ = float(sys.argv[1])
    lZ = float(sys.argv[2])
    y2 = int(sys.argv[3])
    starting_point = int(sys.argv[4])
    ini_file = sys.argv[5]
    big_sampling = sys.argv[6] #finalmodels or premodeling

#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    prefix = config.get("ModelingValues", "prefix")
    working_dir = config.get("ModelingValues", "working_dir")
    verbose = int(config.get("ModelingValues", "verbose"))
    WINDOW = float(config.get("ModelingValues", "WINDOW"))
    files = config.get("ModelingValues", "files")
    files = re.sub('[\n\s\t]','',files)
    files = files.split(",")    
    viewpoints = config.get("ModelingValues", "viewpoints")
    viewpoints = re.sub('[\n\s\t]','',viewpoints)
    viewpoints = viewpoints.split(",")
    viewpoints = [ int(i) for i in viewpoints]
    viewpoints = [int(i/WINDOW) for i in viewpoints]
    genes = config.get("ModelingValues", "genes")
    genes = re.sub('[\n\s\t]','',genes)
    genes = genes.split(",")
    genes = [ int(i) for i in genes]
    genes = [int(i/WINDOW) for i in genes]
    NFRAGMENTS = int(config.get("ModelingValues", "NFRAGMENTS"))
    NFRAGMENTS = int(NFRAGMENTS/WINDOW)
    ignore_beads = config.get("ModelingValues", "ignore_beads")
    if ignore_beads != "NO":
        ignore_beads = re.sub('[\n\s\t]','',ignore_beads)
        ignore_beads = ignore_beads.split(",")
        ignore_beads = [ int(i) for i in ignore_beads]
    else:
        ignore_beads = [] #empty
    if big_sampling == "True":
        number_of_models = int(config.get("ModelingValues", "number_of_models"))
    elif big_sampling == "False":
        number_of_models = int(config.get("Pre-ModelingValues", "number_of_models"))
    else:
        print "is_big_sampling variable has to be True or False. Exiting..."
        sys.exit()
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()


###################################### ###################################### 
###################################### ###################################### 
###################################### CHANGE DEPENDING ON MODELING VARIABLES




rmf_video = False #If we wanna create a video of the IMP optimization
evaluation = False #If we wanna evaluate the restraints 
RESTRAINTS = [True,False,True,False] #4c counts, EV, HUB(connectivity), HLB(connectivity)
RESTRAINTS_QUANTITY = [0,0,0,0]
radius = 0

k = 1
if evaluation:
    std_dev = y2*0.2 #300 A #for evaluation #set a percentage of max distance. 20%
#         std_dev = 1 #A 
if rmf_video:
    frames = 5000
    
#optimization variables
LSTEPS = 5
STEPS = 1
NROUNDS= 10000 #10000 default

endLoopCount = 0
stopCount = 15
endLoopValue = 0.00001
hightemp = int (0.025 * NROUNDS )
alpha = 1.0 * NFRAGMENTS #the weight of the fragments




storage_folder = working_dir+"data/"+prefix+"/"+prefix+"_output_"+str(uZ)+"_"+str(lZ)+"_"+str(y2) #the dir where the data will be saved
sampling = True
score_file = storage_folder+"/score"+str(starting_point)+".txt"
if os.path.exists(score_file): os.remove(score_file) 

exv_values = []
hub_values = []
                                                                    # ZebraFish_output_1.0_-1.0_7000
if not os.path.exists(storage_folder): os.makedirs(storage_folder)

#radius_scale = 0.1 
#radius_scale = 0.021695  #0.01 nm bp occupancy more or less.  #my value 0.04339. Davide = 0.005  #THIS ONE IS BAD

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

###################################### ###################################### 
###################################### ###################################### 
###################################### THE REAL DEAL!
start_time = time.time()
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
    if (verbose == 3):
        print "Generating ", chimera_file, "..."
    values_file = prefix+str(sample)+".txt"
    w = IMP.display.ChimeraWriter(storage_folder+"/"+chimera_file)
    m = IMP.Model()
    
    if rmf_video:
        hierarqy= IMP.atom.Hierarchy.setup_particle(IMP.Particle(m))
    
    
    ##########################    REPRESENTATION ##########################    REPRESENTATION
    ##########################    REPRESENTATION ##########################    REPRESENTATION
    
    for i in range(NFRAGMENTS):
        
            # Create "untyped" Particles
            p = IMP.kernel.Particle(m,"particle_"+str(i))
            
            
            radius_sum = 0
            for j in range(int(WINDOW)):
                radius_sum = radius_sum + reads_size[(i*int(WINDOW))+j]
            if drome:
                radius_sum = 10000
            radius = radius_scale * radius_sum #sphere radius proportional to fragments
            fragment_bp_quantity.append(radius_sum)
            if (verbose == 3):
                print "Fragment number: "+str(i)+" size: "+str(radius_sum)+" radius: "+str(radius)
            #decorator with sphere  
            #Creating very far away particles (10000) could alter the final result of the beads that are not restrained
            d = IMP.core.XYZR.setup_particle(p, IMP.algebra.Sphere3D(IMP.algebra.Vector3D(randint(0,int(y2)), randint(0,int(y2)), randint(0,int(y2))), radius)) 
            bead_radii.append(radius)
            if i in(viewpoints):
                if i in(genes):
                    color = IMP.display.Color(1,0.7,0)
                else: 
                    color = IMP.display.Color(0,1,0)
                IMP.display.Colored.setup_particle(p, color)
            else:
                
#               #one theme of color #blue, purple, red
                #color = IMP.display.Color(1/float(NFRAGMENTS)*i,0.0,1-1/float(NFRAGMENTS)*i) 
                
                
                #another them (only grey)
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
    ##########################  RESTRAINTS ##########################  RESTRAINTS
    
    #Distances
    #Excluded volume
    #Connectivity (HUB and HLB)
    #------------------
    
    r_count = 0
    reads_values,reads_weights,start_windows, end_windows = calculateNWindowedDistances(int(WINDOW),uZ,lZ, y2,files)
    
    for j in range(len(files)):
        reads_weight = reads_weights[j]
        reads_value = reads_values[j]

        #get the number of reads and their size from our files
        f = fileCheck(files[j])
        reads_size = sizeReader(f)
        n_fragments = len(reads_size)/int(WINDOW)  
        print n_fragments
        print "HOLAAAAAAAA"
        
# # # # # # # # # # # # # # # # # # # # # # # # #harmonic restraints got from file
        counter = 0
        if (RESTRAINTS[0]):
            p1 = genome[viewpoints[j]]
            for i in range(n_fragments):
                counter += 1
                if i != viewpoints[j]:
                    if reads_value[i] != 0: #aplying the Z Score lower bound and upper bound (see calculate10WindowedDistances)
                        if i not in ignore_beads:

                            p2 = genome[i]
                            
                            #We add the diameters of the beads to the distance
                            # the real distance is not from the core, we need to add the diameter, all the dna sequence
#                         distance = bead_radii[j] + bead_radii[i] + float(reads_value[i])
                            
                            
                            distance = float(reads_value[i])
                            if distance != float(y2):
#                             if True:
                                #if distance < y2: #if maximum distance is reached, don't set a restraint, because it can be further in genomic distance
                                kk2 = fabs(reads_weight[i])
                                #if it is not in the window of the 4C interactome
                                if (start_windows[j] > counter or end_windows[j] < counter):
                                    f = IMP.core.HarmonicLowerBound(distance, k*kk2)#don't give very good score?
                                    #f = IMP.core.Harmonic(distance, k*kk2)
                                    #harmonicLoweBound of max distance, so that they can not enter in a diameter of MAXDIS
                                else:     
                                    f = IMP.core.Harmonic(distance, k*kk2) #)  #this is the harmonic score. I think second parameter is weight. it was 1.0 until now                  
            #                     f = IMP.core.Harmonic(float(reads_value[i]), k*fabs(reads_weight[i])) #)  #this is the harmonic score. I think second parameter is weight. it was 1.0 until now
                                s = IMP.core.DistancePairScore(f)
                                r = IMP.core.PairRestraint(s, (p1, p2))  #this is the restraint
                                restraints.append(r)
                                m.add_restraint(r)
                                r_count += 1
              
    n_restraints.append(r_count)  
    RESTRAINTS_QUANTITY[0] = r_count 
# # # # # # # # # # # # # # # # # # # # # # # # # excluded volume
    if (RESTRAINTS[1]):
        mode = 1
        if mode == 1:
            r = IMP.core.ExcludedVolumeRestraint(genome,k) #we can remove k and 1 (genome,k,1) 
            restraints.append(r)
            m.add_restraint(r)
              
        
        if mode == 2:
            # this container lists all pairs that are close at the time of evaluation
            nbl= IMP.container.ClosePairContainer(genome, 0,2)
            h= IMP.core.HarmonicLowerBound(300,1)
            sd= IMP.core.DistancePairScore(h)
            #sd= IMP.core.SphereDistancePairScore(h)
            # use the lower bound on the inter-sphere distance to push the spheres apart
            nbr= IMP.container.PairsRestraint(sd, nbl)
            m.add_restraint(nbr)
        RESTRAINTS_QUANTITY[1] = 1 
# # # # # # # # # # # # # # # # # # # # # # # # # String of beads upper bound
    if (RESTRAINTS[2]):
        # using a HarmonicDistancePairScore for fixed length links is more
        # efficient than using a HarmonicSphereDistnacePairScore and works
        # better with the optimizer
        res_count = 0
        for i in range(len(genome)-1): 
                #### Different std_dev
            kk = 1    
            hub = IMP.core.HarmonicUpperBound(bead_radii[i]+bead_radii[i+1],k*kk) #como conseguir esto bien? 4 653 000
            p1 = genome[i]
            p2 = genome[i+1]
        #                 f = IMP.core.Harmonic(float(reads_value[i]), k * np.sqrt(reads_value[i]))  #this is the harmonic score. I think second parameter is weight. it was 1.0 until now
            s = IMP.core.DistancePairScore(hub)
            r = IMP.core.PairRestraint(s, (p1, p2))  #this is the restraint
            restraints.append(r)
            m.add_restraint(r)
            res_count += 1
        RESTRAINTS_QUANTITY[2] = res_count
    

# # # # # # # # # # # # # # # # # # # # # # # # # String of beads lower bound 
    if (RESTRAINTS[3]): 
        res_count = 0 
        hlb = IMP.core.HarmonicLowerBound(300,k)
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
    ##########################  SAMPLING ##########################  SAMPLING
    ##########################  SAMPLING ##########################  SAMPLING
        RESTRAINTS_QUANTITY[3] = res_count
    
    cg = IMP.core.ConjugateGradients(m) 
    mc = IMP.core.MonteCarloWithLocalOptimization(cg, LSTEPS) 
    mc.set_return_best(True) 
    mc.set_name("MC")
    sm = IMP.core.SerialMover(movers)
    mc.add_mover(sm)
     
    # sf = IMP.core.RestraintsScoringFunction(restraints, "RSF")
    # mc.set_scoring_function(sf) #monte carlo
    # cg.set_scoring_function(sf)     
    
    ######################RMF VIDEO, INSTALL RMF AGAIN!! ######################    
    if rmf_video:
     
    #create the RMF file to show the movie
        rmf= RMF.create_rmf_file('genome.rmf')
        rmf.set_description("Simulate genome.\n")
         
        bd = IMP.atom.BrownianDynamics(m)
        bd.set_log_level(IMP.base.SILENT)
#         bd.set_scoring_function(sf)

        bd.set_maximum_time_step(100)
         
        IMP.rmf.add_hierarchy(rmf, hierarqy)
        IMP.rmf.add_restraints(rmf, restraints)

        os= IMP.rmf.SaveOptimizerState(m,rmf)

        os.update_always("initial conformation")
        os.set_log_level(IMP.base.SILENT)
        os.set_simulator(bd)
        bd.add_optimizer_state(os)
        print "Optimizing twith Brownian Dynamics for the RMF file (movie)."
        bd.optimize(frames)
    
    #if I want no log
    IMP.base.set_log_level(IMP.base.SILENT)
    
    if (verbose == 3):
        #print "Number of restraints: %i" % (m.get_number_of_restraints()) #deprectad in last IMP 2.5.1
        print "Number of restraints: %i" % (len(restraints))
    
    #first score
    scores.append(m.evaluate(False))
    if (verbose == 3):
        print "Start score: ",scores[-1]
        print "\nStarts the optimization... "

    #First hightemp iterations, do not stop the optimization
    if (verbose == 3):
        print "High temp iterations"
    for i in range(0,hightemp):
        temperature = alpha * (1.1 * NROUNDS - i) / NROUNDS
        mc.set_kt(temperature)
        scores.append(mc.optimize(STEPS))
        if (verbose == 3):
            print i, scores[-1], "temp: ",mc.get_kt()
    
    needed_time = time.time() - start_time
    lownrj = scores[-1]

    if (verbose == 3):
        print "Time for High temp iterations" , needed_time
        print "Low temp iterations"
    for i in range(hightemp,NROUNDS): 
        temperature = alpha * (1.1 * NROUNDS - i) / NROUNDS
        mc.set_kt(temperature)
        scores.append(mc.optimize(STEPS))
        if (verbose == 3):
            print i, scores[-1], "temp: ",mc.get_kt()
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
#         print RESTRAINTS_QUANTITY[0], "distance restraints: ",suma1
    if RESTRAINTS[1]:
        suma2 = restraints[RESTRAINTS_QUANTITY[0]].evaluate(False)
#         print 1, " excluded Volume restraint: ",suma2
    if RESTRAINTS[2]:    
        n = RESTRAINTS_QUANTITY[0]+RESTRAINTS_QUANTITY[1]
        n2 = RESTRAINTS_QUANTITY[0]+RESTRAINTS_QUANTITY[1]+RESTRAINTS_QUANTITY[2]
        for r in restraints[n:n2]:
            suma3 = suma3 + r.evaluate(False)
#         print n2-n, " connectivity HUB restraints: ",suma3
    if RESTRAINTS[3]:  
        n = RESTRAINTS_QUANTITY[0]+RESTRAINTS_QUANTITY[1]+RESTRAINTS_QUANTITY[2]
        n2 = RESTRAINTS_QUANTITY[0]+RESTRAINTS_QUANTITY[1]+RESTRAINTS_QUANTITY[2]+RESTRAINTS_QUANTITY[3]
        for r in restraints[n:n2]:
            suma4 = suma4 + r.evaluate(False)
#         print n-n2, " connectivity HLB restraints: ",suma4
    if (verbose == 3):
        print "Total: ",suma1+suma2+suma3+suma4
        print "------------------------\n"
        #print "Number of restraints: %i" % (m.get_number_of_restraints()) #deprectad in last IMP 2.5.1
        print "Number of restraints: %i" % (len(restraints))
#     if cg.set_stop_on_good_score(True):
#         print "\n\ntermino con: "+str(i)
#         break;
#     if scoring_function.get_had_good_score():
#         configuration_set.save()
#     return configuration_set
    
    
    # print "\n\n############"
    # for r in restraints:
    #     print r.get_name(), r.evaluate(False)
    if (verbose == 3):
        needed_time = time.time() - start_time
        print "Time for Low temp iterations" , needed_time
    
    
        print "\nFINISH"
    if (sampling):
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
                if j != viewpoints[i]:
                    # the distance is to the surface, not to the center, so add radius*2
                    real_d = IMP.core.get_distance(spheres[j],spheres[viewpoints[i]]) 
    #                 real_d = real_d + radius*2
                    real_d = real_d + bead_radii[j] + bead_radii[viewpoints[i]]
                    
                    should_be_d = values[j] #take out the Z score near 0 average values
                    if should_be_d != 0:
                        total_restraints += 1

                        should_be_d = values[j] + bead_radii[j] + bead_radii[viewpoints[i]]
                        if (should_be_d + std_dev < real_d  or should_be_d - std_dev > real_d):
                            not_fulfilled += 1
                #             print "restraint "+str(j)+"not fulfilled"
#                                 if (verbose == 3):
#                                     print "Restraint " +str(j)+"-"+str(viewpoints[i])+" is "+str(real_d)+" and should be "+str(should_be_d)+" +- "+str(std_dev)+". Difference: "+str(should_be_d-real_d)
        if (verbose == 3):
            print "total: "+str(total_restraints)
            print "Not fulfilled restraints: "+str(not_fulfilled)+"/"+str(n_restraints[0]),"%",str(not_fulfilled*100/n_restraints[0])


    # GENERATE THE TXT FILE WITH THE DATA
    f = open (storage_folder+"/"+values_file,"w")  
    for i in range(len(files)):
        for j in range(n_fragments):
            if j != viewpoints[i]:
                real_d = IMP.core.get_distance(spheres[j],spheres[viewpoints[i]]) 
                real_d = real_d + bead_radii[j] + bead_radii[viewpoints[i]]
                f.write(str(real_d)+"\t")
            else:
                f.write("0\t")
        f.write("\n")  
    f.close()
    
    for sphere in genome:
        g = IMP.core.XYZRGeometry(sphere)
        w.add_geometry(g)

    print "\nModel number {}".format(sample)
    print "Human Score: ",scores[-1]/1000000
    exv_value = suma2/1000000
    exv_values.append(exv_value)
    if (verbose == 3):
        print "EXV: ", exv_value
    
    hub_value = suma3/1000000
    hub_values.append(hub_value)
    if (verbose == 3):
        print "HUB: ", hub_value
        needed_time = time.time() - start_time         
        print str(needed_time)+" seconds!"       

print "Mean exv for distance "+str(y2)+" is: "+str(np.mean(exv_values))  
print "Mean hub for distance "+str(y2)+" is: "+str(np.mean(hub_values))  

