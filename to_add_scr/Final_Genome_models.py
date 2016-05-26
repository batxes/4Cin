# combine #0-210 newchainids False name combine modelId 211
# write format pdb #211 test.pdb

#!/usr/bin/python

import re
import os
import subprocess
from itertools import combinations
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from os import listdir
from os.path import isfile, join
from optparse import Values
import shutil
from variables import WINDOW, prefix, NFRAGMENTS, files, genes, hox_genes, zebrafish, amphioxus, mouse


if amphioxus:
    genes_red = hox_genes[:3]
    genes_blue = hox_genes[-3:]
if zebrafish:
    genes_red = hox_genes[:3]
    genes_blue = hox_genes[-2:]

color_grey = "#b333b333b333"
color_gene = "#ffffb3330000"
color_gene_blue = "#00000000ffff"
color_gene_red = "#ffff00000000"

start_time = time.time()



root = "/home/bioinfo/workspace/genome/data/{}_final_output_0.2_-0.2_7000/".format(prefix)  
pdb_output = "/home/bioinfo/workspace/genome/data/pdb_output_{}/".format(prefix)


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
storage_folder =  "/home/bioinfo/workspace/genome/data/{}_final_output_0.2_-0.2_7000_mtx1/".format(prefix)

# store them in a folder
# storage_folder = "../"+prefix+"_final_output_"+str(uZ)+"_"+str(lZ)+"_"+str(y2)+"/" #the dir where the data will be saved
print "saving in: {}".format(storage_folder)
if not os.path.exists(storage_folder): os.makedirs(storage_folder)   



for i in pdbFiles:
    i = i[:-4] #take out ".pdb"
    
    shutil.copyfile("{}{}.py".format(root,i), "{}{}.py".format(storage_folder,i) )
    shutil.copyfile("{}{}.txt".format(root,i), "{}{}.txt".format(storage_folder,i) )
    
number_of_files_to_super = pdbFiles
# number_of_files_to_super = number_of_files_to_super[:5]
NFRAGMENTS = NFRAGMENTS - 1 
with open("{}superposition.cmd".format(storage_folder),"w") as superposition:
    for i in number_of_files_to_super:
        i = i[:-4]
        superposition.write("open {}.py \n".format(i))
    for i in range(len(number_of_files_to_super)):
        
        for j in range(NFRAGMENTS+1):
            if j in genes_blue:
                superposition.write("color {} #{}\n".format(color_gene_blue,j+i*(NFRAGMENTS+1)))
            elif j in genes_red:
                superposition.write("color {} #{}\n".format(color_gene_red,j+i*(NFRAGMENTS+1)))
            elif j in genes:
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
