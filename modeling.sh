#!/bin/bash

#$ -N Irx_highres
#$ -pe make 20
#$ -cwd

echo "Job started"
#IrxA
#python 4Cin.py /home/ibai/4Cin/data/IrxA/finales/ IrxA_new --cpu 20 --fragments_in_each_bead 90 --colormap magma_r  --from_dist 12000 --to_dist 20000 --from_zscore 0.1 --to_zscore 0.5 
#IrxB
#python 4Cin.py /home/ibai/4Cin/data/IrxB/final/ IrxB_new --cpu 20 --fragments_in_each_bead 45 --colormap magma_r  --from_dist 8000 --to_dist 15000 --from_zscore 0.1 --to_zscore 0.5 
#Irx Amphioxus
python 4Cin.py data/AmphiIrx/final/ Amphi_Irx_high_res --from_dist 1000 --to_dist 8000 --fragments_in_each_bead 4 --colormap magma_r --cpu 20 --Nmodels 10000 
echo "Job finished"
