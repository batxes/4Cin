#!/usr/bin/python

import sys, re, os
import collections
import ConfigParser

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
####
if len(sys.argv) < 2:
    print "Usage: prepare_data.py config_file 4c-seq_files. Files need to be in this format: \nchromosome start_fragment end_fragment score"
    sys.exit()
frag_dict = {}
for i in sys.argv[1:]:
    fourc_file = fileCheck(i)
    for line in fourc_file:
        values = line.split()
        if len(values) != 4:
            continue
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
        try:
            line = fourc_file.readline()
            values = line.split()
            if len(values) != 4 and len(values) != 0:
                continue
            line_n += 1
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
        except:
            #if we run out of lines, we have to populate them until we have the same length as the biggest file
            output.write("{}\t{}\t{}\t0.0\n".format(chrom,k,v))

sys.exit()
# read 1 of the files and set in the config file the locus_size, data_dir and file_names
fourc_file = fileCheck(sys.argv[2]+"_modified")
start = 0
number_of_fragments = 0
for line in fourc_file:
    values = line.split()
    if len(values) != 4:
        continue
    chrom = values[0]
    if start == 0:
        start = int(values[1])
    end = int(values[2])
    number_of_fragments += 1


data_dir = sys.argv[2].split("/")
data_dir = data_dir[:-1]
data_dir = "/".join(data_dir)
data_dir = os.path.abspath(data_dir)

file_names = []
for i in sys.argv[2:]:
    file_names.append(i.split("/")[-1]+"_modified")

config = ConfigParser.SafeConfigParser()
config.read(ini_file)
try:
    config.set("Pre-Modeling", "locus_size",str((end-start)/1000000.0)) #in Mb
    config.set("Modeling", "number_of_fragments",str(number_of_fragments))
    config.set("Modeling", "data_dir",str(data_dir))
    config.set("Modeling", "file_names",",\n\t".join(file_names))
    with open(ini_file,"w+") as configfile:
        config.write(configfile)

except: 
    print "\nError writing the configuration file.\n"
    print sys.exc_info()
    sys.exit()

print "\nFiles were prepared."
print "{} has been updated with locus_size, data_dir, file_names and number_of_fragments\n".format(ini_file)



