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
from normal_distribution import  calculateNWindowedDistances

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
    
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()

root = "{}data/{}/{}_output_{}_{}_{}/".format(working_dir,prefix,prefix,uZ,lZ,y2)
score_file = "{}/score.txt".format(root)


pyfiles = [ f for f in listdir(root) if isfile(join(root,f)) and f.endswith(".py") ]
number_of_models = len(pyfiles)
try:
    os.remove(root+"score.txt")
except OSError:
    pass
scorefiles = [ f for f in listdir(root) if isfile(join(root,f)) and f.startswith("score") ]
number_of_score_files = len(scorefiles)







models = defaultdict(list) # dict: each model ahs a list of 2 values

# first we create a unified score.txt
with open (score_file,"w") as f:
    counter = 0
    for i in range(number_of_score_files):
        with open (root+"score"+str(counter)+".txt", "r") as f2:
            for line in f2:
                f.write(line)
        counter = counter + jump
        
# create the dictionary and populate it
with open (score_file, "r") as f:
    counter = 0
    for line in f:
        counter += 1
        model = []
        values = re.split("\t", line)
        number = int(values[0])
        score = float(values[1])
        model.append(score)
        models[number] = model
        if counter == number_of_models:
            break

# models = models[:number_of_models]    #take aonly the first ones 
        
reads_values,reads_weights,start_windows, end_windows = calculateNWindowedDistances(int(WINDOW),uZ,lZ, y2,files)


print "getting best {} models\n".format(subset)
analized_models = 0
ok_models = 0
for i in range(number_of_models):
    distances_in_model = []
    with open (root+prefix+str(i)+".txt","r") as f:
        for line in f:
            value = re.split("\t",line)
            distances_in_model.append(value)
#         print distances_in_model
    #EVALUATION
 
 
    not_fulfilled = 0
    total = 0
    for k in range(len(files)):

        values = reads_values[k] 
        for j in range(NFRAGMENTS):
            if j != viewpoints[k]:
                
                real_d = distances_in_model[k][j]
                 
                should_be_d = values[j] 
                if should_be_d != 0:
                    total += 1
                    if (should_be_d + std_dev < float(real_d)  or should_be_d - std_dev > float(real_d)):
                        not_fulfilled += 1
            #             print "restraint "+str(j)+"not fulfilled"
                        if (verbose == 3):
                            print "Restraint " +str(j)+"-"+str(viewpoints[k])+" is "+str(real_d)+" and should be "+str(should_be_d)+" +- "+str(std_dev)+". Difference: "+str(should_be_d-float(real_d))
#     print str(i)+"-> Not fulfilled restraints: "+str(not_fulfilled)+"/"+str(total),"%",str(not_fulfilled*100/(total))     
    fulfil_percentage = not_fulfilled*100/total
    print "not_fulfilled -> {}/{} : {}".format(not_fulfilled,total,fulfil_percentage)
    if fulfil_percentage < cut_off_percentage:
        models[i].append(not_fulfilled)
        ok_models += 1
    else:
        del models[i]
    analized_models += 1
    print "Percentage of models that fulfill the threshold: {}".format(100*ok_models/analized_models)
    print "{}/{}".format(ok_models,analized_models)
    #print "{} -> number of models in subset {}".format(i,len(models))  
# after poplating all and takign out the models out of the cout off, take the subset of models



#order the dictionary by score
sorted_models = sorted(models.items(), key=operator.itemgetter(1))
print "Number of models below cutoff: {}".format(len(sorted_models))

# store them in a folder
print "copying best {} models\n".format(subset)
storage_folder = working_dir+"data/"+prefix+"/"+prefix+"_final_output_"+str(uZ)+"_"+str(lZ)+"_"+str(y2)+"/" #the dir where the data will be saved
print storage_folder
if not os.path.exists(storage_folder): os.makedirs(storage_folder)   

models_subset = sorted_models [:subset]
for k in range(subset):
    
    i = models_subset[k][0]
    shutil.copyfile("{}{}{}.py".format(root,prefix,i), "{}{}{}.py".format(storage_folder,prefix,i) )
    shutil.copyfile("{}{}{}.txt".format(root,prefix,i), "{}{}{}.txt".format(storage_folder,prefix,i) )



# create the file to open in chimera
# superposition of the best models
print "Creating superposition of {} models\n".format(subset)
with open(working_dir+"data/"+prefix+"_superposition.py","w") as f:
    f.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\""+root+"\")\n")
    f.write("rc(\"open {}{}.py\")\n".format(prefix,models_subset[0][0]))
    for k in range(1,subset):
        i = models_subset[k][0]
#         print("rc(\"open {}{}.py\")\n".format(prefix,i))
#         print("rc(\"match #{}-{} #0-{}\")\n".format((k+1)*NFRAGMENTS,(k+1)*NFRAGMENTS+NFRAGMENTS-1,NFRAGMENTS-1))
        f.write("rc(\"open {}{}.py\")\n".format(prefix,i))
        f.write("rc(\"match #{}-{} #0-{}\")\n".format(k*NFRAGMENTS,k*NFRAGMENTS+NFRAGMENTS-1,NFRAGMENTS-1))

print "created in {}data/{}_superposition".format(working_dir,prefix)
