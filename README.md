
# 4c2vhic

This is a suite of scripts that lets you generate 3D models of the chromatin of your favourite locus, using 4C data as the only input. It is able to create Hi-C like contact maps of these 3D models and analyze the region further. 

Used in Acemel RD, Tena JJ, Irastorza-Azcarate I, Marletaz F, Gomez-Marin C, de la Calle-Mustienes E, Bertrand S, Diaz SG, Aldea D, Aury JM et al.: A single three-dimensional chromatin compartment in amphioxus indicates a stepwise evolution of vertebrate Hox bimodal regulation. Nat Genet 2016, 48: 336-341. (http://www.nature.com/ng/journal/v48/n3/full/ng.3497.html)

## Overview 
![alt tag](figures/github_pipe.png)

Many other marks can be painted
![alt tag](figures/genomePainting)

## Dependencies

Note: Tested only in Linux, of course.

python 2.7

matplotlib

scipy

numpy

UCSF Chimera (Download from https://www.cgl.ucsf.edu/chimera/download.html)

IMP 2.5, 2.4 (newer versions crash) (Download from http://integrativemodeling.org/old-versions.html)

pysam (for paint_model.py)


Go to Installing dependencies to install them.


## Fast Usage (run this commands)

Fast Note: Models can be than locally or with queue systems like Slurm or SGE

Fast Note: After each script, a little message will appear indicating which is the next step



0 - Generate your config.ini file. See example: config_template.ini

1 - python src/prepare_data.py 4C_files

2 - python run_genome_maxd.py config.ini local

3 - python src/calculate_best_maxd.py config.ini

4 - python run_genome_zscores.py config.ini local

5 - python src/calculate_best_zscores.py config.ini True

6 - python run_genome_sampling.py config.ini local

7 - python src/run_analysis.py config.ini subset std_dev threshold

8 - python src/run_clustering.py config.ini subset kmeans

9 - python src/calculate_vhic.py config.ini matrix.txt True



[Optionals]

10 - python src/get_representative_model.py config.ini matrix.txt

11 - python src/paint_model.py config.ini model.py

12 - python src/calculate_boundaries.py vhic.txt tad_size

13 - python src/Evo_comp.py config.ini config2.ini vhic.txt vhic2.txt

14 - python src/Mut_comp.py config.ini config2.ini vhic.txt vhic2.txt

15 - python src/data_manager.py config.ini

# Explained Usage

Note: Models can be than locally or with queue systems like Slurm or SGE

Note: After each script, a little message will appear indicating which is the next step

0 - Generate your configuration file. Example is given in config_template.ini.

1 - run "prepare_data.py" to homogenize the 4C files. All 4C files need to have the same number of fragments and the same length.

    Example: python src/prepare_data.py 4C_files

2 - Run "run_genome_maxd.py" to do models with different max distances.

    Example: python run_genome_maxd.py config.ini local|qsub|sbatch 

3 - Run "Calculate_best_maxd.py" to get the optimum max distance. Get the max distance that has the most similar genome length to your data. We assume the canonical nucleotide length is of 0.1 nm (ref1, ref2)

    Example: python src/calculate_best_maxd.py config.ini

4 - Run "run_genome_zscores.py" to do models with different upper bound and lower bound Z-scores.

    Example: python run_genome_zscores.py config.ini local|qsub|sbatch

5 - Run "calculate_best_zscores.py" to get the optimum upper and lower bound zscores. set last argument to True to see the validation plots.

    Example: python src/calculate_best_zscores.py config.ini True

6 - With the max distance and the upper and lower z-scores, modeling can start. Run "run_genome_sampling.py".

    Example: python run_genome_sampling.py config.ini local|qsub|sbatch
    
    [3D Models are generated]

7 - run "src/run_analysis.py" to get a subset of all the models. The best models ordered by the IMP scoring function are gathered and also makes a superposition of all those models. The models are very likely to be mirror image of other models, getting two populations of models.
   
Take into account that we need to tweak the std_dev and the cut_of_percentage to gather models. In my essays, I have seen that setting the std_dev at a 10-20% of maximum distance and the threshold in 15% works well normally. I set 200 models out of 50000 as subset, 1000 for std_dev and 15 for threshold
    
    Example: python src/run_analysis.py config.ini 200 1000 15

8 - run "run_clustering.py" to get populations of best models depending on the similarity of the RMSD. It generates a superposition of each of the populations. If we get 2 populations that are mirror image of each other, we can be sure that the modeling went correctly. Set the subset from above and 2 as kmeans value.

    Example: python src/run_clustering.py config.ini 200 2

9 - run "calculate_vhic.py" to generate the virtual Hi-C of one of the populations of the final models. We will set different values in the config file under [VHiC] like:

    -show_fragments_in_vhic: to plot circles of genes or other interesting fragments in the virtual Hi-C
    
    -name_of_fragments: the name of the previous fragments.
    
    -color_of_fragments: will set different colors to the viewpoints. Matplotlib palette.
    
    -maximum_hic_values: will smooth or "burn" the virtual Hi-C heatmap.
    

We will set also the config file, the RMSD matrix file from the clustering of one of the populations and "True" if it is the first time we calculate the matrix. If we already calculated and we just one to add viewpoints, change color of them or set a different maximum_hic_value, we will set to False
    
    Example: python src/calculate_vhic.py config.ini matrix.txt True
    
      [Virtual Hi-C is generated]
     
     
Optional Steps:
    
10 - run "get_representative_model.py". Takes as argument the config file and the matrix of one of the solutions from GenomeClustering.py. It will tell us which model is the one closest and furthest to the average. It will also generate a superposition of the models of that cluster, that will be able to run in UCSF chimera. 

    Example: python src/get_representative_model.py config.ini matrix_cluster1.txt

11 - run "paint_model.py". It will map epigenetic marks in a model of our choice. We will set the path of the bed or bam file and the colormap (matplotlib) in the config file under [Painting]. 

    Example: python src/paint_model.py config_ini /home/user/4c2vhic/data/MyModels/MyModels_final_output/model10.py 

12 - run "calculate_boundaries.py". Given the distance matrix and the the number of beads a TAD has in your virtual HI-C, it plots the directionality index bar plot.

    python src/calculate_boundaries.py vhic.txt tad_size

13 - run "Evo_comp.py". Evolutive comparion. Given two config files and two vhic's generated with calculate_vhic.py of different loci or organisms and the position of Genes/enhancers (beads), it crates a hi-c like matrix with the relative positions of both loci. We will need to set the config file variables under [EvoComp]. Similar to the [VHiC] parameters, we will need to set the viewpoints and the window variable for each of the loci.

    Example: python src/Evo_comp.py config.ini config2.ini vhic1.txt vhic2.txt
    
14 - run "Mut_comp.py". Mutation comparison. The same as Evo_comp.py, but this time the same locus is compared. Useful to study structural genomic variations like inversion, truncation, deletions... Fragments set in the [VHiC] section of config file 1 will be used for the comparison.

    Example: python src/Mut_comp.py config.ini config2.ini vhic.txt vhic2.txt

15 - Input data can be checked calling data_manager.py. Shows 3 plots for each 4C file, showing read counts, Z scores and the conversion into distance restraints that would be used in the modeling.

    Example: python src/data_manager.py config.ini [0.2 -0.4 8000]  

### Installing dependencies

Matplotlib, scipy and numpy:

apt-get install python-matplotlib

apt-get install python-scipy

apt-get install python-numpy

To install Chimera:
make it executable: chmod +x chimera-installer.bin
run it
make link: ln -s CHIMERA/bin/chimera /usr/local/bin/chimera 
if problems visit: https://www.cgl.ucsf.edu/chimera/data/downloads/1.11.2/linux.html

Install IMP from source:

sudo apt-get install cmake

sudo apt-get install libboost1.49-all-dev

sudo apt-get install libhdf5-dev

sudo apt-get install swig

sudo apt-get install libcgal-dev

sudo apt-get install python-dev

Note: For Ubuntu 13.10 libboost1.53-all-dev should be installed instead. 
      For Ubuntu 14.04 libboost1.54-all-dev should be installed instead.

Download the IMP tarball file from http://salilab.org/imp/ and uncompress it:

wget https://integrativemodeling.org/2.5.0/download/imp-2.5.0.tar.gz -O imp-2.5.0.tar.gz

tar xzvf imp-2.5.0.tar.gz

Create a directory for the IMP instalation.

mkdir IMP

Move into the IMP directory and compile the code (Note: the -j option stands for the number of CPUs you want to assign to the compiler; the higher the faster).

cd IMP

cmake ../imp-2.5.0 -DCMAKE_BUILD_TYPE=Release -DIMP_MAX_CHECKS=NONE -DIMP_MAX_LOG=SILENT

make -j4

Once the compilation has finished, open the file setup_environment.sh in your IMP directory and copy the first lines into your ~/.bashrc file (if this file in not present in your home directory, create it). These lines should look like:

LD_LIBRARY_PATH="/SOMETHING/imp-2.5.0/lib:/SOMETHING/imp-2.5.0/lib:/SOMETHING/imp-2.5.0/src/dependency/RMF/:$LD_LIBRARY_PATH"
export LD_LIBRARY_PATH

PYTHONPATH="/SOMETHING/imp-2.5.0/lib:/SOMETHING/imp-2.5.0/lib:/SOMETHING/imp-2.5.0/src/dependency/RMF/:$PYTHONPATH"
export PYTHONPATH

Note

Important note: Do not copy the lines above, copy them from setup_environment.sh, where SOMETHING is replaced by your real path to IMP. 

Installation process of IMP taken from: https://3dgenomes.github.io/TADbit/install.html#imp-3d-modeling

Install pysam (only for paint_model.py)
pip install pysam. 

If does not work:
    git clone git@github.com/pysam-developers/pysam
    python setup.py build
    python setup.py install (libcurl4-gnutls-dev )
    !if u get an error saying regcompA was not found, rename regex.h from the boost library (in my case /usr/local/include/regex.h) to something else before building. The change it back!

### Additional scripts
Getting 4C data like from Hi-C

python data/get_data.py  -> generates 4C like files from the Hi-C file

calculate_vhic_from_realdata.py
convert_HiC_data.py
HiC_comp.py

### Notes

- If you want to concatenate the beads with a tube, after openning the model in UCSF-Chimera, write this in its command line: "shape tube #X-Y radius Z bandlength 10000" (X and Y being the first and last beads, Z being the thickness of tube in Angstroms.)

- All the data will be stored under a directory with the same name as the prefix set in the config file

- bam files need to be sorted and indexed before using. Example: samtools sort mouse_h3k4me3_ES_bingren_rep1.bam mouse_h3k4me3_ES_bingren_rep1.bai 

# FAQ

I have UCSF Chimera installed but it does not work.
    Create a link to chimera with "ln -s" and give permissions to whole python2.7 inside chimera/bin


"AttributeError: 'Model' object has no attribute 'this'"
    install Swig 3.0.7. For this perhaps u need to install sudo apt-get install libpcre3 libpcre3-dev
  
matplotlib colors are here:
    pip install colour
    : https://pypi.python.org/pypi/colour

GenomePainting does not work.
    Check the file generated coloring.cmd and fix the path. Chimera does not like if the first line is something like "open ../myModel.py". Change to something like /home/user/myModel.py.

### references

ref1. Tjong H, Gong K, Chen L, Alber F. Physical tethering and volume exclusion determine higher-order ge- nome organization in budding yeast. Genome Res. 2012; 22: 1295–1305. doi: 10.1101/gr.129437.111 PMID: 22619363

ref2. Bystricky K, Heun P, Gehlen L, Langowski J, Gasser SM. Long-range compaction and flexibility of inter- phase chromatin in budding yeast analyzed by high-resolution imaging techniques. Proc Natl Acad Sci U S A. 2004; 101: 16495–16500. PMID: 15545610


###### writeee
    we modified the windows so the beads represent the same in SIX comparison

    
    Pax3 data -> take our locus
    then take chr2 and chr13 separately and apply prepare_data.py
    then concatenate them and double the value of the aberrant 2+13 chromosome


