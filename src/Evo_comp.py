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
import argparse

working_dir = (os.path.realpath(__file__)).split("/")[:-1]
working_dir = "/".join(working_dir)+"/"

parser = argparse.ArgumentParser(
description='''Program that compares two virtual Hi-C's.''',
epilog= """primers.txt will be used to highlight beads if primers_ecovomp.txt is not provided. """)
group1 = parser.add_argument_group('First Models', 'Parameters of the first models')
group2 = parser.add_argument_group('Second Models', 'Parameters of the second models')
group1.add_argument("data_dir", action="store",help='Directory with the 4C files of the first modeling')
group1.add_argument("prefix", action="store",help='Name of the models')
group1.add_argument("VHiC", action="store",help='Virtual Hi-C of the first models')
group1.add_argument("distance", type=int, action="store",help='Maximum distance used in the first models')
group1.add_argument("--fragments_in_each_bead", type= int, default=0, dest="fragments_in_each_bead" ,action="store",help='Number of fragments that will be represented with each bead in the first model to compare')

group2.add_argument("prefix2", action="store",help='Name of the other models')
group2.add_argument("VHiC2", action="store",help='Virtual Hi-C of the other models')
group2.add_argument("distance2", type=int, action="store",help='Maximum distance used in the other models')
group2.add_argument("--fragments_in_each_bead2", type= int, default=0, dest="fragments_in_each_bead2" ,action="store",help='Number of fragments that will be represented with each bead in the second model to compare')
group2.add_argument("data_dir2", action="store",help='Directory with the 4C files of the second modeling')

parser.add_argument("--storage_dir", action="store",default=working_dir, dest="storage_dir",help='location where the comparison pdf will be generated')
parser.add_argument("--maximum_hic_value",type=float,  action="store",default=1.0, dest="maximum_hic_value",help='The maximum value to plot in the virtual Hi-C comparison')


args = parser.parse_args()
print args

matrix_path = args.VHiC
matrix_path2 = args.VHiC2
storage_dir = args.storage_dir
prefix = args.prefix
prefix2 = args.prefix2
data_dir = args.data_dir
data_dir2 = args.data_dir2
WINDOW = args.fragments_in_each_bead
WINDOW2 = args.fragments_in_each_bead2
max_distance = args.distance
max_distance2 = args.distance2
maximum_hic_value= args.maximum_hic_value

### FIRST VHIC TO COMPARE

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
file_names = primers.keys()
files = [data_dir+f for f in file_names]

comp_primers = {}
try:
    primers_file = open (data_dir+"primers_evocomp.txt", 'r')
    for line in primers_file:
        m = re.search('([^\s\t]+).*chr\w+:(\d+)', line)
        try:
            comp_primers[m.group(1)] = int(m.group(2))
        except:
			break
except IOError:
    print "\nError: File "+ data_dir+ " primers_evocomp.txt does not appear to exist. Using primers.txt to paint positions in the virtual Hi-C\n"
    primers_file = fileCheck(data_dir+"primers.txt")
    for line in primers_file:
        m = re.search('([^\s\t]+).*chr\w+:(\d+)', line)
        try:
            comp_primers[m.group(1)] = int(m.group(2))
        except:
            break

for k,v in comp_primers.iteritems():
	print "Viewpoint:{}\tposition:{}".format(k,v)
	viewpoint_positions.append(v)
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
viewpoints = calculate_fragment_number(viewpoint_positions,files[0])
n_viewpoints = len(viewpoints)

#default, we want 100 beads in each model
if window == 0:
	window = int(number_of_fragments / 100)
name_of_fragments = comp_primers.keys()
gene_names = [x[:10] for x in name_of_fragments]

### SECOND VHIC TO COMPARE


# get the name and position from primers.txt
#primers.txt:  name chrN:position
primers = {}
viewpoint_positions = []
primers_file = fileCheck(data_dir2+"primers.txt")
for line in primers_file:
	m = re.search('([^\s\t]+).*chr\w+:(\d+)', line)
	try:
		primers[m.group(1)] = int(m.group(2))
	except:
		break
file_names = primers.keys()
files = [data_dir+f for f in file_names]

