#!/usr/bin/python

# script to compare virtual and original Hi-c's

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
if True:
    number_of_arguments = len(sys.argv)
    if number_of_arguments != 3: #Or all parameters, or no parameters 
        print "Not enought parameters. virtual Hi-c matrix and Original Hi-C matrix are required. You passed: ",sys.argv[1:]
        sys.exit()
    if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
        matrix_path = sys.argv[1]
        matrix_path2 = sys.argv[2]
        
    n_viewpoints = 70
    max_distance = 5000
    #read the config file
    matrix = np.zeros((n_viewpoints,n_viewpoints))
    matrix2 = np.zeros((n_viewpoints,n_viewpoints))
    matrix_final = np.ones((n_viewpoints,n_viewpoints))

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
                        matrix[count1][count2] = float(values[2])
                        matrix[count2][count1] = float(values[2])
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
                        matrix2[count2][count1] = float(values[2])
                        matrix2[count1][count2] = float(values[2])
                        break

    max_list1 = []
    max_list2 = []
    for i in range(n_viewpoints):
        for j in range(n_viewpoints):
            max_list1.append(matrix[i][j])
            max_list2.append(matrix2[i][j])
    print "pearson: "+str(pearsonr(max_list1,max_list2))
    print "spearman: "+str(spearmanr(max_list1,max_list2))
    max_value_vhic = max(max_list1)
    min_value_vhic = min(max_list1)
    max_value_hic = max(max_list2)
    min_value_hic = min(max_list2)
    print "max and min vhic: {} - {}:".format(max_value_vhic,min_value_vhic)
    print "max and min hic: {} - {}:".format(max_value_hic,min_value_hic)
    max_list1 = []
    max_list2 = []
    for i in range(n_viewpoints):
        for j in range(n_viewpoints):
            if not j == i:
                vhic_value = 1-matrix[i][j]/max_distance
                try:
                    hic_value = matrix2[i][j]/max_value_hic
                    if hic_value != 0.0 and vhic_value != 0.0:
                        max_list1.append(vhic_value)
                        max_list2.append(hic_value)
                    matrix_final[i][j] = vhic_value 
                    matrix_final[j][i] = hic_value
                except:
                    continue

    print "pearson: "+str(pearsonr(max_list1,max_list2))
    print "spearman: "+str(spearmanr(max_list1,max_list2))

    print len(max_list1)
    print len(max_list2)

    fig = plt.figure()
    ax = plt.subplot(1,1,1)
    z = np.array(matrix_final)
    #maximum_hic_value = max(matrix_final)
    maximum_hic_value = max(max_list2)

    #only for rao
    #maximum_hic_value = 0.03

    c = plt.pcolor(z,cmap=plt.cm.magma,vmax=maximum_hic_value, vmin=0)
    #for y in range(z.shape[0]):
    #    for x in range(z.shape[1]):
    #        plt.text(x+0.5,y+0.5,'%.2f' % z[y,x],horizontalalignment='center',verticalalignment='center',size=5)
    #ax.set_frame_on(False)
    plt.colorbar()
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.xticks(rotation=90)

    plt.axis([0,z.shape[1],0,z.shape[0]])

    fig.set_facecolor('white')
    plt.show()
    print "Matrix saved in this directory."
    fig.savefig('HiC_comp.png',dpi = 300)

    #pp = PdfPages('HiC_comp.pdf')
    #pp.savefig(fig)
    #pp.close()
else:
    #supp fig 8
    # to do a little matrix of correlations

    matrix_corr = np.zeros((5,5))
    matrix_corr[0][1] = 0.75187534318386928
    matrix_corr[0][2] = 0.66754083023667898
    matrix_corr[0][3] = 0.55333425695285288
    matrix_corr[0][4] = 0.6635652284316963
    matrix_corr[1][2] = 0.72785481811649311
    matrix_corr[1][3] = 0.53935018788718381
    matrix_corr[1][4] = 0.69158619892835715
    matrix_corr[2][3] = 0.60221587323595382
    matrix_corr[2][4] = 0.66368559486847933
    matrix_corr[3][4] = 0.59119889876050857


    fig = plt.figure()
    ax = plt.subplot(1,1,1)
    z = np.array(matrix_corr)
    c = plt.pcolor(z,cmap=plt.cm.hot_r,vmax=1, vmin=0.5)
    plt.colorbar()

    plt.axis([0,z.shape[1],0,z.shape[0]])

    fig.set_facecolor('white')
    plt.show()

    fig.savefig('HiC_comp.png',dpi = 300)
