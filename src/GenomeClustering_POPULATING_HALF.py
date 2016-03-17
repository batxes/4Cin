#   # \example core/simple.py
# Illustration of simple usage of the IMP library from Python.

#   ##################################### ###################################### 
###################################### ###################################### 
############ Libraries
import sys
import operator
import re
import subprocess
from os import listdir, remove
from os.path import isfile, join
import numpy as np
from itertools import combinations
import ConfigParser
import pylab
import scipy.cluster.hierarchy as sch


from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq


test = False

ini_file = "config.ini"
k_mean = 2

#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    
    prefix = config.get("ModelingValues", "prefix")
    WINDOW = float(config.get("ModelingValues", "WINDOW"))
    NFRAGMENTS = int(config.get("ModelingValues", "NFRAGMENTS"))
    NFRAGMENTS = int(NFRAGMENTS/WINDOW)

    subset = int(config.get("AnalysisValues", "subset"))
    
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()


###################################### ###################################### 
###################################### ###################################### 
###################################### CHANGE DEPENDING ON MODELING VARIABLES
#root = "/home/bioinfo/workspace/genome/"+prefix+"_output_0.2_-0.2_7000_without_2_and_3_4_6_7_8/"
root = "/home/bioinfo/workspace/genome/data/"+prefix+"_final_output_0.2_-0.2_7000/"
root = "/home/bioinfo/workspace/4c2vhic/IrxB_final_output_0.7_-0.3_8000/"
# root = "/home/bioinfo/workspace/genome/data/"+prefix+"_output_0.2_-0.2_7000.0/"

subset = 200
matrix = np.zeros((subset,subset))

only_python_files = []

for pyfile in listdir(root):
    if pyfile.endswith(".py"):
        only_python_files.append(pyfile)
print only_python_files
only_python_files = only_python_files[:subset]
print only_python_files
print len(only_python_files)

# generate a chimera file with match. Chimera when matched, it calculates the RMSD 
NFRAGMENTS = NFRAGMENTS -1

# combi = combinations(range(len(only_python_files)),2)
combi = combinations(range(subset),2)
if not test:
    for pair in combi:
    
        counter_line = pair[0]
        counter_column = pair[1]
    #     matrix.write(line)
    #     matrix.write("\t")
    
            
        print "line: {}, column {}".format(counter_line,counter_column)
        rmsd_file = open ("../{}_calculate_rmsd{}.py".format(prefix,counter_column), "w")
        rmsd_file.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"{}\")\n".format(root))
        rmsd_file.write("rc(\"open {}\")\n".format(only_python_files[counter_line]))
        rmsd_file.write("rc(\"open {}\")\n".format(only_python_files[counter_column]))
        rmsd_file.write("rc(\"match #{}-{} #{}-{}\")\n".format((NFRAGMENTS+1),(NFRAGMENTS+1)+NFRAGMENTS ,0,NFRAGMENTS))
        
        rmsd_file.close()
        #         output = os.system("chimera --nogui ../{}_calculate_rmsd.py".format(prefix))
        rmsd_output = subprocess.check_output(["chimera", "--nogui", "../{}_calculate_rmsd{}.py".format(prefix,counter_column)])
        remove("../{}_calculate_rmsd{}.py".format(prefix,counter_column)) 
        string = ""
        lista = []
        for line2 in rmsd_output:
            string = string + line2
            if line2 == "\n":
                lista.append(string)
                string = ""
             
        #RMSD between 103 atom pairs is 4404.816 angstroms
        print lista
        for line2 in lista:
    
            exp = re.search(r"(\d+\.\d+) angstroms",line2)
            if (exp):
                print exp,
                
                value = exp.group(1)
                print value
    
#                if matrix[counter_line][counter_column] == 0:
                matrix[counter_line][counter_column] = value
#                if matrix[counter_column][counter_line] == 0:
                matrix[counter_column][counter_line] = value    
        #                 matrix.write(str(value)+"\t")
                value = 0
          
          
          
    #write matrix       
    matrixtxt = open("{}matrix.txt".format(root), "w")      
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
    print "matrix.txt written! in {}".format(root)
matrix2 = np.zeros((subset,subset))

models = []
line_ = 0
with open ("{}matrix.txt".format(root), "r") as f:
    for line in f:
        if line_ == 0:
            models = line.split("\t")
            models = models[1:-1]
            line_ += 1
        else:
            column_ = 0
            values = line.split("\t")
            values = values[1:-1]
            for value in values:
                matrix2[line_-1][column_] = value
                column_ += 1
            line_ += 1


print matrix
print type(matrix)
print matrix2
print type(matrix2)
D = matrix

# Compute and plot first dendrogram.
fig = pylab.figure(figsize=(8,8))

ax1 = fig.add_axes([0.09,0.1,0.2,0.6])
Y = sch.linkage(D, method='average')
Z1 = sch.dendrogram(Y, orientation='left')
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
fig.show()
fig.savefig('{}_dendrogram.png'.format(prefix))

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
    print "matrix{}.txt written! in {}".format(i,root)
        
        
            

 

  
