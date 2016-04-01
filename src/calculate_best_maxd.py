#!/usr/bin/python

############# code that evaluates all the models with different distances and gives you which distance is the optimum

import re
import os
import sys
import subprocess
import numpy as np
import ConfigParser
#for each model (50 normally) we will get the length of the chromatin 

number_of_arguments = len(sys.argv)
if number_of_arguments != 2: 
    print "Not enought parameters. Config file is required. You passed: ",sys.argv[1:]
    sys.exit()
ini_file = sys.argv[1]

#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    prefix = config.get("ModelingValues", "prefix")
    WINDOW = float(config.get("ModelingValues", "WINDOW"))
    NFRAGMENTS = int(config.get("ModelingValues", "NFRAGMENTS"))
    NFRAGMENTS = int(NFRAGMENTS/WINDOW)
    working_dir = config.get("ModelingValues", "working_dir")
    min_dist = float(config.get("Pre-ModelingValues", "min_dist"))
    max_dist = float(config.get("Pre-ModelingValues", "max_dist"))
    dist_bins = int(config.get("Pre-ModelingValues", "dist_bins"))
    number_of_models = int(config.get("Pre-ModelingValues", "number_of_models"))

except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()

if not os.path.exists("{}data/{}".format(working_dir, prefix)):
    try:
        os.makedirs("{}data/{}".format(working_dir, prefix))
    except:
        print "\nError creating the data and {} directories.".format(prefix)
        e = sys.exc_info()[1]
        print e
        sys.exit()
    
results_path = "{}data/{}/{}_best_maxd_results.txt".format(working_dir,prefix,prefix)
aux_file = "get_genome_length.py"
number_of_spheres = NFRAGMENTS - 1

print "!! NOTE !! remember that we need models with 0.1 and -0.1 of uZ and lZ for the best calculation."
with open (results_path,"w") as output_results:
    for maxd in np.arange(min_dist,max_dist+1,dist_bins):
        root = "{}data/{}/{}_output_0.1_-0.1_{}/".format(working_dir,prefix,prefix,maxd)
        all_distances = []
        for i in range(number_of_models):
            ###### we get the lengths of all models
            with open (aux_file,'w') as output:
                output.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"{}\")\n".format(root))
                output.write("rc(\"open {}{}.py\")\n".format(prefix,i))
                for j in range (number_of_spheres):
                    output.write("rc(\"distance #"+str(j)+" #"+str(j+1)+"\")\n")
            distance_output = subprocess.check_output(["chimera", "--nogui", aux_file])
            ## reformat the output and read the distances
            #Distance between #297:1@ and #298:1@: 1131.491
            distance_sum = 0
            string = ""
            lista = []
            for line2 in distance_output:
                string = string + line2
                if line2 == "\n":
                    lista.append(string)
                    string = ""
            for line2 in lista:
                distance = re.search(r'Distance between',line2)
                if distance:
                    distance = float(line2.split(' ')[5])
                    distance_sum = distance_sum + distance
            #print ("model {} distance = {}").format(i,distance_sum)
            all_distances.append(distance_sum)
        #print all_distances
        size = np.mean(all_distances)
        #print "{}: {}".format(root,size)
        output_results.write("With max distance {}: {}A Equivalent to a genome of {} Mbp\n".format(maxd,size,size/0.0846/1000000)) #in Mbp
        print "With max distance {}: {}A Equivalent to a genome of {} Mbp".format(maxd,size,size/0.0846/1000000)
if os.path.isfile(aux_file):
    os.remove(aux_file) 
    os.remove(aux_file+"c")   

print "Results writen in: {}".format(results_path)
