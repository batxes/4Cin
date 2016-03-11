#!/usr/bin/python

import sys, re
import matplotlib.pyplot as plt
import numpy as np
from math import fabs
import ConfigParser
#from variables import WINDOW, prefix, NFRAGMENTS, files, genes, hox_genes, zebrafish, amphioxus, mouse, bmp7
from normal_distribution import  calculateNWindowedDistances







def calculate_heatdifference(path, n_files_inside,names,files,prefix):        

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
           
        ax = plt.subplot(2,1,2)
        z = np.array(mean_all_data)
        c = plt.pcolor(z,cmap=plt.cm.terrain_r)
        plt.colorbar()
        ax.set_yticks(np.arange(z.shape[1])+0.5, minor=False)
        plt.axis([0,z.shape[1],0,z.shape[0]])
        ax.set_yticklabels(names)
    #     plt.xlabel("Genomic Position")

    #NOW CALCULATE THE 4C DATA'S HEATMAP (WITHOUT APLLYING LOG)
    HEAT_MAP_DATA, HEATMAP_DATA_LOG= calculateNWindowedDistances(WINDOW,0,0,y2,files,False,True) #stored in HEATMAP_DATA_LOG
    
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
        ax = plt.subplot(2,1,1)
        z = np.array(heatmap_data_modified)
        c = plt.pcolor(z,cmap=plt.cm.terrain_r)

        plt.colorbar()
        ax.set_yticks(np.arange(z.shape[1])+0.5, minor=False)
        plt.axis([0,z.shape[1],0,z.shape[0]])
        ax.set_yticklabels(names)
    #     plt.xlabel("Genomic Position")
        plt.show()



    #CALCULATE THE DIFFERENCE
    value = 0
    for i in range(len(heatmap_data_modified)):
        for j in range(len(heatmap_data_modified[i])):
            # the difference will be relative
            # models with bigger MAX DIST are more likely to have bigger difference
            if mean_all_data[i][j] != 0.0:
                difference = fabs(mean_all_data[i][j]/y2-heatmap_data_modified[i][j]/y2)

                value = value + difference            
                #if i == 1:
                #    print mean_all_data[i][j]
                #    print heatmap_data_modified[i][j]
                #    print "       {}      ####################################".format(value)
    print "Value for "+path+" is: "+str(value)
    return value
                
                
##### MAIN ######
number_of_arguments = len(sys.argv)

if number_of_arguments != 4 and number_of_arguments != 1: #Or all parameters, or no parameters 
    print "Not enought parameters. start_zscore, end_zscore, maxd, bins, plot, ini file are required. You passed: ",sys.argv[1:]
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    start_zscore = float(sys.argv[1])
    end_zscore = float(sys.argv[2])
    max_d = float(sys.argv[3])
    bins = float(sys.argv[4])
    ini_file = sys.argv[5]
    if sys.argv[6] == "True":
        plot = True
    else:
        plot = False
    
else: #if no arguments, set the default values
    start_zscore = 0.1 #upper bound Z-score
    end_zscore = 0.1 #lower bound Z-score 
    max_d = 6000.0  # Max distance BETWEEN bead
    bins = 0.1
    plot = True
    ini_file = "config.ini"
    
#read the config file
config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)
    
    prefix = config.get("ModelingValues", "prefix")
    
    WINDOW = float(config.get("ModelingValues", "WINDOW"))
    
    files = config.get("ModelingValues", "files")
    files = re.sub('[\n\s\t]','',files)
    files = files.split(",")    
    
    names = config.get("ModelingValues", "names")
    names = re.sub('[\n\s\t]','',names)
    names = names.split(",")   
    
    number_of_models = int(config.get("ModelingValues", "number_of_models"))
    
    working_dir = config.get("ModelingValues", "working_dir")
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()
    
results_path = "../data/{}_heatmap_difference_results.txt".format(prefix)
       
with open (results_path,"w") as output_results:
    all_scores = []
    best_uZ = 0
    best_lZ = 0
    last_score = 10000
    for uZ in np.arange(start_zscore,end_zscore+0.01,bins):
        for lZ in np.arange(-start_zscore, -end_zscore-0.01, -bins):
            score = calculate_heatdifference(working_dir+"data/"+prefix+"_output_"+str(uZ)+"_"+str(lZ)+"_"+str(max_d),number_of_models,names,files,prefix)
            output_results.write(str(uZ)+","+str(lZ)+","+str(max_d)+"\t"+str(score)+"\n")
            all_scores.append(score)
            if score < last_score :
                best_uZ = uZ
                best_lZ = lZ
    output_results.write("MIN: {}".format(min(all_scores)))   
    #print min(all_scores)
    print "Best uZ: {}, Best lZ: {}".format(best_uZ,best_lZ)
