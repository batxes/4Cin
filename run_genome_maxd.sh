#!/bin/bash

#bash script that launches different jobs changing the max dist

if [ $# -ne 4 ]; then
    echo "Usage: 'run_genome_maxd.sh config_file run_mode dist_start dist_end'"
    echo "- config_file: Configuration file"
    echo "- run_mode: /bin/bash, qsub"
    echo "- dist_start: Minimum distance for the distance range to use in the modelling in Angstroms"
    echo "- dist_end: Maximum distance for the distance range to use in the modelling in Angstroms"
    echo ""
    echo "Take into account the distance changes every 1000 A"
    exit 1
fi
config_file=$1
run_mode=$2 #/bin/bash or qsub
y2_init=0
dist_start=$3
dist_start=$(echo "$dist_start / 1000" | bc)
dist_start=${dist_start/.*}

dist_end=$4
dist_end=$(echo "$dist_end / 1000" | bc)
dist_end=${dist_end/.*}

for k in $(seq $dist_start $dist_end)
    do
        y2=$(echo "$y2_init + 1000 * $k" | bc)
        if [[ $run_mode == "/bin/bash" ]]; then
            $run_mode run_genome.sh 0.1 -0.1 $y2 0 $config_file False &
            echo "$run_mode run_genome.sh 0.1 -0.1 $y2 0 $config_file False &"
        else
            $run_mode run_genome.sh 0.1 -0.1 $y2 0 $config_file False 
            #qsub run_genome.sh $uZ $lZ $y2
            #qsub -pe ompi 24 run_genome.sh $uZ $lZ $y2 if we parallelize our jobs
            echo "$run_mode run_genome.sh 0.1 -0.1 $y2 0 $config_file False"
        fi    
    done
if [[ $run_mode == "/bin/bash" ]]; then
    wait
