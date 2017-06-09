#!/bin/bash

#$ -N IrxBa_new
#$ -pe make 20
#$ -cwd

echo "Job started"
#IrxA
#python 4Cin.py /home/ibai/4Cin/data/IrxA/finales/ IrxA_new --cpu 20 --fragments_in_each_bead 90 --colormap magma_r  --from_dist 12000 --to_dist 20000 --from_zscore 0.1 --to_zscore 0.5 
#IrxB
#python 4Cin.py /home/ibai/4Cin/data/IrxB/final/ IrxB_new --cpu 20 --fragments_in_each_bead 45 --colormap magma_r  --from_dist 8000 --to_dist 15000 --from_zscore 0.1 --to_zscore 0.5 
#Irx Amphioxus
#python 4Cin.py data/AmphiIrx/final/ Amphi_Irx_high_res --from_dist 1000 --to_dist 10000 --fragments_in_each_bead 5 --colormap magma_r --cpu 20 --Nmodels 50000 
#Irx Fly
#python 4Cin.py data/FLY_IRX/4c_virtual/final/ Fly_Irx_high_res --fragments_in_each_bead 1 --from_dist 1000 --colormap magma_r --cpu 20 --Nmodels 10000 --jump_step analysis --uZ 0.1 --lZ -0.1 --max_distance 1000 --verbose
#IrxAa
#python 4Cin.py data/IrxAa/final/ IrxAa_new_models --fragments_in_each_bead 40  --colormap magma_r --cpu 20 --Nmodels 50000 
#IrxBa
python 4Cin.py data/IrxBa/final/ IrxBa_new_models --fragments_in_each_bead 30  --colormap magma_r --cpu 20 --Nmodels 50000 
echo "Job finished"
