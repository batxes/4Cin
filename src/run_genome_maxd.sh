#!/bin/bash

#bash script that launches different jobs changing the max dist
uZ_init=0.1
lZ_init=-0.1
y2_init=0
for i in {1..1}
do
    uZ=$(echo "$uZ_init * $i" | bc)
    for j in {1..1}
    do
        lZ=$(echo "$lZ_init * $j" | bc)
        for k in {1..12}
        do
            y2=$(echo "$y2_init + 1000 * $k" | bc)
            qsub run_genome.sh $uZ $lZ $y2
#            #qsub -pe ompi 24 run_genome.sh $uZ $lZ $y2 if we parallelize our jobs
            echo $uZ $lZ $y2
        done
    done
done

