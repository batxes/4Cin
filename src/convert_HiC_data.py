#!/usr/bin/python

#script that takes the real hi c data and converts it to distance_matrix type data to use it with TADs_multi.py

#argument1: file
#argument2: bins

import sys
import numpy as np

resolution = 1 #downgrade resolution data by number

if len(sys.argv) != 3:
    print "Not enough arguments: It needs the file to convert and the number of bins between fragments"
    sys.exit()
else:
    hic_file = sys.argv[1]
    bins = int(sys.argv[2])


fragment_list = []
with open(hic_file,"r") as stdin:
    smallest = 0
    biggest = 0
    for line in stdin:
        values = line.split("\t")
        if smallest == 0:
            smallest = int(values[0])
        if values[0] > biggest:
            biggest = int(values[0])

for fragment in range(smallest,biggest+1,bins):
    fragment_list.append(fragment)
size_old = len(fragment_list)

stdout = open (hic_file+"_modified","w")
with open(hic_file,"r") as stdin:
    for line in stdin:
        values = line.split("\t")
        stdout.write("{},{},{}".format(fragment_list.index(int(values[0])),fragment_list.index(int(values[1])),values[2]))

stdout.close()

#downgrade or set the from and to bins straight
print size_old
matrix_old = np.zeros((size_old,size_old))
with open (hic_file+"_modified") as stdin:
    for line in stdin:
        values = line.split(",")
        from_ = int(values[0])
        to_ = int(values[1])
        score_ = float(values[2])
        matrix_old[from_][to_] = score_
        matrix_old[to_][from_] = score_
size_new = int(size_old/resolution)
matrix_new = np.zeros((size_new,size_new))
print matrix_old
print size_new
stdout = open (hic_file+"_modified_lowres","w")
index_i = 0
for i in range(0,size_new):
    index_j = 0
    for j in range(0,size_new):
        merged = np.sum(matrix_old[index_i:index_i+resolution,index_j:index_j+resolution])
        matrix_new[i][j] = merged
        matrix_new[j][i] = merged
        index_j += resolution
    index_i += resolution
print matrix_new
for i in range(size_new):
    for j in range(size_new):
        if j >= i:
            stdout.write("{},{},{}\n".format(i,j,matrix_new[i][j]))
stdout.close()





