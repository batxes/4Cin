#!/bin/bash

#$ -N highres_sshwt
#$ -pe make 20
#$ -cwd

echo "Modeling started"
python aske.py /home/ibai/SHH_IBAI/results/raw/wt/ SHH_WT_models_highres  --fragments_in_each_bead 20 --colormap magma_r --cpu 20
echo "Modeling finished"
