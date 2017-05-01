#!/usr/bin/python

import sys
import inspect
import re
import pysam
import os
import numpy as np
import heapq
import matplotlib
import matplotlib.cm  as cm
import pylab
import argparse

# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
    
# use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"src")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
    
from data_manager import fileCheck, calculate_fragment_number


working_dir = (os.path.realpath(__file__)).split("/")[:-1]
working_dir = "/".join(working_dir)+"/"

parser = argparse.ArgumentParser(
        description = "Script that paints a 3D model generate with 4Cin, providing a bam or bed file.",
        epilog = "if vHi-C (virtual Hi-C) is provided, a clustered RMSD is generated with the beads of the painted model depicted in the diagonal")
parser.add_argument("model", action="store", help="3D model that will be painted.")
parser.add_argument("--vHi-C", action="store", dest="distance_matrix", default = "None", help="vHi-C (virtual Hi-C) file generated with 4Cin.")
parser.add_argument("--name", action="store",dest="prefix",default="4Cin", help="Name for the generated files.")
parser.add_argument("--fragments_in_each_bead",type=int, action="store",dest="fragments_in_each_bead",default=0, help="Number of fragments that will be represented with each bead")
parser.add_argument("data_dir", action="store",help='location of the 4C data. primers.txt file needs to be also in the directory')
parser.add_argument("--working_dir", action="store",default=working_dir, dest="working_dir",help='location where the models will be generated')
parser.add_argument("painting_path", action="store",help="Bed/Bam file.")
parser.add_argument("colormap", action="store",help="Colormap (matplotlib) to paint the model. Check: http://matplotlib.org/examples/color/colormaps_reference.html.")

args = parser.parse_args()
model = args.model
data_dir = args.data_dir
painting_path = args.painting_path
colormap = args.colormap
distance_matrix = args.distance_matrix
prefix = args.prefix
fragments_in_each_bead = args.fragments_in_each_bead
data_dir = args.data_dir
working_dir = args.working_dir

if data_dir[-1] != "/":
    data_dir = data_dir + "/"

#get the name and position from primers.txt
#primers.txt:  name chrN:position
primers = {}
viewpoint_positions = []
primers_file = fileCheck(data_dir+"primers.txt")
for line in primers_file:
    m = re.search('([^\s\t]+).*chr\w+:(\d+)', line)
    try:
        primers[m.group(1)] = int(m.group(2))
    except:
        break
print "\nPrimers.txt. These are the viewpoints that will be used in the modeling:"
for k,v in primers.iteritems():
    print "Viewpoint:{}\tposition:{}".format(k,v)
    viewpoint_positions.append(v)
print

file_names = primers.keys()
files = [data_dir+f for f in file_names]

# read one of the files and get number of fragments and default fragments_in_each_bead
# a_4c_file: chrN start end value
start_frag = 0
end_frag = 0

number_of_fragments = 0

a_4c_file = fileCheck(data_dir+primers.keys()[0])
for line in a_4c_file:
    values = line.split()
    if len(values) != 4:
        continue
    if start_frag == 0:
        start_frag = int(values[1])
    end_frag = int(values[2])
    number_of_fragments += 1

locus_size = end_frag - start_frag
viewpoint_fragments = calculate_fragment_number(viewpoint_positions,files[0])


#default, we want 100 beads in each model
if fragments_in_each_bead == 0:
    fragments_in_each_bead = int(number_of_fragments / 100)

viewpoint_fragments = [int(i/fragments_in_each_bead) for i in viewpoint_fragments]
are_genes = viewpoint_fragments

# now get number of beads
number_of_fragments = int(number_of_fragments/fragments_in_each_bead)



storage_dir = model.split("/")[:-1]
storage_dir = "/".join(storage_dir)

bam_or_bed = painting_path[-3:]
if bam_or_bed != "bam" and bam_or_bed != "bed":
    print "Data file used to paint needs to be a bam or bed file."
    sys.exit()

#read the files and create a bed_file
starts = []
ends = []
if bam_or_bed == "bam":
    print "Reading bam file..."
    bamhandle = pysam.AlignmentFile(painting_path,"rb")
    with open ("bedbam_file","w") as stdout:
        with open (files[0],"r") as stdin:
            for line in stdin:
                values = line.split("\t")
                starts.append(int(values[1]))
                ends.append(int(values[2]))
                #change first char of CHR
                chr_ = list(values[0])
                chr_[0] = 'c'
                values[0] = "".join(chr_)
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
                if counter == number_of_fragments_ALL:
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
        if counter == fragments_in_each_bead:
            normalized_read = added_reads/added_region
            bead_values.append(normalized_read)
            #print normalized_read
            counter = 0
            added_region = 0
            added_reads = 0
    #We dont use the last bead (Modeling does int())
    #if counter != fragments_in_each_bead and counter != 0:  #we add the min value to the last bead if it did not reach to Nfragments 
    #    normalized_read = added_reads/added_region
    #    bead_values.append(normalized_read)

