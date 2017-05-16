#!/bin/bash

#SBATCH -J IrxA
#SBATCH --ntasks=20

python 4Cin.py /home/ibai/4Cin/data/IrxA/finales/ IrxA_new --cpu 20 --fragments_in_each_bead 90
