# 4c2vhic

### Dependencies
chimera

IMP 2.4 (newer versions crash)

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
    Gets the best models and also makes a superposition of all those models. They are very likely to be mirror image of each other

7 - run "GenomeClustering.py"
    Gets population of models depending on K value of Kmeans. Also get a superposition of each of the populations.

8 - run "Tads.py"

9 - run "Final_genome_models.py"
    Takes as argument the matrix of one of the solutions from GenomeClustering.py. It will tell us which model is the one closest to the average.

10 - run "GenomePainting.py"
    It will paint the genome model closest to the average depending on the bam files

### Notes
- All the date will be stored under a directory with the same name as the prefix set in the config file
- the bash scripts are scripts that I used for my projects. If you want to use them with another queue system or change the bins between each iteration, feel free to modify or create your own.
    * run_mode /bin/bash is set to work in the background with &


#TODO
    Give user the best model with the tube shape
    write down that chimera needs to be a "ln -s" and give permissions to whole python2.7 inside chimera/bin also
    IMP 2.5 <
    if "AttributeError: 'Model' object has no attribute 'this'"
    install Swig 3.0.7. For this perhaps u need to install sudo apt-get install libpcre3 libpcre3-dev
    remember that the bash scripts are also done by me, they can change it if they want. Right now I don't know how to take from the config file the data and use it in the bash script

    make tube shape after clustering? in the same file?
    give colors to last superposition?
    pip install pysam
