# 4c2vhic

### Dependencies
chimera

IMP

matplotlib




### Usage
0 - Set the configuration file. Example is given in config.ini.

1 - Run "run_genome_maxd.sh" to get models with different max distances.
    Example: ./run_genome_maxd.sh config.ini /bin/bash 3000 12000

2 - Run "Calculate_best_maxd.py" to get the optimum max distances.
    Example: python src/calculate_best_maxd.py config.ini

3 - Pass as a parameter the optimum max distance to "run_genome_zscores.sh"
    Example: ./run_genome_zscores.sh config.ini /bin/bash 8000 1.2

4 - Run "calculate_heatmap_difference.py" to get the optimum zscores.
    Example: python src/calculate_heatmap_difference.py config.ini 8000 True

5 - With the max distance and the upper and lower z-scores, modeling can start. Run "run_genome_sampling.sh" with those parameters

6 - run "GenomeAnalysis.py"

7 - run "GenomeClustering.py"

8 - run "Tads.py"

### Notes
- All the date will be stored under a directory with the same name as the prefix set in the config file
- the bash scripts are scripts that I used for my projects. If you want to use them with another queue system or change the bins between each iteration, feel free to modify or create your own.
    * run_mode /bin/bash is set to work in the background with &

