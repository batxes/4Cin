#!/usr/bin/python

# script to run modeling in different batches, so we can run models in parallel
import sys
import os
import re
import ConfigParser
import subprocess

number_of_arguments = len(sys.argv)
if number_of_arguments != 3:  
    print "Not enought parameters. Config_file and run_mode are required. You passed: ",sys.argv[1:]
    print " -Config_file: Configuration filemax_dist."
    print " -run_mode: 'local', 'qsub', 'sbatch'"
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    ini_file = sys.argv[1]
    mode = sys.argv[2]

#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    number_of_models = int(config.get("Modeling", "number_of_models"))
    max_dist = int(config.get("Modeling", "max_dist"))
    max_z = float(config.get("Modeling", "max_zscore"))
    min_z = float(config.get("Modeling", "min_zscore"))
    number_of_cpus = int(config.get("Modeling", "number_of_cpus"))
    number_of_models = number_of_models / number_of_cpus
    prefix = config.get("Modeling", "prefix")
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()

local_processes = []
for cpu in range(number_of_cpus):
    if mode == "local":
        p = subprocess.Popen(['python','src/run_modeling.py',str(max_z),str(min_z),str(max_dist),str(cpu*number_of_models),str(ini_file),'True'])
        print("python src/run_modeling.py {} {} {} {} {} True &".format(mode,max_z,min_z,max_dist,cpu*number_of_models,ini_file))
        local_processes.append(p)
    if mode == "qsub":
        print("{} run_genome.sh {} {} {} {} {} True".format(mode,max_z,min_z,max_dist,cpu*number_of_models,ini_file))
        os.system("{} run_genome.sh {} {} {} {} {} True".format(mode,max_z,min_z,max_dist,cpu*number_of_models,ini_file))
    if mode == "sbatch":
        print("{} run_genome.slurm {} {} {} {} {} True".format(mode,max_z,min_z,max_dist,cpu*number_of_models,ini_file))
        os.system("{} run_genome.slurm {} {} {} {} {} True".format(mode,max_z,min_z,max_dist,cpu*number_of_models,ini_file))

if mode == "local":
    exit_codes = [p.wait() for p in local_processes]

print("\n\nWhen the jobs have finished, run 'python src/run_analysis.py {} {} {} {}' (default values)".format(sys.argv[1],200,max_dist/10,25))


