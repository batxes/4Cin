#!/usr/bin/python

import os
import sys, re
import numpy as np
from math import fabs
import ConfigParser
from scipy.stats.stats import spearmanr
from data_manager import calculateNWindowedDistances


def calculate_heatdifference(path, n_files_inside,files,prefix):        

    #FIRST CALCULATE OUR MODELS HEATMAP
    y2 = re.split('_',path)[-1] #I get 3000.0, now I take out .0 and convert to int
    y2 = int(re.split('\.',y2)[0])
    all_data = []
    number_of_reads = 0
    for i in range(n_files_inside):
        all_modified_arrays = []
        with open("{0}/{1}{2}.txt".format(path,prefix,i),"r") as f: #in 2.7 and newer versions I dont have to set indices

            #f = open(path+"/"+prefix+""+str(i)+".txt", "r")
            five_arrays = []
            for line in f:
                array = re.split('\t',line)
                reads = np.genfromtxt(array)
                five_arrays.append(reads)
                number_of_reads = len(reads)
                #the data is independent so get the values for each array in five_arrays
            for array in five_arrays:

                # Min distance = 0 value
                # Max distance = 100 value
                x1 = min(array)
                x2 = max(array)
                #y2 = 
                y1 = 300  
                slope = (y2-y1) / (x2-x1)
                array_modified = [slope*(read-x1)+y1 for read in array]

                all_modified_arrays.append(array_modified)
            all_data.append(all_modified_arrays)
       
    #calculate mean of all arrays
    mean_all_data = []
    # first we will calculate the mean for a gen_array, so we need to to this 5 times.
    for i in range(len(files)): #5 genes
        mean_one_gene_array = []
        for j in range(number_of_reads):
            value = 0
            for k in range(len(all_data)): #n_files_inside times
                current_array = all_data[k]
                value = value + current_array[i][j]
            mean = value/len(all_data)
            mean_one_gene_array.append(mean)
        mean_all_data.append(mean_one_gene_array)

    if plot:
        fig = plt.figure(figsize=(10,10))   
        ax = plt.subplot(2,1,2)
        z = np.array(mean_all_data)
        c = plt.pcolor(z,cmap=plt.cm.terrain_r)
        plt.colorbar()
        ax.set_yticks(np.arange(z.shape[1])+0.5, minor=False)
        plt.axis([0,z.shape[1],0,z.shape[0]])
        labels = [(x.split("/")[-1])[:15] for x in files]
        ax.set_yticklabels(labels)
        plt.xlabel("Beads")
    #     plt.xlabel("Genomic Position")

    #NOW CALCULATE THE 4C DATA'S HEATMAP (WITHOUT APLLYING LOG)
    HEAT_MAP_DATA, HEATMAP_DATA_LOG= calculateNWindowedDistances(fragments_in_each_bead,0,0,y2,files,False,True) #stored in HEATMAP_DATA_LOG
    
    heatmap_data_modified = []


    for array in HEAT_MAP_DATA:
    # without log
    # max reads = 0 distance
        x1 = max(array)
        x2 = min(array)
        y1 = 300  
        slope = (y2-y1) / (x2-x1)
        array_modified = [slope*(read-x1)+y1 for read in array]
        heatmap_data_modified.append(array_modified)
    if plot: 
        plt.title("Top: Raw data reads per bear. \nBottom: Average distance between beads of the models.")
        ax = plt.subplot(2,1,1)
        z = np.array(heatmap_data_modified)
        c = plt.pcolor(z,cmap=plt.cm.terrain_r)

        plt.colorbar()
        ax.set_yticks(np.arange(z.shape[1])+0.5, minor=False)
        plt.axis([0,z.shape[1],0,z.shape[0]])
        labels = [(x.split("/")[-1])[:15] for x in files]
        ax.set_yticklabels(labels)
        plt.subplots_adjust(bottom=0.1, right=0.999, top=0.9, left=0.2)
    #     plt.xlabel("Genomic Position")
        plt.savefig('{}_heatmap.png'.format(path))
        plt.close('all')


    #CALCULATE THE DIFFERENCE
    array2 = []
    for i in (mean_all_data):
        for j in i:
            array2.append(j)
    array1 = []
    for i in (heatmap_data_modified):
        for j in i:
            array1.append(j)

    #value = 0
    #for i in range(len(heatmap_data_modified)):
    #    for j in range(len(heatmap_data_modified[i])):
    #        # the difference will be relative
    #        # models with bigger MAX DIST are more likely to have bigger difference
    #        if mean_all_data[i][j] != 0.0:
    #            difference = fabs(mean_all_data[i][j]/y2-heatmap_data_modified[i][j]/y2)
    #            value = value + difference            
    #print "Value for "+path+" is: "+str(value)
    spearman_value = spearmanr(array1,array2)[0]
    print "Spearman correlation for {}: {}".format(path,str(spearman_value))

    #print "Spearman: "+str(spearmanr(heatmap_data_modified,mean_all_data))

    return spearman_value
                
                
