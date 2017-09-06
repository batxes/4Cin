#!/usr/bin/python

#This script is able to compare 2 matrixes and give the output in a heatmap style. Substraction of both matrixes is done.
#Lines  108-118 were created for the Shh inversion explicitly. Take out when publishing all


## CREATE THE CMD TO USE IN CHIMERA
import re,os
import sys
import subprocess
from multiprocessing import Pool
from itertools import combinations, chain
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from data_manager import fileCheck, sizeReader,  calculateNWindowedDistances, calculate_fragment_number
import argparse
from scipy.stats.stats import pearsonr
from scipy.stats.stats import spearmanr

working_dir = (os.path.realpath(__file__)).split("/")[:-2]
working_dir = "/".join(working_dir)+"/"

parser = argparse.ArgumentParser(
description='''Program that compares two virtual Hi-C's.''',
epilog= """primers.txt will be used to highlight beads if primers_vhic.txt is not provided. """)
group1 = parser.add_argument_group('First Models', 'Parameters of the first models')
group1.add_argument("--colormap",action="store",dest="colormap",default = "PuRd_r",help='The colormap of the virtual Hi-C. Matplotlib colormap.')
group2 = parser.add_argument_group('Second Models', 'Parameters of the second models')
parser.add_argument("data_dir", action="store",help='Directory with the 4C files')
group1.add_argument("prefix", action="store",help='Name of the models')
group1.add_argument("VHiC", action="store",help='Virtual Hi-C of the first models')
group1.add_argument("distance", type=int, action="store",help='Maximum distance used in the first models')

group2.add_argument("prefix2", action="store",help='Name of the other models')
group2.add_argument("VHiC2", action="store",help='Virtual Hi-C of the other models')
group2.add_argument("distance2", type=int, action="store",help='Maximum distance used in the other models')


parser.add_argument("--storage_dir", action="store",default=working_dir, dest="storage_dir",help='location where the comparison pdf will be generated')
parser.add_argument("--fragments_in_each_bead", type= int, default=0, dest="fragments_in_each_bead" ,action="store",help='Number of fragments that will be represented with each bead')

args = parser.parse_args()
#print args

root = args.VHiC
root2 = args.VHiC2
storage_dir = args.storage_dir
prefix = args.prefix
prefix2 = args.prefix2
data_dir = args.data_dir
window = args.fragments_in_each_bead
distance = args.distance
distance2 = args.distance2
colormap = args.colormap




#opening vhic primers
color_of_fragments = []
mut_primers = {}
mut_colors = {}
viewpoint_positions = []

# get the name and position from primers.txt
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


try:
    primers_file = open (data_dir+"primers_vhic.txt", 'r')
    for line in primers_file:
        m = re.search('([^\s\t]+).*chr\w+:(\d+)\s*(\w+)?', line)
        try:
            mut_primers[m.group(1)] = int(m.group(2))
            if m.group(3) == None:
                mut_colors[m.group(1)] = "yellow"
            else:
                mut_colors[m.group(1)] = m.group(3)
        except:
			break
except IOError:
    print "\nError: File "+ data_dir+ " primers_vhic.txt does not appear to exist. Using primers.txt to paint positions in the virtual Hi-C\n"
    primers_file = fileCheck(data_dir+"primers.txt")
    for line in primers_file:
        m = re.search('([^\s\t]+).*chr\w+:(\d+)', line)
        try:
            mut_primers[m.group(1)] = int(m.group(2))
            mut_colors[m.group(1)] = "yellow"
        except:
            break

for k,v in mut_primers.iteritems():
	print "Viewpoint:{}\tposition:{}".format(k,v)
	viewpoint_positions.append(v)

#print files
viewpoint_fragments = calculate_fragment_number(viewpoint_positions,files[0])

fragments_in_each_bead = 0
start_frag = 0
end_frag = 0
number_of_fragments = 0
a_4c_file = fileCheck(files[0])
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
if window == 0:
	window = int(number_of_fragments / 100)
	
#viewpoints = [int(i/window) for i in viewpoint_fragments]

# now get number of beads
number_of_spheres = int(number_of_fragments/window)

show_fragments_in_vhic = mut_primers.values()
name_of_fragments = mut_primers.keys()
color = mut_colors.values()
gene_names = [x[:10] for x in name_of_fragments]

show_fragments_in_vhic = calculate_fragment_number(show_fragments_in_vhic,files[0])
show_fragments_in_vhic = [int(i/window) for i in show_fragments_in_vhic]




root3 = "{}{}_vs_{}_mutcomp".format(storage_dir,prefix,prefix2)
root4 = "{}{}_vs_{}_mutcomp_raw".format(storage_dir,prefix,prefix2)
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

guide = range(number_of_spheres)
#we modify positions of inverted genome
# beads 35 to 63 will be now 63 to 35
#print "We are Inverting bins 35-64 of one matrix. Shh experiment."
#delete this, only for INVERSION
#guide[35:64] = guide[64:35:-1]
aux_matrix = np.zeros((number_of_spheres,number_of_spheres))
for line in range(number_of_spheres):
    for col in range(number_of_spheres):
        aux_matrix[line][col] = matrix2[guide[line]][guide[col]]
