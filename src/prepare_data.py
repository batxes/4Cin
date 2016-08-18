#!/usr/bin/python

import sys, re
import collections

#############################################################################################################
# This code helps prepare the data for the modeling. Given the files, it adds 0's to the fragments that are
# not present. The files need to be only with "chromosome start_fragment end_fragment score" in each line.
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
#yolo
####
if len(sys.argv) < 2:
    print "Usage: prepare_data.py 4c-seq_files."
    sys.exit()

frag_dict = {}
for i in sys.argv[1:]:
    fourc_file = fileCheck(i)
    for line in fourc_file:
        values = line.split()
        chrom = values[0]
        start_frag = int(values[1])
        end_frag = int(values[2])
        if not start_frag in frag_dict:
            frag_dict[start_frag] = end_frag
ordered_dict = collections.OrderedDict(sorted(frag_dict.items()))	    

### now, take each file, and write a new one with the missing fragments
for i in sys.argv[1:]:
    line_offset = []
    offset = 0
    line_n = 0
    fourc_file = fileCheck(i)
    for line in fourc_file: #we generate an offset, so we can go to previous line
        line_offset.append(offset)
        offset += len(line)
    fourc_file.seek(0)
    output = open(i+"_modified", "w")
    for k,v in ordered_dict.iteritems():
        line = fourc_file.readline()
        line_n += 1
        values = line.split()
        chrom = values[0]
        start_frag = int(values[1])
        end_frag = int(values[2])
        score = float(values[3])
        if start_frag == k:
            output.write("{}\t{}\t{}\t{}\n".format(chrom,start_frag,end_frag,score))
        else:
            output.write("{}\t{}\t{}\t0.0\n".format(chrom,k,v))
            line_n -= 1
            fourc_file.seek(line_offset[line_n])





