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
    number_of_models = int(config.get("ModelingValues", "number_of_models"))
    max_dist = int(config.get("ModelingValues", "max_dist"))
    max_z = float(config.get("ModelingValues", "max_z"))
    min_z = float(config.get("ModelingValues", "min_z"))
    number_of_cpu = int(config.get("ModelingValues", "number_of_cpu"))
    prefix = config.get("ModelingValues", "prefix")
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()


for cpu in range(number_of_cpu):
    if mode == "/bin/bash":
        print("{} run_genome.sh {} {} {} {} {} True &".format(mode,min_z,max_z,max_dist,cpu*number_of_models,ini_file))
    if mode == "qsub":
        print("{} run_genome.sh {} {} {} {} {} True".format(mode,min_z,max_z,max_dist,cpu*number_of_models,ini_file))

if mode == "/bin/bash":
    system(wait)



