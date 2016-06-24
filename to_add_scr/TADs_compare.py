#!/usr/bin/python

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
sys.path.insert(1,'/home/bioinfo/workspace/genome/utils')
from variables import WINDOW, prefix, NFRAGMENTS, files, genes


# if myf5_wt:
#     color = [10,5,5,10,10,10,10,10]
#     gene_names = ['ctcf12','myf5','myf4', 'ecr17','ecr29','ecr56.5','ecr111', 'ctcf219']
#     distance_file = "get_genome_distances_myf5_wt.py"  
# if myf5_mut:
#     color = [10,5,10,10,10,10,10]
#     gene_names = ['ctcf12','myf4', 'ecr17','ecr29','ecr56.5','ecr111', 'ctcf219']
#     distance_file = "get_genome_distances_myf5_mut.py"  
     
    
# genes = [c+0.5 for c in genes] #to match the gene_names in the matrix Since the ticks don't match with the heatmap.

number_of_spheres = 149 #the smallest one (myf5 mut)
gene_names = ['ctcf12','myf5','myf4', 'ecr17','ecr29','ecr56.5','ecr111', 'ctcf219']
root = "/home/bioinfo/workspace/genome/myf5_wt_final_output_1.1_-0.1_3000/distances_of_current_model_myf5_wt.txt"
root2 = "/home/bioinfo/workspace/genome/myf5_mut_final_output_0.9_-0.1_3000/distances_of_current_model_myf5_mut.txt"
root3 = "/home/bioinfo/workspace/genome/distances_of_current_model_compare_myf5.txt"

# root = "/home/bioinfo/workspace/genome/utils/distances_of_current_model_test.txt"
# root2 = "/home/bioinfo/workspace/genome/utils/distances_of_current_model_test2.txt"
# root3 = "/home/bioinfo/workspace/genome/distances_of_current_model_compare_test.txt"

matrix1 = np.zeros((number_of_spheres,number_of_spheres))
with open(root, 'r') as f1:
    for line in f1:
        values = re.split(',', line)
        bead_from = int(values[0])
        bead_to = int(values[1])
        if bead_from < number_of_spheres and bead_to < number_of_spheres:
            matrix1[bead_from][bead_to] = float(values[2])
            matrix1[bead_to][bead_from] = float(values[2])

matrix2 = np.zeros((number_of_spheres,number_of_spheres))
with open(root2, 'r') as f2:
    for line in f2:
        values = re.split(',', line)
        bead_from = int(values[0])
        bead_to = int(values[1])
        if bead_from < number_of_spheres and bead_to < number_of_spheres:
            matrix2[bead_from][bead_to] = float(values[2])
            matrix2[bead_to][bead_from] = float(values[2])


# compare both matrixes and create another one with differences

f= open(root3, 'w')
matrix3 = np.zeros((number_of_spheres,number_of_spheres))
diff_list = []
for line in range(number_of_spheres):
    for column in range(number_of_spheres):   
        
        difference = (matrix1[line][column]-matrix2[line][column])
        diff_list.append(difference)
        matrix3[line][column] = difference
        f.write(str(line)+","+str(column)+","+str(difference))   
        f.write("\n")

f.close()


fig = plt.figure()
ax = plt.subplot(1,1,1)
z = np.array(matrix3)


max_value = np.max(diff_list)
min_value = np.min(diff_list)

print max_value
print min_value
c = plt.pcolor(z,cmap=plt.cm.jet,vmax=max_value, vmin=min_value)
ax.set_frame_on(False)
plt.colorbar()


#to set the viewpoints
# plt.scatter(genes, genes, s=10, c=color,cmap=plt.cm.autumn)


ax.set_yticks(genes)
ax.set_xticks(genes)
ax.set_xticklabels(gene_names, minor=False)
ax.set_yticklabels(gene_names, minor=False)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)

plt.axis([0,z.shape[1],0,z.shape[0]])

fig.set_facecolor('white')
plt.show()

pp = PdfPages('{}_HiC.pdf'.format(prefix))
pp.savefig(fig)
pp.close()
print '{}_HiC.pdf writen'.format(prefix)

#Distance between #1 marker 1  and #10 marker 1 : 2203.213
            

