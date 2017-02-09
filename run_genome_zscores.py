#!/usr/bin/python

# script that runs a small number of modeling rounds with different Z-score values.
import sys
import os
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
    number_of_models = int(config.get("Pre-Modeling", "number_of_models"))
    from_zscore= int(10*float(config.get("Pre-Modeling", "from_zscore")))
    to_zscore= int(10*float(config.get("Pre-Modeling", "to_zscore")))
    zscore_bins = int(10*float(config.get("Pre-Modeling", "zscore_bins")))
    dist = int(config.get("Modeling", "max_dist"))
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()

print from_zscore, to_zscore, zscore_bins
local_processes = []
for z_min in range(from_zscore,to_zscore+zscore_bins,zscore_bins):
    for z_max in range(from_zscore,to_zscore+zscore_bins,zscore_bins):
        if mode == "local":
            p = subprocess.Popen(['/usr/bin/python', 'src/run_modeling.py', str(float(z_min)/10) ,str(float(z_max)/-10), str(dist),' 0' ,str(ini_file) ,'False'])
            print("/usr/bin/python src/run_modeling.py {} {} {} 0 {} False".format(float(z_min)/10,float(z_max)/-10,dist,ini_file))
            local_processes.append(p)
        if mode == "qsub":
            os.system("{} run_genome.sh {} -{} {} 0 {} False".format(mode,float(z_min)/10,float(z_max)/10,dist,ini_file))
            print("{} run_genome.sh {} -{} {} 0 {} False".format(mode,float(z_min)/10,float(z_max)/10,dist,ini_file))
        if mode == "sbatch":
            os.system("{} run_genome.slurm {} -{} {} 0 {} False".format(mode,float(z_min)/10,float(z_max)/10,dist,ini_file))
            print("{} run_genome.slurm {} -{} {} 0 {} False".format(mode,float(z_min)/10,float(z_max)/10,dist,ini_file))
if mode == "local":
    exit_codes = [p.wait() for p in local_processes]
print("When the jobs have finished, run 'python src/calculate_best_zscores.py {} True'. Set last variable to False if fails.".format(sys.argv[1]))




