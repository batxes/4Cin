#!/usr/bin/python

# Script modified from Tads_multi to take data from real hi-c's in this format:
# 0,0,12312
# 0,1,111
# 0,2,1132
# ...
#and generates the heatmap

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


number_of_arguments = len(sys.argv)
if number_of_arguments != 2: #Or all parameters, or no parameters 
    print "Not enought parameters. Matrix file (absolute path) is required. You passed: ",sys.argv[1:]
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    root = sys.argv[1]
    matrix_path = sys.argv[1]
    root = matrix_path.split("/")[0:-1]
    root = '/'.join(root)
    root = root+"/"
root = "/home/ibai/4Cin/"
print root
    
prefix = "vHiC_from_Real"
distance_file = "get_genome_distance_{}".format(prefix)
path = "{}distances_of_current_model_{}".format(root,prefix)
start_time = time.time()

NFRAGMENTS = 0
with open(matrix_path, 'r') as std_in:
    for line in std_in:
        values = line.split(",") 
        NFRAGMENTS = int(values[0])

NFRAGMENTS += 1
with open(matrix_path, 'r') as std_in:
    matrix_mean = np.zeros((NFRAGMENTS,NFRAGMENTS))
    for line in std_in:
        values = line.split(",")
        #print values
        matrix_mean[int(values[0])][int(values[1])] = float(values[2])

max_list = []
for line in matrix_mean:
    max_list.append(max(line))

#matrix_mean = matrix_mean[15:-15,15:-15]
#viewpoints = [x-15 for x in viewpoints]
fig = plt.figure()
ax = plt.subplot(1,1,1)
z = np.array(matrix_mean)



vmax = max(max_list)
vmax = 50 #foxo1 real hic human
c = plt.pcolor(z,cmap=plt.cm.PuRd,vmax=vmax, vmin=0)
ax.set_frame_on(False)
plt.colorbar()

#viewpoints = 51,15,57,69 #pax3,epha4,sgpp2,farsb human
#viewpoints = 111,115,61,58 #foxo1,mrps31,cog6,lhfp human
#viewpoints = 47,53,62,13 #pax3,sgpp2,farsb,epha4 mouse
#viewpoints = 58,50,96,97 #foxo1,maml3,cog6,lhfp mouse
#to set the viewpoints
#plt.scatter(viewpoints, viewpoints, s=20, c=color,cmap=plt.cm.autumn)
#plt.scatter(viewpoints, viewpoints, s=20,cmap=plt.cm.autumn)

#ax.set_yticks(viewpoints)
#ax.set_xticks(viewpoints)
#ax.set_xticklabels(gene_names, minor=False)
#ax.set_yticklabels(gene_names, minor=False)
#plt.tick_params(axis='both', which='major', labelsize=8)
#plt.xticks(rotation=90)

plt.axis([0,z.shape[1],0,z.shape[0]])

fig.set_facecolor('white')
#plt.show()

pp = PdfPages('{}{}_HiC.pdf'.format(root,prefix))
pp.savefig(fig)
pp.close()
print '{}{}_HiC.pdf writen'.format(root,prefix)
print "{} segundos".format(time.time() - start_time)
#Distance between #1 marker 1  and #10 marker 1 : 2203.213
            
