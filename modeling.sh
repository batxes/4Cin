#!/bin/bash

#$ -N modeling.batxes
#$ -pe make 20
#$ -cwd

echo "Modeling started"
python run_genome_maxdV3.py /home/ibai/4c2vhic/data/Shh_mouse/temp/ Test_models --cpu 20
echo "Modeling finished"
