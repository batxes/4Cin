#!/usr/bin/python

import sys
import re
import ConfigParser
import pysam
from colour import Color
import heapq
import matplotlib.cm  as cm

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
    viewpoints = [int(round(i/WINDOW)) for i in viewpoints]
    print viewpoints
    
    NFRAGMENTS_ALL = int(config.get("ModelingValues", "NFRAGMENTS"))
    NFRAGMENTS = int(NFRAGMENTS_ALL/WINDOW)
    
    number_of_models = int(config.get("ModelingValues", "number_of_models"))
    working_dir = config.get("ModelingValues", "working_dir")


    subset = int(config.get("AnalysisValues", "subset"))
    std_dev = int(config.get("AnalysisValues", "std_dev"))
    jump = number_of_models
    cut_off_percentage = int(config.get("AnalysisValues", "cut_off_percentage"))

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
    with open ("bed_file","w") as stdout:
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
        with open ("bed_file","w") as stdout:
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
with open ("bed_file","r") as stdin:
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
            print normalized_read
            counter = 0
            added_region = 0
            added_reads = 0
    if counter != WINDOW: #we add the min value to the last bead if it did not reach to Nfragments 
        normalized_read = added_reads/added_region
        bead_values.append(normalized_read)

from pylab import *
import matplotlib as mpl
import matplotlib.cm as cm
cmap = cm.Blues

norm = mpl.colors.Normalize(vmin=min(bead_values), vmax=max(bead_values))
#norm = mpl.colors.Normalize(vmin=0.01, vmax=0.04) #methylome
#norm = mpl.colors.Normalize(vmin=0.1, vmax=0.6) #atac-seq
m = cm.ScalarMappable(norm=norm, cmap=cmap)

with open("coloring.cmd","w") as colored_model:
    colored_model.write("open {}\n".format(model))
    for number in range(NFRAGMENTS):
        colored_model.write("color {} #{}\n".format(matplotlib.colors.rgb2hex(m.to_rgba(bead_values[number])),number))
        #print "bead: {} color:{} value:{}".format(number,matplotlib.colors.rgb2hex(m.to_rgba(bead_values[number])),bead_values[number])
    colored_model.write("shape tube #{}-{} radius 200 bandlength 10000".format(0,NFRAGMENTS))


print "Now, open coloring.cmd wich Chimera."





