#!/usr/bin/python

# Script that runs small rounds of modeling with different Max distances

import sys
import os
import re
import ConfigParser
import subprocess
from multiprocessing import Process, Lock, Pool, current_process


def worker(instructions):
    p = subprocess.Popen(instructions)
    p.wait()

number_of_cpu = 2
p = Pool(number_of_cpu)

number_of_arguments = len(sys.argv)
if number_of_arguments != 2:  
    print "Not enought parameters. Config_file and run_mode are required."
    print " -Config_file: config.ini."
    sys.exit()
if len(sys.argv) > 0:  #if we pass the arguments (in the cluster)
    ini_file = sys.argv[1]

#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    number_of_models = int(config.get("Pre-Modeling", "number_of_models"))
    from_dist = int(config.get("Pre-Modeling", "from_dist"))
    to_dist = int(config.get("Pre-Modeling", "to_dist"))
    dist_bins = int(config.get("Pre-Modeling", "dist_bins"))
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()

execute = []
for dist in range(from_dist,to_dist+dist_bins,dist_bins):
    instructions = ['/usr/bin/python', 'src/run_modeling.py', '0.1' ,'-0.1', str(dist),' 0' ,str(ini_file) ,'False']
    execute.append(instructions)
p.map(worker,execute)

print("\n\nWhen the jobs have finished, run 'python src/calculate_best_maxd.py {}'".format(sys.argv[1]))


