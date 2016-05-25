# combine #0-210 newchainids False name combine modelId 211
# write format pdb #211 test.pdb

#!/usr/bin/python

import re
import os
import subprocess

import time

from variables import WINDOW, prefix, NFRAGMENTS, files, genes, hox_genes, zebrafish, amphioxus, mouse



start_time = time.time()


root = "/home/bioinfo/workspace/genome/data/{}_final_output_0.2_-0.2_7000/".format(prefix)  
pdb_output = "/home/bioinfo/workspace/genome/data/pdb_output_{}/".format(prefix)


if not os.path.exists(pdb_output): os.makedirs(pdb_output)
if zebrafish:
    matrix_file = "data/matrix_zebra_1.txt"
    write_pdb = 'get_genome_pdbs_zebrafish.py'
if amphioxus:
    matrix_file = "data/matrix_amphioxus_1.txt"    
    write_pdb = 'get_genome_pdbs_amphioxus.py'


models = []
with open(matrix_file, "r") as mtx:
    for line in mtx:
        models.append(re.split("\t", line)[1])

models = models[1:]


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
# 
# 
#     string = ""
#     lista = []    
#     for line2 in distance_output:
#         string = string + line2
#         if line2 == "\n":
#             lista.append(string)
#             string = ""
#          
#     #Distance between #209:1@ and #210:1@: 512.326
#     
#     for line2 in lista:
#       
#         distance = re.search(r'#(\d*).*#(\d*).*:\s?(\d*\.\d*)',line2)  
#         if (distance):
# #             print "[{}][{}][{}]".format(distance.group(1),distance.group(2),counter)
#             matrix[int(distance.group(1))][int(distance.group(2))][counter] = float(distance.group(3))
#             matrix[int(distance.group(2))][int(distance.group(1))][counter] = float(distance.group(3))
            
         




