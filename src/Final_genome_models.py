#!/usr/bin/python


import re
import os
from os import listdir
from os.path import isfile, join
import subprocess
from itertools import combinations
import time
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from optparse import Values
import shutil
import sys
import ConfigParser

number_of_arguments = len(sys.argv)


if number_of_arguments != 4:             
    print "Not enought parameters. Models directory, matrix_file and config_file are required. You passed: ",sys.argv[1:]
    sys.exit()
if len(sys.argv) > 1:  #if we pass the arguments (in the cluster)
    root = sys.argv[1]
    matrix_file = sys.argv[2]
    ini_file = sys.argv[3]


config = ConfigParser.ConfigParser()
try:
    config.read(ini_file)

    WINDOW = float(config.get("ModelingValues", "WINDOW"))
    NFRAGMENTS = int(config.get("ModelingValues", "NFRAGMENTS"))
    NFRAGMENTS = int(NFRAGMENTS/WINDOW)
    working_dir = config.get("ModelingValues", "working_dir")
    root = working_dir+root
    
    viewpoints = config.get("ModelingValues", "viewpoints")
    viewpoints = re.sub('[\n\s\t]','',viewpoints)
    viewpoints = viewpoints.split(",")
    viewpoints = [ int(i) for i in viewpoints]
    viewpoints = [int(i/WINDOW) for i in viewpoints]
    genes = config.get("ModelingValues", "genes")
    genes = re.sub('[\n\s\t]','',genes)
    genes = genes.split(",")
    genes = [ int(i) for i in genes]
    genes = [int(i/WINDOW) for i in genes]

    
except:
    print "\nError reading the configuration file.\n"
    e = sys.exc_info()[1]
    print e
    sys.exit()

########### FIRST GET THE PDB MODELS

#pdb directory will be inside the final models directory
pdb_output = "{}/pdb_output/".format(root)
if not os.path.exists(pdb_output): os.makedirs(pdb_output)
write_pdb = "{}get_genome_pdbs.py".format(root)
models = []
with open(matrix_file, "r") as mtx:
    for line in mtx:
        models.append(re.split("\t", line)[0])

models = models[1:]

#testing with less models
models = models[:10]

# in chimera:
# open all files (half of matrix)
# match all files
# combine all files
# write the pdb file

counter = 1
with open (write_pdb,'w') as output:
    
    output.write("import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"{}\")\n".format(root))
    print "0 - {}".format(models[0])
    output.write("rc(\"open {}\")\n".format(models[0]))
    for model in models[1:]:
    # for model in models[-2:]:
        print "{} - {}".format(counter,model)
        output.write("rc(\"open {}\")\n".format(model))
        counter += 1       
    for model in range(len(models)-1):
        output.write("rc(\"match #{}-{} #0-{}\")\n".format((model+1)*NFRAGMENTS,(model+1)*NFRAGMENTS+NFRAGMENTS-1,NFRAGMENTS-1))
     
    start_id = len(models)*NFRAGMENTS    
    for model in range(len(models)):
        
        output.write("rc(\"combine #{}-{} newchainids False name combine modelId {}\")\n".format(model*NFRAGMENTS,(model*NFRAGMENTS+NFRAGMENTS-1),start_id))
        output.write("rc(\"write format pdb #{} {}{}.pdb\")\n".format(start_id,pdb_output,models[model][:-3])) #with -3 we take out the ".PY"
        start_id+=1
        #combine #0-210 newchainids False name combine modelId 211    
        
        #write format pdb #211 test.pdb
        
print "writting pdb-s... it can take like 30 minutes."        
distance_output = subprocess.check_output(["chimera", "--nogui", write_pdb])
print "Pdb's written. Calculating average model..."
os.remove(write_pdb)
            
         
########## NOW WE GET THE AVERAGE MODEL




color_grey = "#b333b333b333"
color_gene = "#ffffb3330000"



#get the pdb files 
pdbFiles = [ f for f in listdir(pdb_output) if isfile(join(pdb_output,f)) ]

#get the x y and z position of all beads of all models
all_models = []

for pdbFile in pdbFiles:
    one_model = []
    with open("{}{}".format(pdb_output,pdbFile), "r") as f:
        for line in f:
            values = re.search(r'HETATM\s+\d+\s+\*{4}\s+\d+\s{4}(.{8})(.{8})(.{8})',line)  
            if values:
                value_tuple = (float(values.group(1)),float(values.group(2)),float(values.group(3)))
                one_model.append(value_tuple)
    all_models.append(one_model)
    
