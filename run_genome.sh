#!/bin/bash
#$ -N _4c2vhic
#$ -cwd

/usr/bin/python src/GenomeModeling.py $1 $2 $3 $4 $5 $6 
echo "Genome with $1 $2 $3 and starting point $4 finished"
