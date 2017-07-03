#!/bin/bash

#Author: ibai Irastorza
#execute inside the frag_counts directory
#script that takes datadir, chr, start and end and replaces the original data

DIR=$1;
CHR=$2;
START=$3;
END=$4;


for i in $(ls $DIR);do
    echo "trimming" $i
    awk -F '\t' -v chr_var="$CHR" -v start_var="$START" -v end_var="$END" '{if ($1 == chr_var && $2 >= start_var && $3 <= end_var){print $1,$2,$3,$4 }}' OFS="\t" $DIR$i >> $i
done
for i in $(ls $DIR);do
    echo "moving" $i
    mv $i $DIR$i
done

