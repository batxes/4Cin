#!/bin/bash
#$ -N _4c2vhic
#$ -cwd
#s -pe make 24



/usr/bin/python -W ignore /home/ibai/4c2vhic/src/GenomeModeling.py $1 $2 $3 $4 $5 $6 
echo "Genome with $1 $2 $3 and starting point $4 finished"