##### MAIN ######
number_of_arguments = len(sys.argv)

if number_of_arguments != 3: #Or all parameters, or no parameters 
    print "Not enought parameters. Config file  and plotting 'True/False' are required. You passed: ",sys.argv[1:]
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    ini_file = sys.argv[1]
    if sys.argv[2] == "True":
        plot = True
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pylab as plt
    elif sys.argv[2] == "False":
        plot = False
    else:
        print "\nError, set True/False for the plotting.\n"
        sys.exit()
    
#read the config file
config = ConfigParser.SafeConfigParser()
try:
    config.read(ini_file)
    prefix = config.get("ModelingValues", "prefix")
    maxD = int(config.get("ModelingValues", "max_dist"))
    fragments_in_each_bead = float(config.get("ModelingValues", "fragments_in_each_bead"))
    data_dir = config.get("ModelingValues", "data_dir")
    file_names = config.get("ModelingValues", "file_names")
    file_names = re.sub('[\n\s\t]','',file_names)
    file_names = file_names.split(",")
    files = [data_dir+f for f in file_names]
    working_dir = config.get("ModelingValues", "working_dir")
    number_of_models = int(config.get("Pre-ModelingValues", "number_of_models"))
    from_zscore = float(config.get("Pre-ModelingValues", "from_zscore"))
    to_zscore = float(config.get("Pre-ModelingValues", "to_zscore"))
    zscore_bins = float(config.get("Pre-ModelingValues", "zscore_bins"))
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()
    
results_path = "{}data/{}/{}_heatmap_difference_results.txt".format(working_dir,prefix,prefix)
       
with open (results_path,"w") as output_results:
    all_scores = []
    best_uZ = 0
    best_lZ = 0
    best_score = 0.0
    for uZ in np.arange(from_zscore,to_zscore+0.01,zscore_bins):
        for lZ in np.arange(-from_zscore, -to_zscore-0.01, -zscore_bins):
            score = calculate_heatdifference(working_dir+"data/"+prefix+"/"+prefix+"_output_"+str(uZ)+"_"+str(lZ)+"_"+str(maxD),number_of_models,files,prefix)
            output_results.write(str(uZ)+","+str(lZ)+","+str(maxD)+"\t"+str(score)+"\n")
            all_scores.append(score)
            if score > best_score :
                best_uZ = uZ
                best_lZ = lZ
                best_score = score
    #output_results.write("MIN: {}".format(min(all_scores)))   
    output_results.write("Max: {}".format(max(all_scores)))   
    #print min(all_scores)
try:
    config.set("ModelingValues", "max_zscore",str(best_uZ))
    config.set("ModelingValues", "min_zscore",str(best_lZ))
    with open(ini_file,"w+") as configfile:
        config.write(configfile)
except:
    print "\nError writing the configuration file.\n"
    print sys.exc_info()
    sys.exit()

print "{} has been updated".format(ini_file)

print "Best uZ: {}, Best lZ: {}".format(best_uZ,best_lZ)
if plot:
    print "\nFigures comparing raw data vs modeling were created in {}data/{}/".format(working_dir,prefix)

print "\nNow run python 'run_genome_sampling.py {} qsub,sbatch,local'".format(ini_file)
