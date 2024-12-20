#!/bin/bash

#$ -N sshWT.batxes
#$ -pe make 20
#$ -cwd

echo "Modeling started"
python run_genome_maxdV3.py /home/ibai/SHH_IBAI/results/raw/wt/ SHH_WT_models --cpu 20 --fragments_in_each_bead 100
echo "Modeling finished"
