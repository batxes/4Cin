#!/bin/bash

#bash script that launches different jobs with different parameters

if [ $# -ne 7 ]; then
    echo "Usage: 'run_genome_sampling.sh config_file run_mode upper_Z-score lower_Z-score maxDistance number_of_models models_in_each_job'"
    exit 1
fi
config_file=$1
run_mode=$2 #/bin/bash or qsub
uZ=$3
lZ=$4
maxD=$5
number_of_models=$6
models_in_each_job=$7
until=$(echo "$number_of_models / $models_in_each_job" | bc)
until=$(echo "$until - 1" | bc)
until=${until/.*}


init_number=0
for i in $(seq 0 $until)   # 25*2000 = 50.000 Models.  
    do
        init=$(echo "$init_number + ($models_in_each_job * $i)" | bc)
        $run_mode run_genome.sh $3 $4 $maxD $init $config_file True 
        echo "$run_mode run_genome.sh $3 $4 $maxD $init $config_file True"
    done

