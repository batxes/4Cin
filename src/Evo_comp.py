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
#plt.style.use('ggplot')
from matplotlib.backends.backend_pdf import PdfPages
from scipy.stats.stats import pearsonr
from scipy.stats.stats import spearmanr




number_of_arguments = len(sys.argv)
if number_of_arguments != 4: #Or all parameters, or no parameters 
    print "Not enought parameters. Config file, matrix_distance1 and matrix_distance2 are required. You passed: ",sys.argv[1:]
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    ini_file = sys.argv[1]
    matrix_path = sys.argv[2]
    matrix_path2 = sys.argv[3]
    
#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    
    prefix = config.get("ModelingValues", "prefix")
    storage_dir = config.get("EvoComp", "storage_dir")
    verbose = int(config.get("ModelingValues", "verbose"))
    WINDOW = float(config.get("EvoComp", "WINDOW"))
    WINDOW2 = float(config.get("EvoComp", "WINDOW2"))
    
    viewpoints = config.get("EvoComp", "viewpoints")
    viewpoints = re.sub('[\n\s\t]','',viewpoints)
    viewpoints = viewpoints.split(",")
    viewpoints = [ int(i) for i in viewpoints]
    viewpoints = [int(i/WINDOW) for i in viewpoints]
    viewpoints2 = config.get("EvoComp", "viewpoints2")
    viewpoints2 = re.sub('[\n\s\t]','',viewpoints2)
    viewpoints2 = viewpoints2.split(",")
    viewpoints2 = [ int(i) for i in viewpoints2]
    viewpoints2 = [int(i/WINDOW2) for i in viewpoints2]
    n_viewpoints = len(viewpoints2)
    max_distance = int(config.get("EvoComp", "max_dist"))
    max_distance2 = int(config.get("EvoComp", "max_dist2"))
    
    
    gene_names = config.get("EvoComp", "gene_names")
    gene_names = re.sub('[\n\s\t]','',gene_names)
    gene_names = gene_names.split(",")
    gene_names2 = config.get("EvoComp", "gene_names2")
    gene_names2 = re.sub('[\n\s\t]','',gene_names2)
    gene_names2 = gene_names2.split(",")
    
    number_of_cpu = int(config.get("TADs", "number_of_cpu"))
    maximum_hic_value= float(config.get("EvoComp", "maximum_hic_value"))

except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()
viewpoints_ticks = [c+0.5 for c in viewpoints] #to match the gene_names in the matrix Since the ticks don't match with the heatmap.
matrix = np.zeros((n_viewpoints,n_viewpoints))
matrix2 = np.zeros((n_viewpoints,n_viewpoints))
matrix_final = np.zeros((n_viewpoints,n_viewpoints))
print viewpoints
print viewpoints2
print matrix_path
print matrix_path2

count1 = -1
print "Filling first half..."
for bead1 in viewpoints:
    count1 += 1
    count2 = -1
    for bead2 in viewpoints:
        count2 += 1
        with open("{}".format(matrix_path), "r") as mtx:
            for line in mtx:
                values = re.split(",", line)
                if int(values[0]) ==  bead1 and int(values[1]) == bead2:
                    matrix[count1][count2] = float(values[2])/max_distance
                    break
        

print "Filling the other half..."
count1 = -1
for bead1 in viewpoints2:
    count1 += 1
    count2 = -1
    for bead2 in viewpoints2:
        count2 += 1
        with open("{}".format(matrix_path2), "r") as mtx2:
            for line in mtx2:
                values = re.split(",", line)
                if int(values[0]) ==  bead1 and int(values[1]) == bead2:
                    matrix2[count2][count1] = float(values[2])/max_distance2
                    break

matrix_diff = np.zeros((n_viewpoints,n_viewpoints))
for i in range(n_viewpoints):
    for j in range(n_viewpoints):
        matrix_final[i][j] = matrix[i][j]
        matrix_final[j][i] = matrix2[i][j]
        matrix_diff[i][j] = matrix_diff[j][i] = matrix[i][j] - matrix2[i][j]




array1 = []
array2 = []
for i in range(n_viewpoints):
    for j in range(n_viewpoints):
        array1.append(matrix[i][j])
for i in range(n_viewpoints):
    for j in range(n_viewpoints):
        array2.append(matrix2[i][j])

print "pearson: "+str(pearsonr(array1,array2))
print "spearman: "+str(spearmanr(array1,array2))

print len(array2)
    


if verbose==3:  print "Generating matrix to plot..."     
fig = plt.figure()
ax = plt.subplot(1,1,1)
z = np.array(matrix_final)

c = plt.pcolor(z,cmap=plt.cm.PuRd_r,vmax=maximum_hic_value, vmin=0)
for y in range(z.shape[0]):
    for x in range(z.shape[1]):
        plt.text(x+0.5,y+0.5,'%.2f' % z[y,x],horizontalalignment='center',verticalalignment='center',size=5)
#ax.set_frame_on(False)
plt.colorbar()


#to set the viewpoints
#color = [10,5,5,10,10]
#plt.scatter(genes, genes, s=10, cmap=plt.cm.autumn)
tick_location = [i+0.5 for i in range(len(viewpoints))]
ax.set_yticks(tick_location)
ax.set_xticks(tick_location)
ax.set_xticklabels(gene_names2, minor=False)
ax.set_yticklabels(gene_names, minor=False)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)

plt.axis([0,z.shape[1],0,z.shape[0]])

fig.set_facecolor('white')
plt.show()

pp = PdfPages('{}{}_evocomp.pdf'.format(storage_dir,prefix))
pp.savefig(fig)
pp.close()
print '{}_evocomp.pdf writen'.format(prefix)
#Distance between #1 marker 1  and #10 marker 1 : 2203.213

from matplotlib.colors import LinearSegmentedColormap
vmax = 1.0
cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'white'),(0.35 / vmax, 'white'),(0.5 / vmax, 'green'),(0.65 / vmax, 'white'),(1 / vmax, 'white')])
fig = plt.figure()
ax = plt.subplot(1,1,1)
z = np.array(matrix_diff)

#c = plt.pcolor(z,cmap=plt.cm.PRGn,vmax=1,vmin=-1)
c = plt.pcolor(z,cmap=cmap,vmax=1,vmin=-1)
for y in range(z.shape[0]):
    for x in range(z.shape[1]):
        plt.text(x+0.5,y+0.5,'%.2f' % z[y,x],horizontalalignment='center',verticalalignment='center',size=5)
plt.colorbar()
tick_location = [i+0.5 for i in range(len(viewpoints))]
ax.set_yticks(tick_location)
ax.set_xticks(tick_location)
ax.set_xticklabels(gene_names2, minor=False)
ax.set_yticklabels(gene_names, minor=False)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)

plt.axis([0,z.shape[1],0,z.shape[0]])

fig.set_facecolor('white')
plt.show()

pp = PdfPages('{}{}_evocomp_diff.pdf'.format(storage_dir,prefix))
pp.savefig(fig)
pp.close()
print '{}_evocomp_diff.pdf writen'.format(prefix)
            
