#!/usr/bin/python

#script that takes the real hi c data and converts it to distance_matrix type data to use it with TADs_multi.py

#argument1: file
#argument2: bins

import sys

if len(sys.argv) != 3:
    print "Not enough arguments: It needs the file to convert and the number of bins between fragments"
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

stdout = open (hic_file+"_modified","w")
with open(hic_file,"r") as stdin:
    for line in stdin:
        values = line.split("\t")
        stdout.write("{},{},{}".format(fragment_list.index(int(values[0])),fragment_list.index(int(values[1])),values[2]))

stdout.close()