matrix2 = aux_matrix
# compare both matrixes and create another one with differences
f= open(root3+".txt", 'w')
matrix3 = np.zeros((number_of_spheres,number_of_spheres))
for line in range(number_of_spheres):
    for column in range(number_of_spheres):   
        
        #difference = ((matrix1[line][column])/max_distance - (matrix2[line][column])/max_distance2)
        difference = ((matrix1[line][column])/distance - (matrix2[line][column])/distance2)

        #print "{}/{}\t-\t{}/{}\t=\t{}".format (matrix1[line][column],max_distance,matrix2[line][column],max_distance2,difference)
        matrix3[line][column] = difference
        f.write(str(line)+","+str(column)+","+str(difference))   
        f.write("\n")


f.close()

#  Populate a matrix with both matrices, just for the plotting, un triangle matrix1, the other matrix2
matrix_final = np.zeros((number_of_spheres,number_of_spheres))
for i in range(number_of_spheres):
    for j in range(number_of_spheres):
        matrix_final[i][j] = matrix1[i][j]/distance
        matrix_final[j][i] = matrix2[i][j]/distance2

#correlation
list1 = []
list2 = []
for i in range(number_of_spheres):
    for j in range(number_of_spheres):
        list1.append(matrix_final[i][j])
        list2.append(matrix_final[j][i])
print "pearson: "+str(pearsonr(list1,list2)[0])
print "spearman: "+str(spearmanr(list1,list2)[0])




fig = plt.figure()
plt.title("Virtual Hi-C comparison between mutants.")
ax = plt.subplot(1,1,1)
z = np.array(matrix3)

from matplotlib.colors import LinearSegmentedColormap
vmax = 1.0
vmin = -1.0

# no gradient [1 - 0.3 = RED | 0.3- -0.3 = WHITE | -0.3 - -1 = BLUE]
#cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'blue'),(0.34 / vmax, 'blue'),(0.35 / vmax, 'white',(0.5 / vmax, 'white')),(0.65 / vmax, 'white'),(0.66 / vmax, 'red'),(1 / vmax, 'red')])

#RED BLUE gradient with more white
#cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'blue'),(0.35 / vmax, 'white'),(0.36 / vmax, 'white',(0.5 / vmax, 'white')),(0.64 / vmax, 'white'),(0.65 / vmax, 'white'),(1 / vmax, 'red')])

#RED BLUE gradient with less white
#cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'blue'),(0.40 / vmax, 'white'),(0.41 / vmax, 'white',(0.5 / vmax, 'white')),(0.59 / vmax, 'white'),(0.60 / vmax, 'white'),(1 / vmax, 'red')])

#RED BLUE gradient with almost no white
cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'blue'),(0.50 / vmax, 'white'),(1 / vmax, 'red')])

c = plt.pcolor(z,cmap=cmap,vmax=vmax, vmin=vmin)
ax.set_frame_on(False)
plt.colorbar()


#to set the viewpoints
show_fragments_in_vhic = [c+0.5 for c in show_fragments_in_vhic] #to match the gene_names in the matrix Since the ticks don't match with the heatmap.
plt.scatter(show_fragments_in_vhic,show_fragments_in_vhic, s=20, c=color,cmap=plt.cm.autumn)

ax.set_yticks(show_fragments_in_vhic)
ax.set_xticks(show_fragments_in_vhic)
ax.set_xticklabels(gene_names, minor=False)
ax.set_yticklabels(gene_names, minor=False)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)

plt.axis([0,z.shape[1],0,z.shape[0]])

fig.set_facecolor('white')
#plt.show()

pp = PdfPages('{}.pdf'.format(root3))
pp.savefig(fig)
pp.close()
print '{} vs {} vHi-C comparison written in {}.pdf'.format(prefix,prefix2,root3)

#Now generate the raw comparison figure
fig = plt.figure()
plt.title("Virtual Hi-C comparison between mutants.")
ax = plt.subplot(1,1,1)
z = np.array(matrix_final)
cmap = plt.cm.get_cmap(colormap)
c = plt.pcolor(z,cmap=cmap,vmax=0.85, vmin=0)
plt.colorbar()
#viewpoints = [c+0.5 for c in viewpoints] #to match the gene_names in the matrix Since the ticks don't match with the heatmap.
plt.scatter(show_fragments_in_vhic,show_fragments_in_vhic, s=20, c=color,cmap=plt.cm.autumn)
ax.set_yticks(show_fragments_in_vhic)
ax.set_xticks(show_fragments_in_vhic)
ax.set_xticklabels(gene_names, minor=False)
ax.set_yticklabels(gene_names, minor=False)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)

plt.axis([0,z.shape[1],0,z.shape[0]])

fig.set_facecolor('white')
#plt.show()

pp = PdfPages('{}.pdf'.format(root4))
pp.savefig(fig)
pp.close()
print '{} vs {} vHi-C raw comparison written in {}.pdf'.format(prefix,prefix2,root4)

#Distance between #1 marker 1  and #10 marker 1 : 2203.213
            

