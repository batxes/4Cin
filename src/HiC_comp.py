#!/usr/bin/python

# script to compare virtual and original Hi-c's

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
if number_of_arguments != 3: #Or all parameters, or no parameters 
    print "Not enought parameters. virtual Hi-c matrix and Original Hi-C matrix are required. You passed: ",sys.argv[1:]
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    matrix_path = sys.argv[1]
    matrix_path2 = sys.argv[2]
    
n_viewpoints = 74
max_distance = 10000
#read the config file
matrix = np.zeros((n_viewpoints,n_viewpoints))
matrix2 = np.zeros((n_viewpoints,n_viewpoints))
matrix_final = np.zeros((n_viewpoints,n_viewpoints))

count1 = -1
print "Filling first half..."
for bead1 in range(n_viewpoints):
    count1 += 1
    count2 = -1
    for bead2 in range(n_viewpoints):
        count2 += 1
        with open("{}".format(matrix_path), "r") as mtx:
            for line in mtx:
                values = re.split(",", line)
                if int(values[0]) ==  bead1 and int(values[1]) == bead2:
                    matrix[count1][count2] = 1/(float(values[2])+1) / 0.00298806386879 #KNOWN VALUE with max(array1)
                    matrix[count2][count1] = 1/(float(values[2])+1) / 0.00298806386879 #KNOWN VALUE with max(array1)
                    break
        

print "Filling the other half..."
count1 = -1
for bead1 in range(n_viewpoints):
    count1 += 1
    count2 = -1
    for bead2 in range(n_viewpoints):
        count2 += 1
        with open("{}".format(matrix_path2), "r") as mtx2:
            for line in mtx2:
                values = re.split(",", line)
                if int(values[0]) ==  bead1 and int(values[1]) == bead2:
                    matrix2[count2][count1] = float(values[2])/65.001709121   #KNOWN VALUE with max(array2)
                    matrix2[count1][count2] = float(values[2])/65.001709121   #KNOWN VALUE with max(array2)
                    break

for i in range(n_viewpoints):
    for j in range(n_viewpoints):
        matrix_final[i][j] = matrix[i][j]
        matrix_final[j][i] = matrix2[i][j]




array1 = []
array2 = []
for i in range(n_viewpoints):
    for j in range(n_viewpoints):
        array2.append(matrix2[i][j])
        if matrix2[i][j] == 0:
            array1.append(matrix[i][j])
            array1.append(0)
        else:
            array1.append(matrix[i][j])

print "pearson: "+str(pearsonr(array1,array2))
print "spearman: "+str(spearmanr(array1,array2))

print min(array1)
print min(array2)
print max(array1)
print max(array2)
    
print matrix_final


fig = plt.figure()
ax = plt.subplot(1,1,1)
z = np.array(matrix_final)
#maximum_hic_value = max(matrix_final)
maximum_hic_value = max(array2)

c = plt.pcolor(z,cmap=plt.cm.PuRd,vmax=maximum_hic_value, vmin=0)
#for y in range(z.shape[0]):
#    for x in range(z.shape[1]):
#        plt.text(x+0.5,y+0.5,'%.2f' % z[y,x],horizontalalignment='center',verticalalignment='center',size=5)
#ax.set_frame_on(False)
plt.colorbar()


#to set the viewpoints
#color = [10,5,5,10,10]
#plt.scatter(genes, genes, s=10, cmap=plt.cm.autumn)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)

plt.axis([0,z.shape[1],0,z.shape[0]])

fig.set_facecolor('white')
plt.show()

pp = PdfPages('HiC_comp.pdf')
pp.savefig(fig)
pp.close()
#Distance between #1 marker 1  and #10 marker 1 : 2203.213

