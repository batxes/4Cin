#!/bin/bash

#$ -N Drome_Strig
#$ -pe make 20
#$ -cwd

echo "Job started"
############# IRX
#IrxA
#python 4Cin.py /home/ibai/4Cin/data/IrxA/finales/ IrxA_new --cpu 20 --fragments_in_each_bead 90 --colormap magma_r  --from_dist 12000 --to_dist 20000 --from_zscore 0.1 --to_zscore 0.5 
#IrxB
#python 4Cin.py /home/ibai/4Cin/data/IrxB/final/ IrxB_new --cpu 20 --fragments_in_each_bead 45 --colormap magma_r  --from_dist 8000 --to_dist 15000 --from_zscore 0.1 --to_zscore 0.5 
#Irx Amphioxus
#python 4Cin.py data/AmphiIrx/final/ Amphi_Irx_high_res --from_dist 1000 --to_dist 10000 --fragments_in_each_bead 5 --colormap magma_r --cpu 20 --Nmodels 50000 
#Irx Amphioxus improved
#python 4Cin.py data/AmphiIrx/final2/ Amphi_Irx_high_res2 --from_dist 1000 --to_dist 10000 --fragments_in_each_bead 5 --colormap magma_r --cpu 20 --Nmodels 50000 
#python 4Cin.py data/AmphiIrx/final2/ Amphi_Irx_Super_high_res --from_dist 500 --to_dist 5000 --dist_bins 500 --fragments_in_each_bead 2 --colormap magma_r --cpu 20 --Nmodels 50000 
##python 4Cin.py data/AmphiIrx/final2/ Amphi_Irx_SuperUltra_high_res --from_dist 500 --to_dist 5000 --dist_bins 500 --fragments_in_each_bead 1 --colormap magma_r --cpu 1 --Nmodels 50000 --jump_step vhic --maximum_hic_value 900 --uZ 0.1 --lZ -0.1 --max_distance 1500 
#Irx Fly
#python 4Cin.py data/FLY_IRX/4c_virtual/final/ Fly_Irx_high_res2 --fragments_in_each_bead 1 --from_dist 500 --to_dist 3000 --dist_bins 500 --colormap magma_r --cpu 20 --Nmodels 50000 --ignore_beads 117 121 126 154 159 248 333
#IrxAa
#python 4Cin.py data/IrxAa/final/ IrxAa_new_models --fragments_in_each_bead 40  --colormap magma_r --cpu 20 --Nmodels 50000 
#IrxBa
#python 4Cin.py data/IrxBa/final/ IrxBa_new_models --fragments_in_each_bead 30  --colormap magma_r --cpu 20 --Nmodels 50000 
#python 4Cin.py data/IrxBa/final_binarized_W51H100/ IrxBa_new_models_binary --fragments_in_each_bead 30  --colormap magma_r --cpu 20 --Nmodels 50000 --binary_data
#Irx Strigamia
#python 4Cin.py data/Strigamia_IRX_data/final/ Irx_strigamia_models --fragments_in_each_bead 2  --colormap magma_r --cpu 20 --Nmodels 50000 --from_dist 1000 --to_dist 8000
#irx strigamia more resolution 
#python 4Cin.py data/Strigamia_IRX_data/final/ Irx_strigamia_models_high_res --fragments_in_each_bead 1  --colormap magma_r --cpu 20 --Nmodels 50000 --from_dist 500 --to_dist 5000 --dist_bins 500

##SSH SIX ARTICLE 4CIN

#Does variability change if we have less models
python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_100/ Six_zebra_100kmodels --cpu 20 --fragments_in_each_bead 33 --Nmodels 100000  --max_distance 12000 --uZ 0.1 --lZ -0.1 --jump_step pre_modeling
python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_100/ Six_zebra_50kmodels --cpu 20 --fragments_in_each_bead 33 --Nmodels 50000  --max_distance 12000 --uZ 0.1 --lZ -0.1 --jump_step pre_modeling
python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_100/ Six_zebra_25kmodels --cpu 20 --fragments_in_each_bead 33 --Nmodels 25000  --max_distance 12000 --uZ 0.1 --lZ -0.1 --jump_step pre_modeling
python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_100/ Six_zebra_10kmodels --cpu 20 --fragments_in_each_bead 33 --Nmodels 10000  --max_distance 12000 --uZ 0.1 --lZ -0.1 --jump_step pre_modeling
python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_100/ Six_zebra_5kmodels --cpu 20 --fragments_in_each_bead 33 --Nmodels 5000  --max_distance 12000 --uZ 0.1 --lZ -0.1 --jump_step pre_modeling
python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_100/ Six_zebra_2kmodels --cpu 20 --fragments_in_each_bead 33 --Nmodels 2000  --max_distance 12000 --uZ 0.1 --lZ -0.1 --jump_step pre_modeling
python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_100/ Six_zebra_1kmodels --cpu 20 --fragments_in_each_bead 33 --Nmodels 1000  --max_distance 12000 --uZ 0.1 --lZ -0.1 --jump_step pre_modeling
python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_100/ Six_zebra_500models --cpu 20 --fragments_in_each_bead 33 --Nmodels 500  --max_distance 12000 --uZ 0.1 --lZ -0.1 --jump_step pre_modeling