comp_primers = {}
try:
    primers_file = open (data_dir+"primers_evocomp.txt", 'r')
    for line in primers_file:
        m = re.search('([^\s\t]+).*chr\w+:(\d+)', line)
        try:
            comp_primers[m.group(1)] = int(m.group(2))
        except:
			break
except IOError:
    print "\nError: File "+ data_dir+ " primers_evocomp.txt does not appear to exist. Using primers.txt to paint positions in the virtual Hi-C\n"
    primers_file = fileCheck(data_dir+"primers.txt")
    for line in primers_file:
        m = re.search('([^\s\t]+).*chr\w+:(\d+)', line)
        try:
            comp_primers[m.group(1)] = int(m.group(2))
        except:
            break

for k,v in comp_primers.iteritems():
	print "Viewpoint:{}\tposition:{}".format(k,v)
	viewpoint_positions.append(v)
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
viewpoints2 = calculate_fragment_number(viewpoint_positions,files[0])
n_viewpoints2 = len(viewpoints)

#default, we want 100 beads in each model
if window == 0:
	window = int(number_of_fragments / 100)
name_of_fragments = comp_primers.keys()
gene_names2 = [x[:10] for x in name_of_fragments]
    


if n_viewpoints != n_viewpoints2:
    print "\nFragments to compare between {} and {} are different. Comparing {} and {} fragments. Check config files.".format(prefix,prefix2,len(viewpoints),len(viewpoints2))
    sys.exit()
viewpoints_ticks = [c+0.5 for c in viewpoints] #to match the gene_names in the matrix Since the ticks don't match with the heatmap.
matrix = np.zeros((n_viewpoints,n_viewpoints))
matrix2 = np.zeros((n_viewpoints,n_viewpoints))
matrix_final = np.zeros((n_viewpoints,n_viewpoints))
print "\nBeads to compare from first region: {}".format(viewpoints)
print "Beads to compare from second region: {}".format(viewpoints2)

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
        if i != j:
            array1.append(matrix[i][j])
for i in range(n_viewpoints):
    for j in range(n_viewpoints):
        if i != j:
            array2.append(matrix2[i][j])

print "\nCorrelation between both regions: (Type, correlation, P-value)"
print "pearson: "+str(pearsonr(array1,array2))
print "spearman: "+str(spearmanr(array1,array2))

print "Generating matrix to plot..."     
fig = plt.figure()
plt.title("Conserved regions vhic comparison")
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

pp = PdfPages('{}{}_vs_{}_evocomp.pdf'.format(storage_dir,prefix,prefix2))
pp.savefig(fig)
pp.close()
print "-------\nEvocomp.pdf shows in each matrix triangle the contact map between the conserved beads for each region."
print '{}{}_vs_{}_evocomp.pdf written'.format(storage_dir,prefix,prefix2)
#Distance between #1 marker 1  and #10 marker 1 : 2203.213

from matplotlib.colors import LinearSegmentedColormap
vmax = 1.0

#green_plot
#cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'white'),(0.35 / vmax, 'white'),(0.5 / vmax, 'green'),(0.65 / vmax, 'white'),(1 / vmax, 'white')])

#mut_comp
#cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'blue'),(0.34 / vmax, 'blue'),(0.35 / vmax, 'white',(0.5 / vmax, 'white')),(0.65 / vmax, 'white'),(0.66 / vmax, 'red'),(1 / vmax, 'red')])
cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'blue'),(0.4 / vmax, 'white'),(0.6 / vmax, 'white'),(1 / vmax, 'red')])

#white_black
#cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'black'),(0.5 / vmax, 'white'),(1 / vmax, 'black')])


fig = plt.figure()
plt.title("Similarity between conserved regions vhic")
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

pp = PdfPages('{}{}_vs_{}_evocomp_diff.pdf'.format(storage_dir,prefix,prefix2))
pp.savefig(fig)
pp.close()
print "-------\nEvocomp_diff shows the difference between both half matrices."
print '{}{}_vs_{}_evocomp_diff.pdf writen'.format(storage_dir,prefix,prefix2)
            
