#!/usr/bin/python

import sys, re, os
import collections
import matplotlib.pyplot as plt
#plt.style.use('ggplot')

#############################################################################################################
# This script takes the raw 4C-seq data. Then for each file it creates another one with some changes. For readcounts above "hit_threshold", it will call it hit, and then it will be calculated the ammount of hits in a window of "window".
# 
#
# Parameters: 4cfiles
#############################################################################################################

def fileCheck(f):
    try:
        f = open (f, 'r')
        return f
    except IOError:
        print "\nError: File "+ f +" does not appear to exist.\n"
        sys.exit()

#####
#MAIN
####

#common windows 25,51,101
#common hits 1, 10, 100
window = 25
hit_threshold = 1

show_plot = False


if len(sys.argv) < 4:
    print "Usage: prepare_data.py window hit_threshold 4c-seq_files. Files need to be in this format: \nchromosome start_fragment end_fragment score"
    sys.exit()
### now, take each file, and write a new one with the missing fragments
window = int(sys.argv[1])
hit_threshold = int(sys.argv[2])
print "Window = {}, Hit_threshold = {}.".format(window, hit_threshold)
for i in sys.argv[3:]:
    hit_percentage = []
    hit_list = []
    fourc_file = fileCheck(i)
    output = open(i+"_modified_W{}H{}".format(window,hit_threshold), "w")
    for line in fourc_file: 
        values = line.split()
        if float(values[3]) > hit_threshold:
            hit_list.append(1)
        else:
            hit_list.append(0)

    for j in range(len(hit_list)):
        if j <= int((window - 1)/2):
            pos = 0
        elif j >= len(hit_list) - int((window-1)/2):
            pos = int((window-1)/2)
        else:
            pos = j
        #print float(sum(hit_list[pos-int((window-1)/2):pos+int((window-1)/2)]))/window

        hit_percentage.append(float(sum(hit_list[pos-int((window-1)/2):pos+int((window-1)/2)]))/window)
    fourc_file = fileCheck(i)
    line_n = 0
    for line in fourc_file: 
        values = line.split()
        chrom = values[0]
        start_frag = int(values[1])
        end_frag = int(values[2])
        #print chrom, start_frag, end_frag, hit_percentage[line_n]
        output.write("{}\t{}\t{}\t{}\n".format(chrom,start_frag,end_frag,hit_percentage[line_n]))
        line_n += 1
    output.close()
    if show_plot:
        fig = plt.figure()
        bar_list = plt.bar(range(len(hit_percentage)),hit_percentage,width=0.5)
        plt.xlabel(i)
        plt.ylim(ymax=1,ymin=0)

        plt.show()
    print "Data generated in {}_modified_W{}H{}".format(i,window,hit_threshold)

