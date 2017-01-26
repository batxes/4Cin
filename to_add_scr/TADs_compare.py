#!/usr/bin/python

#This script is able to compare 2 matrixes and give the output in a heatmap style. Substraction of both matrixes is done.

## CREATE THE CMD TO USE IN CHIMERA
import re
import sys
import subprocess
from multiprocessing import Pool
from itertools import combinations, chain
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import ConfigParser

number_of_arguments = len(sys.argv)
if number_of_arguments != 4: #Or all parameters, or no parameters 
    print "Not enought parameters. Config file, matrix_distance1 and matrix_distance2 are required. You passed: ",sys.argv[1:]
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    ini_file = sys.argv[1]
    root = sys.argv[2]
    root2 = sys.argv[3]


#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)

    prefix = config.get("ModelingValues", "prefix")
    storage_dir = config.get("MutComp", "storage_dir")
    verbose = int(config.get("ModelingValues", "verbose"))
    WINDOW = float(config.get("MutComp", "WINDOW"))
    NFRAGMENTS = int(config.get("ModelingValues", "NFRAGMENTS"))
    number_of_spheres = int(NFRAGMENTS/WINDOW)
    number_of_spheres = number_of_spheres - 1

    viewpoints = config.get("MutComp", "viewpoints")
    viewpoints = re.sub('[\n\s\t]','',viewpoints)
    viewpoints = viewpoints.split(",")
    viewpoints = [ int(i) for i in viewpoints]
    viewpoints = [int(i/WINDOW) for i in viewpoints]
    n_viewpoints = len(viewpoints)
    #max_distance = int(config.get("MutComp", "max_dist"))
    #max_distance2 = int(config.get("MutComp", "max_dist2"))


    gene_names = config.get("MutComp", "names")
    gene_names = re.sub('[\n\s\t]','',gene_names)
    gene_names = gene_names.split(",")

    color = config.get("TADs", "color")
    color = re.sub('[\n\s\t]','',color)
    color = color.split(",")
    color = [ int(i) for i in color]
    number_of_cpu = int(config.get("TADs", "number_of_cpu"))
    #maximum_hic_value= float(config.get("EvoComp", "maximum_hic_value"))

except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()

root3 = "{}{}Mutant_comparison".format(storage_dir,prefix)
matrix1 = np.zeros((number_of_spheres,number_of_spheres))
max_distance = 0
with open(root, 'r') as f1:
    for line in f1:
        values = re.split(',', line)
        bead_from = int(values[0])
        bead_to = int(values[1])
        read = float(values[2])
        if bead_from < number_of_spheres and bead_to < number_of_spheres:
            matrix1[bead_from][bead_to] = read
            matrix1[bead_to][bead_from] = read
            if read > max_distance:
                max_distance = read

matrix2 = np.zeros((number_of_spheres,number_of_spheres))
max_distance2 = 0
with open(root2, 'r') as f2:
    for line in f2:
        values = re.split(',', line)
        bead_from = int(values[0])
        bead_to = int(values[1])
        read = float(values[2])
        if bead_from < number_of_spheres and bead_to < number_of_spheres:
            matrix2[bead_from][bead_to] = read
            matrix2[bead_to][bead_from] = read
            if read > max_distance2:
                max_distance2 = read

#we modify positions of inverted genome
# beads 35 to 63 will be now 63 to 35
guide = range(number_of_spheres)
print guide
guide[35:64] = guide[63:34:-1]
print guide
aux_matrix = np.zeros((number_of_spheres,number_of_spheres))
for line in range(number_of_spheres):
    for col in range(number_of_spheres):
        aux_matrix[line][col] = matrix2[guide[line]][guide[col]]


matrix2 = aux_matrix
#matrix2[35:63,35:63] = matrix2[63:35:-1,63:35:-1] 

# compare both matrixes and create another one with differences

f= open(root3, 'w')
matrix3 = np.zeros((number_of_spheres,number_of_spheres))
diff_list = []
for line in range(number_of_spheres):
    for column in range(number_of_spheres):   
        
        difference = ((matrix1[line][column])/max_distance - (matrix2[line][column])/max_distance2)
        #print "{}/{}\t-\t{}/{}\t=\t{}".format (matrix1[line][column],max_distance,matrix2[line][column],max_distance2,difference)
        diff_list.append(difference)
        matrix3[line][column] = difference
        f.write(str(line)+","+str(column)+","+str(difference))   
        f.write("\n")

f.close()


fig = plt.figure()
ax = plt.subplot(1,1,1)
z = np.array(matrix3)


#vmax = np.max(diff_list)
#vmin = np.min(diff_list)


from matplotlib.colors import LinearSegmentedColormap
vmax = 1.0
vmin = -1.0

# no gradient [1 - 0.3 = RED | 0.3- -0.3 = WHITE | -0.3 - -1 = BLUE]
#cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'blue'),(0.34 / vmax, 'blue'),(0.35 / vmax, 'white',(0.5 / vmax, 'white')),(0.65 / vmax, 'white'),(0.66 / vmax, 'red'),(1 / vmax, 'red')])

#RED BLUE gradient 
#cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'blue'),(0.5 / vmax, 'white'),(1 / vmax, 'red')])

#RED BLUE gradient with more white
#cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'blue'),(0.35 / vmax, 'white'),(0.36 / vmax, 'white',(0.5 / vmax, 'white')),(0.64 / vmax, 'white'),(0.65 / vmax, 'white'),(1 / vmax, 'red')])

#RED BLUE gradient with less white
cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'blue'),(0.40 / vmax, 'white'),(0.41 / vmax, 'white',(0.5 / vmax, 'white')),(0.59 / vmax, 'white'),(0.60 / vmax, 'white'),(1 / vmax, 'red')])

c = plt.pcolor(z,cmap=cmap,vmax=vmax, vmin=vmin)
ax.set_frame_on(False)
plt.colorbar()


#to set the viewpoints
viewpoints = [c+0.5 for c in viewpoints] #to match the gene_names in the matrix Since the ticks don't match with the heatmap.
plt.scatter(viewpoints,viewpoints, s=20, c=color,cmap=plt.cm.autumn)

ax.set_yticks(viewpoints)
ax.set_xticks(viewpoints)
ax.set_xticklabels(gene_names, minor=False)
ax.set_yticklabels(gene_names, minor=False)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)

plt.axis([0,z.shape[1],0,z.shape[0]])

fig.set_facecolor('white')
#plt.show()

pp = PdfPages('{}_HiC.pdf'.format(root3))
pp.savefig(fig)
pp.close()
print '{}_HiC.pdf writen'.format(prefix)

#Distance between #1 marker 1  and #10 marker 1 : 2203.213
            