mean_model = []
for bead in range(NFRAGMENTS):   
    lista_x = []
    lista_y = []
    lista_z = []           
    for model in all_models:
        lista_x.append(model[bead][0]) #get the X value of all models for each bead
        lista_y.append(model[bead][1])
        lista_z.append(model[bead][2])
    x_media = np.mean(lista_x)
    y_media = np.mean(lista_y)
    z_media = np.mean(lista_z)
    distance_tuple = (x_media,y_media,z_media)
    mean_model.append(distance_tuple)

#mean model has the values in tuples of the mean for each bead

#now get the model more similar to these mean values

sum_of_distances = []

for model in all_models:
    d_sum = 0
    for bead in range(NFRAGMENTS):
        
        d = (model[bead][0]-mean_model[bead][0])**2 + (model[bead][1]-mean_model[bead][1])**2 + (model[bead][2]-mean_model[bead][2])**2
        square_d = np.sqrt(d)
        d_sum = d_sum + square_d
    sum_of_distances.append(d_sum)  
  
  


print "MIN:"
# print sum_of_distances.index(min(sum_of_distances))
print pdbFiles[sum_of_distances.index(min(sum_of_distances))]
print "MAX:"
print pdbFiles[sum_of_distances.index(max(sum_of_distances))]
sum_of_distances.remove(max(sum_of_distances))
print "Second MAX:"
print pdbFiles[sum_of_distances.index(max(sum_of_distances))]

print "the list is:"
for i in pdbFiles:
    print i


# save all models of this matrix in another dir
storage_folder =  "{}mtx1_models/".format(root)

# store them in a folder
# storage_folder = "../"+prefix+"_final_output_"+str(uZ)+"_"+str(lZ)+"_"+str(y2)+"/" #the dir where the data will be saved
print "saving in: {}".format(storage_folder)
if not os.path.exists(storage_folder): os.makedirs(storage_folder)   



for i in pdbFiles:
    i = i[:-4] #take out ".pdb"
    
    shutil.copyfile("{}/{}.py".format(root,i), "{}{}.py".format(storage_folder,i) )
    shutil.copyfile("{}/{}.txt".format(root,i), "{}{}.txt".format(storage_folder,i) )
    
number_of_files_to_super = pdbFiles
# number_of_files_to_super = number_of_files_to_super[:5]
NFRAGMENTS = NFRAGMENTS - 1 
with open("{}superposition.cmd".format(storage_folder),"w") as superposition:
    for i in number_of_files_to_super:
        i = i[:-4]
        superposition.write("open {}.py \n".format(i))
    for i in range(len(number_of_files_to_super)):
        
        for j in range(NFRAGMENTS+1):
            if j in viewpoints:
                superposition.write("color {} #{}\n".format(color_gene,j+i*(NFRAGMENTS+1)))
            else:
                superposition.write("color {} #{}\n".format(color_grey,j+i*(NFRAGMENTS+1)))
        i += 1      
    for i in range(len(number_of_files_to_super)-1):
        i += 1
        superposition.write("match #{}-{} #0-{}\n".format(i*(NFRAGMENTS+1),i*(NFRAGMENTS+1)+NFRAGMENTS,NFRAGMENTS))
    for i in range(len(number_of_files_to_super)):
        superposition.write("shape tube #{}-{} radius 20 bandlength 10000\n".format(i*(NFRAGMENTS+1),i*(NFRAGMENTS+1)+NFRAGMENTS))
        
    #if we want a model to be highlighted
#     for i in range(len(number_of_files_to_super)):
#         if number_of_files_to_super[i] == "HoxGenomeZebra21741.pdb":
#             superposition.write("shape tube #{}-{} radius 100 bandlength 10000\n".format(i*(NFRAGMENTS+1),i*(NFRAGMENTS+1)+NFRAGMENTS)) 
#         else:
#             superposition.write("shape tube #{}-{} radius 20 bandlength 10000\n".format(i*(NFRAGMENTS+1),i*(NFRAGMENTS+1)+NFRAGMENTS))
        superposition.write("close #{}-{}\n".format(i*(NFRAGMENTS+1),i*(NFRAGMENTS+1)+NFRAGMENTS))
print "Superposition file generated in {}.".format(storage_folder)



