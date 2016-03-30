#!/bin/bash

#bash script that launches different jobs with different zscore parameters
# it needs the MAXD as a variable
uZ_init=0.1
lZ_init=-0.1
y2=$1
for i in {1..12}
do
    uZ=$(echo "$uZ_init * $i" | bc)
    for j in {1..12}
    do
       lZ=$(echo "$lZ_init * $j" | bc)
        qsub run_genome.sh $uZ $lZ $y2
        echo $uZ $lZ $y2
    done
done

