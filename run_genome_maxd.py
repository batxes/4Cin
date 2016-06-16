#!/usr/bin/python

import sys
import os
import re
import ConfigParser


number_of_arguments = len(sys.argv)
if number_of_arguments != 3:  
    print "Not enought parameters. Config_file and run_mode are required. You passed: ",sys.argv[1:]
    print " -Config_file: Configuration filemax_dist."
    print " -run_mode: '/bin/bash', 'qsub'"
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    ini_file = sys.argv[1]
    mode = sys.argv[2]

#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    number_of_models = int(config.get("Pre-ModelingValues", "number_of_models"))
    min_dist = int(config.get("Pre-ModelingValues", "min_dist"))
    max_dist = int(config.get("Pre-ModelingValues", "max_dist"))
    dist_bins = int(config.get("Pre-ModelingValues", "dist_bins"))
    prefix = config.get("ModelingValues", "prefix")
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()


for dist in range(min_dist,max_dist+dist_bins,dist_bins):
    if mode == "/bin/bash":
        os.system("{} run_genome.sh 0.1 -0.1 {} 0 {} False &".format(mode,dist,ini_file))
        print("{} run_genome.sh 0.1 -0.1 {} 0 {} False &".format(mode,dist,ini_file))
    if mode == "qsub":
        os.system("{} run_genome.sh 0.1 -0.1 {} 0 {} False".format(mode,dist,ini_file))
        print("{} run_genome.sh 0.1 -0.1 {} 0 {} False".format(mode,dist,ini_file))
if mode == "/bin/bash":
    system(wait)



