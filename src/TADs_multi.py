#!/usr/bin/python

## CREATE THE CMD TO USE IN CHIMERA
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

calculate_the_matrix = True #to get only the HIC from the text use TADS_generate_matrix

number_of_arguments = len(sys.argv)
if number_of_arguments != 5: #Or all parameters, or no parameters 
    print "Not enought parameters. Config file, directory with data, matrix file and calculate_the_matrix True/False are required. You passed: ",sys.argv[1:]
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    ini_file = sys.argv[1]
    root = sys.argv[2]
    matrix_path = root + sys.argv[3]
    if sys.argv[4] == "True":
        calculate_the_matrix = True
    elif sys.argv[4] == "False":
        calculate_the_matrix = False
    else:
        print "Set True or False in calculate_the_matrix."
        sys.exot()
    
#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    
    prefix = config.get("ModelingValues", "prefix")
    verbose = int(config.get("ModelingValues", "verbose"))
    WINDOW = float(config.get("ModelingValues", "WINDOW"))
    
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
    
    number_of_models = int(config.get("ModelingValues", "number_of_models"))
    
    gene_names = config.get("TADs", "gene_names")
    gene_names = re.sub('[\n\s\t]','',gene_names)
    gene_names = gene_names.split(",")
    
    number_of_cpu = int(config.get("TADs", "number_of_cpu"))
    maximum_hic_value= int(config.get("TADs", "maximum_hic_value"))

except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()
distance_file = "get_genome_distance_{}".format(prefix)
path = "{}distances_of_current_model_{}".format(root,prefix)
start_time = time.time()
if calculate_the_matrix:
      
    viewpoints = [c+0.5 for c in viewpoints] #to match the gene_names in the matrix Since the ticks don't match with the heatmap.
    #root = "/home/bioinfo/workspace/4c2vhic/{}_final_output_0.7_-0.3_8000/".format(prefix)
#     root = "/home/bioinfo/workspace/genome/{}_output_0.2_-0.2_7000_without_2_and_3_4_6_7_8/".format(prefix)
    models = []
        # matrix = np.zeros((number_of_spheres,number_of_spheres,number_of_spheres))
        ## we get a file that (cmd) that we are gonna use it in chimera. It will write all distances in the model
    with open("{}".format(matrix_path), "r") as mtx:
        for line in mtx:
            models = re.split("\t", line)
            print models
            break

    
    models = models[1:-1]
    print models
    
    
#     models = models[50:51] #testing
    
    
    counter = 0
    matrix = np.zeros((NFRAGMENTS,NFRAGMENTS,len(models)))
    
    p = Pool(number_of_cpu)
    print number_of_cpu


    for model in models:
        print "{} - {}".format(counter,model)
        chimera_files = []
        combi = combinations(range(0,NFRAGMENTS),2)
        instruction_list = []
        for pair in combi:
            instruction_list.append("rc(\"distance #"+str(pair[0])+" #"+str(pair[1])+"\")\n")
#         print len(instruction_list)
        for cpu in range(number_of_cpu):
            instru_start = (cpu) * (len(instruction_list)/number_of_cpu) 
            if cpu == number_of_cpu-1:
                instru_end =  len(instruction_list)
            else:
                instru_end =  (cpu+1) * (len(instruction_list)/number_of_cpu) 
                
            dis_file = distance_file+"cpu"+str(cpu)+".py"
            with open (dis_file,'w') as output:
                output.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"{}\")\n".format(root))
                output.write("rc(\"open {}\")\n".format(model))
#                 print root
#                 print model  
#                 print instru_start, instru_end
                for instru in instruction_list[instru_start:instru_end]:
#                     print instru
                    output.write(instru)
                chimera_files.append(dis_file)

            
        if verbose==3:  print "Calculating in chimera..."       
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
        print "{} segundos".format(time.time() - start_time)



    f= open(path, 'w') #store the data in file
    matrix_mean = np.zeros((NFRAGMENTS,NFRAGMENTS))
    for line in range(NFRAGMENTS):
        for column in range(NFRAGMENTS):
            mean_value = np.mean(matrix[line][column])
#         print "[{}][{}] = {}".format(line,column,mean_value)
            matrix_mean[line][column] = mean_value
#         matrix_mean[column][line] = mean_value
            f.write(str(line)+","+str(column)+","+str(mean_value))   
            f.write("\n")
    f.close()
    for chi_file in chimera_files:
        os.remove(chi_file)
        os.remove(chi_file+"c")
else:
    with open(path, 'r') as std_in:
        matrix_mean = np.zeros((NFRAGMENTS,NFRAGMENTS))
        for line in std_in:
            values = line.split(",")
            matrix_mean[int(values[0])][int(values[1])] = float(values[2])


if verbose==3:  print "Generating matrix to plot..."     
fig = plt.figure()
ax = plt.subplot(1,1,1)
z = np.array(matrix_mean)



c = plt.pcolor(z,cmap=plt.cm.PuRd_r,vmax=maximum_hic_value, vmin=0)
ax.set_frame_on(False)
plt.colorbar()


#to set the viewpoints
# color = [10,5,5,10,10,10,10,10] -> depending on quantity of genes
# plt.scatter(genes, genes, s=10, c=color,cmap=plt.cm.autumn)


ax.set_yticks(viewpoints)
ax.set_xticks(viewpoints)
ax.set_xticklabels(gene_names, minor=False)
ax.set_yticklabels(gene_names, minor=False)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)

plt.axis([0,z.shape[1],0,z.shape[0]])

fig.set_facecolor('white')
#plt.show()

pp = PdfPages('{}{}_HiC.pdf'.format(root,prefix))
pp.savefig(fig)
pp.close()
print '{}_HiC.pdf writen'.format(prefix)
print "{} segundos".format(time.time() - start_time)
#Distance between #1 marker 1  and #10 marker 1 : 2203.213
            
