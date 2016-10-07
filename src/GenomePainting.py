#!/usr/bin/python

import sys
import re
import ConfigParser
import pysam

import numpy as np
from colour import Color
import heapq
import matplotlib.cm  as cm
import pylab

number_of_arguments = len(sys.argv)
if number_of_arguments != 3: #Or all parameters, or no parameters 
    print "Not enought parameters. Model to be painted and config file are needed. You passed: ",sys.argv[1:]
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    model = sys.argv[1]
    ini_file = sys.argv[2]

#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    verbose = int(config.get("ModelingValues", "verbose"))
    prefix = config.get("ModelingValues", "prefix")
    
    WINDOW = float(config.get("ModelingValues", "WINDOW"))
    
    files = config.get("ModelingValues", "files")
    files = re.sub('[\n\s\t]','',files)
    files = files.split(",")    
    
    viewpoints = config.get("ModelingValues", "viewpoints")
    viewpoints = re.sub('[\n\s\t]','',viewpoints)
    viewpoints = viewpoints.split(",")
    viewpoints = [ int(i) for i in viewpoints]
    viewpoints = [int(i/WINDOW) for i in viewpoints]
    
    NFRAGMENTS_ALL = int(config.get("ModelingValues", "NFRAGMENTS"))
    NFRAGMENTS = int(NFRAGMENTS_ALL/WINDOW)
    
    working_dir = config.get("ModelingValues", "working_dir")



    painting_path = config.get("Painting","file_path")
    color_from = config.get("Painting","color_from")
    color_to = config.get("Painting","color_to")
    bam_or_bed = config.get("Painting","bam_or_bed")
    
    
    
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()

#read the files and create a bed_file
starts = []
ends = []
if bam_or_bed == "bam":
    print "Reading Atac bam file..."
    bamhandle = pysam.AlignmentFile(painting_path,"rb")
    with open ("bedbam_file","w") as stdout:
        with open (files[0],"r") as stdin:
            for line in stdin:
                values = line.split("\t")
                starts.append(int(values[1]))
                ends.append(int(values[2]))
                read_count = bamhandle.count(values[0],int(values[1]),int(values[2])) #chrm, start, end
                stdout.write("{}\t{}\t{}\t{}\n".format(values[0],values[1],values[2],read_count))


elif bam_or_bed == "bed":
    with open (files[0],"r") as stdin:
        for line in stdin:
            values = line.split("\t")
            starts.append(int(values[1]))
            ends.append(int(values[2]))
    # create bed file for DNAmet
    print "Reading DNA met file..."
    counter = 0
    total_reads = 0
    with open (painting_path,"r") as stdin:
        print "Writing bed file with DNA met data..."
        with open ("bedbam_file","w") as stdout:
            for line in stdin:
                if counter == NFRAGMENTS_ALL:
                    break
                else:
                    values = line.split("\t")
                    if int(values[0]) == 13:
                        if starts[counter] <= int(values[1]) <= ends[counter]:
                            total_reads += float(values[4])/float(values[5])
                        else:
                            if total_reads == 0 and counter > 0 and starts[counter] <= int(values[1]): #gap in data
                                stdout.write("{}\t{}\t{}\t{}\n".format("chr13",starts[counter],ends[counter],0))
                                counter += 1
                                
                            if total_reads != 0:
                                stdout.write("{}\t{}\t{}\t{}\n".format("chr13",starts[counter],ends[counter],total_reads))
                                counter += 1
                                total_reads = 0


# create bed file
print "Painting genome..."
#file format: chr    from    to  value
bead_values = []
with open ("bedbam_file","r") as stdin:
    counter = 0
    added_reads = 0
    added_region = 0
    for line in stdin:
        values = line.split("\t")
        added_region += float(values[2])-float(values[1])
        added_reads += float(values[3])
        counter += 1
        if counter == WINDOW:
            normalized_read = added_reads/added_region
            bead_values.append(normalized_read)
            #print normalized_read
            counter = 0
            added_region = 0
            added_reads = 0
    if counter != WINDOW and counter != 0:  #we add the min value to the last bead if it did not reach to Nfragments 
        normalized_read = added_reads/added_region
        bead_values.append(normalized_read)

from pylab import *
import matplotlib as mpl
import matplotlib.cm as cm
#cmap = cm.hot_r
cmap = cm.Reds

#plot statistic figures
fig = pylab.figure(figsize=(8,8))
pylab.hist(bead_values,bins=100)
try:
        fig.savefig('genome_painting_stats_hist.png')
except:
        pass
fig = pylab.figure(figsize=(8,8))
pylab.boxplot(bead_values)
try:
        fig.savefig('genome_painting_stats_box.png')
