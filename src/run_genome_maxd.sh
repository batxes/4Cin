#!/bin/bash

#bash script that launches different jobs changing the max dist

if [ $# -ne 2 ]; then
    echo "Usage: 'run_genome_maxd.sh config_file run_mode'"
    exit 1
fi
config_file=$1
run_mode=$2
y2_init=0
for k in {3..10}
    do
        y2=$(echo "$y2_init + 1000 * $k" | bc)
        $run_mode run_genome.sh 0.1 -0.1 $y2 0 $config_file False
        #qsub run_genome.sh $uZ $lZ $y2
        #qsub -pe ompi 24 run_genome.sh $uZ $lZ $y2 if we parallelize our jobs
        echo $uZ $lZ $y2
    done

