#!/usr/bin/python

import sys
import os
import re
from collections import defaultdict
import operator
import shutil
import ConfigParser
from os import listdir
from os.path import isfile, join
import pysam

number_of_arguments = len(sys.argv)
if number_of_arguments != 5: #Or all parameters, or no parameters 
    print "Not enought parameters. uZ, lZ, maxD and config_file are required. You passed: ",sys.argv[1:]
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    uZ = float(sys.argv[1])
    lZ = float(sys.argv[2])
    y2 = float(sys.argv[3])
    ini_file = sys.argv[4]

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
    
    NFRAGMENTS = int(config.get("ModelingValues", "NFRAGMENTS"))
    NFRAGMENTS = int(NFRAGMENTS/WINDOW)
    
    number_of_models = int(config.get("ModelingValues", "number_of_models"))
    working_dir = config.get("ModelingValues", "working_dir")


    subset = int(config.get("AnalysisValues", "subset"))
    std_dev = int(config.get("AnalysisValues", "std_dev"))
    jump = number_of_models
    cut_off_percentage = int(config.get("AnalysisValues", "cut_off_percentage"))

    atac_path = config.get("Painting","Atac_path")
    
    
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()


# create bed file
bamhandle = pysam.AlignmentFile(atac_path,"rb")
with open ("bed_file","w") as stdout:
    with open (files[0],"r") as stdin:
        for line in stdin:
            values = line.split("\t")
            read_count = bamhandle.count(values[0],values[1],values[2]) #chrm, start, end
            stdout.write("{}\t{}\t{}\t{}\n".format(values[0],values[1],values[2],read_count))






