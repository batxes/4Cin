awk '$1=="chr2" && $2 >= 171840000 && $3 <= 173380000' Esc_20kb_NcoI > Esc_20kb_NcoI_bmp7.txt

awk 'BEGIN {FS="\t|:|-|,"; OFS="\t"} $5 >= 171840000 && $6 <= 173380000 {print $2, $5, $7}' Esc_20kb_NcoI_bmp7.txt > Esc_20kb_NcoI_bmp7_3cols.txt


awk 'BEGIN {FS="."} FNR==NR {x[$1]++} !($1 in x) {print $1}' b a






























#SHH region in mouse
awk '$1=="chr5" && $2 >= 28600000 && $3 <= 30000000' Esc_20kb_hindIII_rep1 > Esc_20kb_hindIII_rep1_Shh.txt
awk 'BEGIN {FS="\t|:|-|,"; OFS="\t"} $5 >= 28600000 && $6 <= 30000000 {print $2, $5, $7}' Esc_20kb_hindIII_rep1_Shh.txt >Esc_20kb_hindIII_rep1_Shh_3cols.txt