except:
        pass

#take out outliers (Q1-1.5xIQR - Q3+1.5*IQR take only)
mid = np.percentile(bead_values,50)
Q1 = np.percentile(bead_values,25)
Q3 = np.percentile(bead_values,75)
IQR =  Q3 - Q1
inlier1 = Q1 - 1.5*IQR
inlier2 = Q3 + 1.5*IQR
vmax = 0
for max_value in bead_values:
    if max_value >= inlier1 and max_value <= inlier2:
        if max_value > vmax:
            vmax = max_value
vmin = 1000000
for min_value in bead_values:
    if min_value >= inlier1 and min_value <= inlier2:
        if min_value <= vmin:
            vmin = min_value
           
#for atac and h3k4me3
#print "min value = ",vmax
#print "max value = ",inlier2
#norm = mpl.colors.Normalize(vmin=vmax, vmax=inlier2)
print bead_values
#for dnamet
print "min value = ",vmin
print "max value = ",vmax
norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
m = cm.ScalarMappable(norm=norm, cmap=cmap)

with open("coloring.cmd","w") as colored_model:
    colored_model.write("open {}\n".format(model))
    for number in range(NFRAGMENTS):
        colored_model.write("color {} #{}\n".format(matplotlib.colors.rgb2hex(m.to_rgba(bead_values[number])),number))
        #print "bead: {} color:{} value:{}".format(number,matplotlib.colors.rgb2hex(m.to_rgba(bead_values[number])),bead_values[number])
    colored_model.write("shape tube #{}-{} radius 200 bandlength 10000".format(0,NFRAGMENTS))


print "Now, open coloring.cmd wich Chimera."

#test.
# check out size of beads in the scatterplot
# check out the matrix_path
#check out the vmin and vmax
dendro_test = False
if dendro_test:
    ####################
    import sys
    import operator
    import re
    import subprocess
    from os import listdir, remove
    from os.path import isfile, join
    from itertools import combinations
    import ConfigParser
    import scipy.cluster.hierarchy as sch
    import pylab
    from pylab import plot,show
    from scipy.cluster.vq import kmeans,vq



    matrix_path = "/home/ibai/4c2vhic/data/Six_zebra_models/Six_zebra_models_final_output_0.1_-0.1_13000/distances_of_current_model_Six_zebra_models"
    #matrix_path = "/home/ibai/4c2vhic/distances_of_current_model_zebra_200.txt"
    article = True
    enriched_dendro = True
    cutoff = 0.25
    cutoff = 0.0 #ALL beads
    value_list = []
    count = 0
    bead_values = bead_values[0:-1]
    bead_colors = []
    if article:
        for bead in bead_values:
            bead_colors.append(bead)
            if enriched_dendro:
                if bead >= cutoff:
                    value_list.append(count)
            else:
                if bead < cutoff:
                    value_list.append(count)
            count += 1

    matrix = np.zeros((len(value_list),len(value_list)))

    count1 = -1
    for bead1 in value_list:
        count1 += 1
        count2 = -1
        for bead2 in value_list:
            count2 += 1
            with open("{}".format(matrix_path), "r") as mtx:
                for line in mtx:
                    values = re.split(",", line)
                    if int(values[0]) ==  bead1 and int(values[1]) == bead2:
                        matrix[count1][count2] = float(values[2])
                        matrix[count2][count1] = float(values[2])
                        break

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

    axmatrix.set_xticks(range(len(value_list)))
    ordered_values = [value_list[i] for i in Z1['leaves']]
    axmatrix.set_xticklabels(ordered_values)
    axmatrix.xaxis.set_label_position('bottom')
    axmatrix.xaxis.tick_bottom()
    pylab.xticks(rotation=-90,fontsize=8)

    axmatrix.set_yticks([])

    # Plot colorbar.
    axcolor = fig.add_axes([0.91,0.1,0.02,0.6])
    pylab.colorbar(im, cax=axcolor)

    #scatter plot
    color = [bead_colors[i] for i in ordered_values]
    aux = []
    cut_max = vmax
    cut_min = vmin
    cut_max = mid
    cut_min = mid
    for t in color:
        if t > cut_max:
            aux.append(max(bead_values)) 
        elif t <= cut_min:
            aux.append(min(bead_values))
        else:
            aux.append(t)
    color = aux

    axmatrix.scatter(range(len(value_list)), range(len(value_list)), s=80, c=color,vmin=min(bead_values),vmax=max(bead_values),cmap=cm.Reds)

    #fig.show()
    try:
            fig.savefig('atac_heatmap.png')
    except:
            pass



