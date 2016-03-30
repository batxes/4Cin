#!/bin/bash

#bash script that launches different jobs with different parameters
init_number=0
for i in {0..24}   #50.000(0..24) models for Hox, 10.000(00.4) for bmp, wnt and tbx
#for i in {25..49}   #50.000(0..24) models for Hox, 10.000(00.4) for bmp, wnt and tbx
do
    init=$(echo "$init_number + (2000 * $i)" | bc)
    qsub run_genome.sh 0.9 -0.1 3000 $init #for irxAa
    #qsub run_genome.sh 0.1 -0.8 5000 $init #IrxAb
    #qsub run_genome.sh 0.6 -0.1 5000 $init #IrxBa
    #qsub run_genome.sh 0.1 -1.1 7000 $init #IrxB mouse
done

