#!/bin/bash

#bash script that launches different jobs with different zscore parameters
# it needs the MAXD as a variable

if [ $# -ne 3 ]; then
    echo "Usage: 'run_genome_maxd.sh config_file run_mode maxDistance'"
    exit 1
fi


uZ_init=0.1
lZ_init=-0.1
config_file=$1
run_mode=$2
y2=$3
for i in {1..2}
do
    uZ=$(echo "$uZ_init * $i" | bc)
    for j in {1..2}
    do
       lZ=$(echo "$lZ_init * $j" | bc)
        $run_mode run_genome.sh $uZ $lZ $y2 0 $config_file False
        echo $uZ $lZ $y2
    done
done