import matplotlib as mpl

#cmap = cm.Blues
cmap = cm.get_cmap(colormap)


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
           
#for ctcf h3k4me3
#print "min value = ",vmax
#print "max value = ",inlier2
#norm = mpl.colors.Normalize(vmin=vmax, vmax=inlier2)

#for dnamet, h3k27ac,atac
#print "min value = ",vmin
#print "max value = ",vmax
norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)


m = cm.ScalarMappable(norm=norm, cmap=cmap)

with open("{}/coloring.cmd".format(storage_dir),"w") as colored_model:
    colored_model.write("open {}\n".format(model))
    for number in range(number_of_fragments):
        current_color = matplotlib.colors.rgb2hex(m.to_rgba(bead_values[number]))
        colored_model.write("color {} #{}\n".format(current_color,number))
        #print "bead: {} color:{} value:{}".format(number,matplotlib.colors.rgb2hex(m.to_rgba(bead_values[number])),bead_values[number])
    colored_model.write("shape tube #{}-{} radius 200 bandlength 10000".format(0,number_of_fragments))

print "coloring.cmd generated in {}/".format(storage_dir)
print "Now, open coloring.cmd wich Chimera."

print "\nGenerating some plots..."
#plot statistic figures
fig = pylab.figure(figsize=(8,8))
fig.suptitle("Epigenetic Marks")
pylab.xlabel("Bead Number")
pylab.ylabel("Score")
#pylab.plot(bead_values)
h = pylab.bar(range(len(bead_values)),bead_values,color=cmap(norm(bead_values)),width=1,linewidth=0)
#for i in range(len(bead_values)-1):
    #pylab.vlines(i,0,bead_values[i],color=cmap(norm(bead_values[i])),linewidth=6)
    #pylab.fill_between([range(len(bead_values))[i],range(len(bead_values))[i+1]],[bead_values[i],bead_values[i+1]],color=cmap(norm(bead_values[i])))

axes = pylab.gca()
axes.set_xlim([0-0.5,len(bead_values)-0.5])
try:
        fig.savefig('{}/genome_painting_stats_plot_{}.png'.format(storage_dir,prefix))
        print "Plot painted in {}/".format(storage_dir,prefix)
except:
        pass

fig = pylab.figure(figsize=(8,8))
pylab.hist(bead_values,bins=100)
fig.suptitle("Epigenetic Marks. Histogram.")
pylab.ylabel("Frequency")
pylab.xlabel("Score")
try:
        fig.savefig('{}/genome_painting_stats_hist_{}.png'.format(storage_dir,prefix))
        print "Histogram painted in {}/".format(storage_dir,prefix)
except:
        pass
fig = pylab.figure(figsize=(8,8))
pylab.boxplot(bead_values)
fig.suptitle("Epigenetic Marks. Boxplot.")
pylab.ylabel("Score")
try:
        fig.savefig('{}/genome_painting_stats_box_{}.png'.format(storage_dir,prefix))
        print "Box plot painted in {}/".format(storage_dir,prefix)
except:
        pass

#distance_matrix needed for this plot
if distance_matrix != "None":
    bead_count = len(bead_values)
    fig = pylab.figure(figsize=(8,8))
    distance_value = []
    epigenetic_value = []
    color_value = []
    with open(distance_matrix, 'r') as mtx:
        for line in mtx:
            values = re.split(",",line)
            if int(values[0]) != int(values[1]):
            #if int(values[0]) == 0:
                distance_value.append(float(values[2]))
                epigenetic_value.append(bead_values[int(values[1])])
                color_value.append(cmap(norm(bead_values))[int(values[0])])
    print len(distance_value)
    for i in range(0,(bead_count-1)*(bead_count-1),bead_count):
        from_ = i
        to_ = i+bead_count-1
        #print distance_value[from_:to_]
        pylab.plot(np.unique(distance_value[from_:to_]), np.poly1d(np.polyfit(distance_value[from_:to_], epigenetic_value[from_:to_], 1))(np.unique(distance_value[from_:to_])))
    pylab.scatter(distance_value,epigenetic_value,color=color_value)
    #fitting
    #pylab.plot(np.unique(distance_value), np.poly1d(np.polyfit(distance_value, epigenetic_value, 1))(np.unique(distance_value)))
    pylab.xlim(0)
    try:
            fig.savefig('genome_painting_proximity_plot.png')
    except:
            pass
    #print distance_value
    #print epigenetic_value
    #print color_value
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



