#!/bin/bash

#$ -N MYF5
#$ -pe make 20
#$ -cwd

echo "Job started"
#IrxA
#python 4Cin.py /home/ibai/4Cin/data/IrxA/finales/ IrxA_new --cpu 20 --fragments_in_each_bead 90 --colormap magma_r  --from_dist 12000 --to_dist 20000 --from_zscore 0.1 --to_zscore 0.5 
#IrxB
#python 4Cin.py /home/ibai/4Cin/data/IrxB/final/ IrxB_new --cpu 20 --fragments_in_each_bead 45 --colormap magma_r  --from_dist 8000 --to_dist 15000 --from_zscore 0.1 --to_zscore 0.5 
#Irx Amphioxus
#python 4Cin.py data/AmphiIrx/final/ Amphi_Irx_high_res --from_dist 1000 --to_dist 10000 --fragments_in_each_bead 5 --colormap magma_r --cpu 20 --Nmodels 50000 
#Irx Amphioxus improved
#python 4Cin.py data/AmphiIrx/final2/ Amphi_Irx_high_res2 --from_dist 1000 --to_dist 10000 --fragments_in_each_bead 5 --colormap magma_r --cpu 20 --Nmodels 50000 
#Irx Fly
#python 4Cin.py data/FLY_IRX/4c_virtual/final/ Fly_Irx_high_res --fragments_in_each_bead 1 --from_dist 1000 --colormap magma_r --cpu 20 --Nmodels 50000 
#IrxAa
#python 4Cin.py data/IrxAa/final/ IrxAa_new_models --fragments_in_each_bead 40  --colormap magma_r --cpu 20 --Nmodels 50000 
#IrxBa
#python 4Cin.py data/IrxBa/final/ IrxBa_new_models --fragments_in_each_bead 30  --colormap magma_r --cpu 20 --Nmodels 50000 
#Irx Strigamia
#python 4Cin.py data/Strigamia_IRX_data/final/ Irx_strigamia_models --fragments_in_each_bead 2  --colormap magma_r --cpu 20 --Nmodels 50000 --from_dist 1000 --to_dist 8000

#WT2_MYF
#python 4Cin.py data/myf5/wt_final2 Myf5_WT2_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
#PAE2_Myf
#python 4Cin.py data/myf5/pae_final2 Myf5_PAE2_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
#WT_MYF_no56
#python 4Cin.py data/myf5/wt_final_no56 Myf5_WT_no56_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
#muT_MYF_no56
#python 4Cin.py data/myf5/mut_final_no56 Myf5_MUT_no56_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
#PAE_Myf_no56
#python 4Cin.py data/myf5/pae_final_no56 Myf5_PAE_no56_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
#WT_MYF
#python 4Cin.py data/myf5/wt_final Myf5_WT_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
#muT_MYF
#python 4Cin.py data/myf5/mut_final Myf5_MUT_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
#PAE_Myf
#python 4Cin.py data/myf5/pae_final Myf5_PAE_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
#python 4Cin.py data/myf5/wt_final_no5629 Myf5_WT_no5629_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
#muT_MYF_no56
#python 4Cin.py data/myf5/mut_final_no5629 Myf5_MUT_no5629_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
#PAE_Myf_no56
#python 4Cin.py data/myf5/pae_final_no5629 Myf5_PAE_no5629_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
#muT_MYF_no29
python 4Cin.py data/myf5/mut_final_no29 Myf5_MUT_no29_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
echo "Job finished"
