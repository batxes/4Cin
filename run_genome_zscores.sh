#!/bin/bash

#bash script that launches different jobs with different zscore parameters
# it needs the MAXD as a variable. Also the maximum z-score. Bigger z-score will require more modeling.

if [ $# -ne 4 ]; then
    echo "Usage: 'run_genome_zscores.sh config_file run_mode maxDistance max_zscore'"
    echo "- config_file: Configuration file"
    echo "- run_mode: /bin/bash, qsub"
    echo "- maxDistance: The maximum distance in Angstroms that the modeling will use"
    echo "- max_zscore: The maximum limit for the z-score"
    echo ""
    echo "Take into account the z-score bins are of 0.1"
    exit 1
fi

max_zscore=$4
max_zscore=$(echo "$max_zscore * 10" | bc)
max_zscore=${max_zscore/.*}
uZ_init=0.1
lZ_init=-0.1
config_file=$1
run_mode=$2 #/bin/bash or qsub
y2=$3
for i in $(seq 1 $max_zscore)
do
    uZ=$(echo "$uZ_init * $i" | bc)
    for j in $(seq 1 $max_zscore)
    do
       lZ=$(echo "$lZ_init * $j" | bc)
        $run_mode run_genome.sh $uZ $lZ $y2 0 $config_file False
        echo "$run_mode run_genome.sh $uZ $lZ $y2 0 $config_file False"
    done
done

