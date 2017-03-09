#!/bin/bash

#SBATCH -J modeling.batxes
#SBATCH --ntasks=20

python run_genome_maxdV3.py /home/ibai/4c2vhic/data/Shh_mouse/temp/ Test_models --cpu 20
