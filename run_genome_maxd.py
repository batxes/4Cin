#!/usr/bin/python

import sys
import os
import re
import ConfigParser
import subprocess

number_of_arguments = len(sys.argv)
if number_of_arguments != 3:  
    print "Not enought parameters. Config_file and run_mode are required."
    print " -Config_file: config.ini."
    print " -run_mode: 'local', 'qsub', 'sbatch'"
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    ini_file = sys.argv[1]
    mode = sys.argv[2]

#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    number_of_models = int(config.get("Pre-ModelingValues", "number_of_models"))
    from_dist = int(config.get("Pre-ModelingValues", "from_dist"))
    to_dist = int(config.get("Pre-ModelingValues", "to_dist"))
    dist_bins = int(config.get("Pre-ModelingValues", "dist_bins"))
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()

local_processes = []
for dist in range(from_dist,to_dist+dist_bins,dist_bins):
    if mode == "local":
        p = subprocess.Popen(['/usr/bin/python', 'src/GenomeModeling.py', '0.1' ,'-0.1', str(dist),' 0' ,str(ini_file) ,'False'])
        print("/usr/bin/python src/GenomeModeling.py 0.1 -0.1 {} 0 {} False".format(dist,ini_file))
        local_processes.append(p)
    if mode == "qsub":
        os.system("{} run_genome.sh 0.1 -0.1 {} 0 {} False".format(mode,dist,ini_file))
        print("{} run_genome.sh 0.1 -0.1 {} 0 {} False".format(mode,dist,ini_file))
    if mode == "sbatch":
        os.system("{} run_genome.slurm 0.1 -0.1 {} 0 {} False".format(mode,dist,ini_file))
        print("{} run_genome.slurm 0.1 -0.1 {} 0 {} False".format(mode,dist,ini_file))
if mode == "local":
    exit_codes = [p.wait() for p in local_processes]

print("\n\nWhen the jobs have finished, run 'python src/calculate_best_maxd.py {}'".format(sys.argv[1]))


