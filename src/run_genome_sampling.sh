#!/bin/bash

#bash script that launches different jobs with different parameters

if [ $# -ne 5 ]; then
    echo "Usage: 'run_genome_maxd.sh config_file run_mode upper_Z-score lower_Z-score maxDistance'"
    exit 1
fi
config_file=$1
run_mode=$2
uZ=$3
lZ=$4
maxD=$5

init_number=0
for i in {0..24}   #50.000(0..24) models for Hox, 10.000(00.4) for bmp, wnt and tbx
do
    init=$(echo "$init_number + (2000 * $i)" | bc)
    $run_mode run_genome.sh $3 $4 $maxD $init $config_file True 
done

