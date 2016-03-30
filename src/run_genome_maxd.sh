#!/bin/bash

#bash script that launches different jobs changing the max dist
y2_init=0
for k in {3..10}
    do
        y2=$(echo "$y2_init + 1000 * $k" | bc)
        /bin/bash run_genome.sh 0.1 -0.1 $y2 0 config.ini False
        #qsub run_genome.sh $uZ $lZ $y2
        #qsub -pe ompi 24 run_genome.sh $uZ $lZ $y2 if we parallelize our jobs
        echo $uZ $lZ $y2
    done

