#!/usr/bin/python

#script that measures the distance between all the beads in each model, calculates the average distance between all models, and generates a heatmap of these distances, also called, virtual Hi-C.

import re
import os
import sys
import subprocess
from multiprocessing import Pool
from itertools import combinations, chain
import time
import ConfigParser
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def chimera_worker(chimera_file):
    distance_output = subprocess.check_output(["chimera", "--nogui", chimera_file])
    return distance_output


number_of_arguments = len(sys.argv)
if number_of_arguments != 4: #Or all parameters, or no parameters 
    print "Not enough parameters. Config file, matrix file path and calculate_the_matrix True/False are required. "
    print " -config_file: file with more data. Check config_template.ini for an example"
    print " -matrix file path: Path to one of the matrices (a cluster) calculated in the clustering. Located in the directory of the final models."
    print " -calculate_the_matrix: True if we want to (re)calculate the virtual Hi-C"


    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    ini_file = sys.argv[1]
    root = sys.argv[2]
    matrix_path = sys.argv[2]
    root = matrix_path.split("/")[0:-1]
    root = '/'.join(root)
    root = root+"/"
    if sys.argv[3] == "True":
        y_or_n = raw_input ("Are you sure you want to calculate the matrix again? (Y/N): ")
        if y_or_n == "Y" or y_or_n == "y": 
            calculate_the_matrix = True
        elif y_or_n == "N" or y_or_n == "n":
            calculate_the_matrix = False
        else: 
            print "Bad input."
            sys.exit()
    elif sys.argv[3] == "False":
        calculate_the_matrix = False
    else:
        print "Set True or False in calculate_the_matrix."
        sys.exit()
    
#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    
    prefix = config.get("ModelingValues", "prefix")
    fragments_in_each_bead = float(config.get("ModelingValues", "fragments_in_each_bead"))
    show_fragments_in_vhic = config.get("TADs", "show_fragments_in_vhic")
    show_fragments_in_vhic = re.sub('[\n\s\t]','',show_fragments_in_vhic)
    show_fragments_in_vhic = show_fragments_in_vhic.split(",")
    show_fragments_in_vhic = [ int(i) for i in show_fragments_in_vhic]
    show_fragments_in_vhic = [int(i/fragments_in_each_bead) for i in show_fragments_in_vhic]
    
    number_of_fragments = int(config.get("ModelingValues", "number_of_fragments"))
    number_of_fragments = int(number_of_fragments/fragments_in_each_bead)
    
    name_of_fragments = config.get("TADs", "name_of_fragments")
    name_of_fragments = re.sub('[\n\s\t]','',name_of_fragments)
    name_of_fragments = name_of_fragments.split(",")
    color = config.get("TADs", "color_of_fragments")
    color = re.sub('[\n\s\t]','',color)
    color = color.split(",")
    
    number_of_cpus = int(config.get("ModelingValues", "number_of_cpus"))
    maximum_hic_value= int(config.get("TADs", "maximum_hic_value"))



except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()
    print e
    sys.exit()
distance_file = "get_genome_distance_{}".format(prefix)
path = "{}vhic_{}.txt".format(root,prefix)
start_time = time.time()
if calculate_the_matrix:
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
        print "{} - {}".format(counter,model)
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

            
        print "Calculating in chimera..."       
        distance_output = p.map(chimera_worker,chimera_files)

        

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
        print "{} seconds needed.".format(time.time() - start_time)



    f= open(path, 'w') #store the data in file
    matrix_mean = np.zeros((number_of_fragments,number_of_fragments))
    for line in range(number_of_fragments):
        for column in range(number_of_fragments):
            mean_value = np.mean(matrix[line][column])
#         print "[{}][{}] = {}".format(line,column,mean_value)
            matrix_mean[line][column] = mean_value
#         matrix_mean[column][line] = mean_value
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
#matrix_mean = matrix_mean[15:-15,15:-15]
#show_fragments_in_vhic = [x-15 for x in show_fragments_in_vhic]
show_fragments_in_vhic = [c+0.5 for c in show_fragments_in_vhic] #to match the name_of_fragments in the matrix Since the ticks don't match with the heatmap.
fig = plt.figure()
plt.title("Virtual Hi-C")
ax = plt.subplot(1,1,1)
z = np.array(matrix_mean)



c = plt.pcolor(z,cmap=plt.cm.PuRd_r,vmax=maximum_hic_value, vmin=0)
ax.set_frame_on(False)
plt.colorbar()


#to set the show_fragments_in_vhic
#color = [10,5,5,10,10,10,10,10] -> depending on quantity of genes
plt.scatter(show_fragments_in_vhic, show_fragments_in_vhic, s=20, c=color,cmap=plt.cm.autumn)



ax.set_yticks(show_fragments_in_vhic)
ax.set_xticks(show_fragments_in_vhic)
ax.set_xticklabels(name_of_fragments, minor=False)
ax.set_yticklabels(name_of_fragments, minor=False)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)

plt.axis([0,z.shape[1],0,z.shape[0]])

fig.set_facecolor('white')
#plt.show()

pp = PdfPages('{}{}_vHiC.pdf'.format(root,prefix))
pp.savefig(fig)
pp.close()
print '\nVirtual HiC.pdf written in {}{}_HiC.pdf'.format(root,prefix)
#Distance between #1 marker 1  and #10 marker 1 : 2203.213
print """\nWhat do you want to do now?:

-If the virtual Hi-C is too red or white, modify the maximum_hic_value in the config file and run:
    'python {} {} {} False'

-To get the representative model and superposition of best models:
    'python src/get_representative_model.py {} {}'

-To paint a model with epigenetic marks (bam/bed file required):
    'python src/paint_model.py {} your_model.py '

-To call the TAD boundaries, run:
    'python src/calculate_boundaries.py {} tad_size'

-To compare this virtual Hi-C to another one, run:
    'python src/Evocomp.py {} config_file2 {} vhic2'
    
-To compare this virtual Hi-C to another one, run:
    'python src/mutcomp'
    
    
    """.format(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[1],sys.argv[2],sys.argv[1],path,sys.argv[1],path)        
