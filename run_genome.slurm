#!/bin/bash
#SBATCH -J _4c2vhic

/usr/bin/python src/GenomeModeling.py $1 $2 $3 $4 $5 $6 
echo "Genome with $1 $2 $3 and starting point $4 finished"
