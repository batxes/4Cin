#!/bin/bash
#$ -N Myf5_mut
#$ -cwd

#CHECK THAT IT IS PRUEBA.PY OR PRUEBA_SAMPLING.PY
#massive
/usr/bin/python /mnt/beegfs/ibai/genome/src/GenomeModeling_Massive.py $1 $2 $3 $4
echo "Genome with $1 $2 $3 and $4 finished"

#parameter calculations
#/usr/bin/python /mnt/beegfs/ibai/genome/src/GenomeModeling_2.py $1 $2 $3
#echo "Genome with $1 $2 and $3 finished"

~                                                 