#Six_Zebra Downsampling OF 4C INPUT DATA
#python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_100/ Six_zebra_downsampling_100 --fragments_in_each_bead 33 --colormap magma_r --cpu 20 --Nmodels 5000 --uZ 0.1 --lZ -0.1 --max_distance 12000 --jump_step pre_modeling
#python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_80/ Six_zebra_downsampling_80 --fragments_in_each_bead 33 --colormap magma_r --cpu 20 --Nmodels 5000 --uZ 0.1 --lZ -0.1 --max_distance 12000 --jump_step pre_modeling
#python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_60/ Six_zebra_downsampling_60 --fragments_in_each_bead 33 --colormap magma_r --cpu 20 --Nmodels 5000 --uZ 0.1 --lZ -0.1 --max_distance 12000 --jump_step pre_modeling 
#python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_40/ Six_zebra_downsampling_40 --fragments_in_each_bead 33 --colormap magma_r --cpu 20 --Nmodels 5000 --uZ 0.1 --lZ -0.1 --max_distance 12000 --jump_step pre_modeling
#python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_20/ Six_zebra_downsampling_20 --fragments_in_each_bead 33 --colormap magma_r --cpu 20 --Nmodels 5000 --uZ 0.1 --lZ -0.1 --max_distance 12000 --jump_step pre_modeling 
#python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_10/ Six_zebra_downsampling_10 --fragments_in_each_bead 33 --colormap magma_r --cpu 20 --Nmodels 5000 --uZ 0.1 --lZ -0.1 --max_distance 12000 --jump_step pre_modeling 
#python 4Cin.py ../Zebra_six_data/downsampling/smooth_data_5/ Six_zebra_downsampling_5 --fragments_in_each_bead 33 --colormap magma_r --cpu 20 --Nmodels 5000 --uZ 0.1 --lZ -0.1 --max_distance 12000 --jump_step pre_modeling 


#Variability calculation for SIX and SHH models. Bioiformatics
#python 4Cin.py data/six/six23/final/ Six_zebra_models --jump_step vhic --max_distance 13000 --uZ 0.1 --lZ -0.1 --cpu 20 --fragments_in_each_bead 33
#python 4Cin.py data/4c_Six_mouse/final Six_mouse_models --jump_step vhic --max_distance 11000 --uZ 0.2 --lZ -0.1 --cpu 20 --fragments_in_each_bead 1 
#python 4Cin.py ../SHH_IBAI/results/raw/wt/ SHH_WT_models --jump_step vhic --max_distance 11000 --uZ 0.1 --lZ -0.1 --cpu 20 --fragments_in_each_bead 100 
#python 4Cin.py ../SHH_IBAI/results/raw/inv/ SHH_INV_models --jump_step vhic --max_distance 10000 --uZ 0.2 --lZ -0.1 --cpu 20 --fragments_in_each_bead 100 


#jackniffing in mouse six
#python 4Cin.py data/4c_Six_mouse/final_4left Six_mouse_models_4left --cpu 20 --fragments_in_each_bead 1 --uZ 0.1 --lZ -0.4 --max_distance 12000 --repaint_vhic --maximum_hic_value 5000
#python 4Cin.py data/4c_Six_mouse/final_4center Six_mouse_models_4center --cpu 20 --fragments_in_each_bead 1 --uZ 0.5 --lZ -0.5 --max_distance 11000 --repaint_vhic --maximum_hic_value 5000
#python 4Cin.py data/4c_Six_mouse/final_4right Six_mouse_models_4right --cpu 20 --fragments_in_each_bead 1 --uZ 0.1 --lZ -0.1 --max_distance 12000 --repaint_vhic --maximum_hic_value 5000
#python 4Cin.py data/4c_Six_mouse/final Six_mouse_models --cpu 20 --fragments_in_each_bead 1 --uZ 0.2 --lZ -0.1 --max_distance 11000 --repaint_vhic --maximum_hic_value 5000

#python 4Cin.py data/4c_Six_mouse/final_4promoter Six_mouse_models_4promoter --cpu 20 --fragments_in_each_bead 1 
#python 4Cin.py data/4c_Six_mouse/final_4nopromoter Six_mouse_models_4nopromoter --cpu 20 --fragments_in_each_bead 1 


############## Carvajal MYF
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
#python 4Cin.py data/myf5/mut_final_no29 Myf5_MUT_no29_models --fragments_in_each_bead 5  --from_dist 1000 --to_dist 5000 --colormap magma_r --cpu 20 --Nmodels 10000 --ignore_beads 43 44 45 46 47 48 49
echo "Job finished"
