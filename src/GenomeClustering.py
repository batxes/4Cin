#!/usr/bin/python
import sys
import operator
import re
import subprocess
from os import listdir, remove
from os.path import isfile, join
import numpy as np
from itertools import combinations,izip
import ConfigParser
import scipy.cluster.hierarchy as sch
import matplotlib
matplotlib.use('agg')
import pylab
from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq
from multiprocessing import Process, Lock, Pool, current_process


def chimera_worker(chimera_file):
    distance_output = subprocess.check_output(["chimera", "--nogui", chimera_file[0]])
    return distance_output,chimera_file[1],chimera_file[2],current_process().name

number_of_arguments = len(sys.argv)
if number_of_arguments != 4: #Or all parameters, or no parameters 
    print "Not enought parameters. Config file, subset and K value are missing."
    print " -config_file: file with more data. Check config_template.ini for an example"
    print " -subset: number of best models gathered in the analysis"
    print " -K value: number of cluster you expect to have. Value 2 is recommended."
    sys.exit()
if len(sys.argv) > 3:  #if we pass the arguments (in the cluster)
    ini_file = sys.argv[1]
    subset = int(sys.argv[2])
    k_mean = int(sys.argv[3])

#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    working_dir = config.get("ModelingValues", "working_dir")
    
    prefix = config.get("ModelingValues", "prefix")
    fragments_in_each_bead = float(config.get("ModelingValues", "fragments_in_each_bead"))
    min_z = float(config.get("ModelingValues", "min_zscore"))
    max_z = float(config.get("ModelingValues", "max_zscore"))
    max_dist = int(config.get("ModelingValues", "max_dist"))
    root = "{}data/{}/{}_final_output_{}_{}_{}/".format(working_dir,prefix,prefix,max_z,min_z,max_dist)
    number_of_fragments = int(config.get("ModelingValues", "number_of_fragments"))
    number_of_fragments = int(number_of_fragments/fragments_in_each_bead)

    number_of_cpu = int(config.get("ModelingValues", "number_of_cpus"))
    
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()

matrix = np.zeros((subset,subset))

only_python_files = []

for pyfile in listdir(root):
    if pyfile.endswith(".py"):
        only_python_files.append(pyfile)
only_python_files = only_python_files[:subset]
print len(only_python_files)

# generate a chimera file with match. Chimera when matched, it calculates the RMSD 
number_of_fragments = number_of_fragments -1

# combi = combinations(range(len(only_python_files)),2)
combi = combinations(range(subset),2)
p = Pool(number_of_cpu)
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
    rmsd_file.write("rc(\"match #{}-{} #{}-{}\")\n".format((number_of_fragments+1),(number_of_fragments+1)+number_of_fragments ,0,number_of_fragments))
    rmsd_file.close()
    instruction_files.append(chimera_file)
    instruction_files.append(counter_line)
    instruction_files.append(counter_column)
    instructions.append(instruction_files)
print "Populating matrix.txt ..."
for core in range(0,number_of_files,number_of_cpu):
    if len(instructions) - core < number_of_cpu:
        execute = instructions[core:len(instructions)-core]
    else:
        execute = instructions[core:core+number_of_cpu] 
    # WE NEED TO EXECUTE THIS DEPENDING ON CPU SIZE
    rmsd_output = p.map(chimera_worker,execute)
    #print rmsd_output
    for i in range(len(execute)):
        #print "Writing [{}][{}]".format(rmsd_output[i][1],rmsd_output[i][2])
        string = ""
        lista = []
        for line2 in rmsd_output[i][0]:
            string = string + line2
            if line2 == "\n":
                lista.append(string)
                string = ""
        #RMSD between 103 atom pairs is 4404.816 angstroms
        for line2 in lista:
            exp = re.search(r"(\d+\.\d+) angstroms",line2)
            if (exp):
                value = exp.group(1)
                matrix[rmsd_output[i][1]][rmsd_output[i][2]] = value
                matrix[rmsd_output[i][2]][rmsd_output[i][1]] = value    
                value = 0
    #delete files while we execute them
    for i in range(len(execute)):
        remove(execute[i][0])
        remove(execute[i][0]+"c")
    if core!= 0:
        sys.stdout.write("\r{}%".format( core*100/number_of_files))
        sys.stdout.flush()


      
      
#write matrix       
matrixtxt = open("{}matrix_parallel.txt".format(root), "w")      
matrixtxt.write("\t")
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
print "\n\nmatrix_parallel.txt written! in {}".format(root)
print "\nThis is the whole RMSD matrix (all models vs all models)"
#matrix2 = np.zeros((subset,subset))

#models = []
#line_ = 0
#with open ("{}matrix.txt".format(root), "r") as f:
#    for line in f:
#        if line_ == 0:
#            models = line.split("\t")
#            models = models[1:-1]
#            line_ += 1
#        else:
#            column_ = 0
#            values = line.split("\t")
#            values = values[1:-1]
#            for value in values:
#                matrix2[line_-1][column_] = value
#                column_ += 1
#            line_ += 1


D = matrix

# Compute and plot first dendrogram.
fig = pylab.figure(figsize=(8,8))

ax1 = fig.add_axes([0.09,0.1,0.2,0.6])
Y = sch.linkage(D, method='average')
Z1 = sch.dendrogram(Y, orientation='right')
ax1.set_xticks([])
ax1.set_yticks([])

# # Compute and plot second dendrogram.
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
im = axmatrix.matshow(D, aspect='auto', origin='lower', cmap=pylab.cm.YlGnBu)
axmatrix.set_xticks([])
axmatrix.set_yticks([])

# Plot colorbar.
axcolor = fig.add_axes([0.91,0.1,0.02,0.6])
pylab.colorbar(im, cax=axcolor)
#fig.show()
try:
    fig.savefig('{}{}_heatmap.png'.format(root,prefix))
except:
    pass

# Code to retrieve the clusters
n = subset
cluster_number = []
cluster_dict = dict()
for i in range(subset-2):
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
for i in cluster_dict:
    cluster_number.append(i)

if not(len(cluster_number) == k_mean):
    print "There is a different number of cluster than set in K. Exiting..."
    sys.exit()
        
number_of_fragments = number_of_fragments +1 
# Write the matrix data in different files, k_mean times
for i in cluster_number:
    matrixtxt = open("{}matrix{}.txt".format(root,i), "w")      
    matrixtxt.write("\t")
    cluster_values = [int(j) for j in cluster_dict[i]]
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
        
        
    # create the file to open in chimera
    # superposition of the best models
    print "\nCreating superposition of this cluster...\n"
    with open(working_dir+"data/"+prefix+"/"+prefix+"_superposition_"+str(i)+".py","w") as f:
        f.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\""+root+"\")\n")
        f.write("rc(\"open {}\")\n".format(cluster_models[0]))
        for k in range(1,len(cluster_models)):
            imodel = cluster_models[k]
            f.write("rc(\"open {}\")\n".format(imodel))
            f.write("rc(\"match #{}-{} #0-{}\")\n".format(k*number_of_fragments,k*number_of_fragments+number_of_fragments-1,number_of_fragments-1))

    print "created in {}data/{}/{}_superposition".format(working_dir,prefix,prefix)
    print "\n"

