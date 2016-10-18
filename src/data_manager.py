#!/usr/bin/python

import sys, re
import numpy as np
from scipy.stats import skew,kurtosis
try:
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
except ImportError:
    pass
except:
    pass

#############################################################################################################
# code that calculates the average and standard deviation of the given 4c data file
#
# Parameters: 4cfile
#############################################################################################################


# function: file checker
#
# Checks if the passing file exists. If exists, it opens.

def fileCheck(f):
    try:
        f = open (f, 'r')
        return f
    except IOError:
        print "\nError: File "+ f +" does not appear to exist.\n"
        sys.exit()

# function: Value Reader by windows
#
# reads the file and extracts the values every N lines

def valueReaderNWindow(f,window):
    counter = 0
    aux = 0
    arrayList = []
    for line in f:
        counter += 1
        values = re.split('\t',line)
        values[3] = values[3].strip() #remove \n from the list
        if (values[3] is '-'):
            read = 0 + 1 # +1 to counter log10
        else:
            read = float(values[3]) + 1 # +1 to counter log10
        aux += read
        if counter == window:
            counter = 0
            aux = aux / window
            arrayList.append(aux)
            aux = 0
    return arrayList

# function Size Reader
#
# calculates the size of the reads of the input file and returns an arraylist with the values

def sizeReader(f):
    arrayList = []
    for line in f:
        values = re.split('\t',line)
        values[1] = values[1].strip() #remove \n from the list
        values[2] = values[2].strip() #remove \n from the list
        size = int(values[2]) - int(values[1])
        arrayList.append(size)
    return arrayList


# function: calculate values by windows
#
# sums up all the read counts of the inputa data 

def calculateNWindowedValues(WINDOW, files):
    read_sums = []
    factors = []
    for i in range(len(files)):
        reads = []
        f = fileCheck(files[i])
        reads = valueReaderNWindow(f,WINDOW)
        read_sums.append(sum(reads))
    for i in read_sums:
        value = max(read_sums)/i
        factors.append(value)
    return factors

# Function: calculate distances from input data
#
# Takes the read counts and converts them in distance restraints for the modelling

# Note: EVERY LANE OF 4C DATA WILL BE INDEPENDENT
def calculateNWindowedDistances(window,uZ,lZ,y2,files,wanna_plot=False,heatmap=False):
    show_z_scores = False  
    plot = wanna_plot
    HEATMAP_DATA = []
    HEATMAP_DATA_LOG = []
    reads = []
    final_zscores = []
    final_reads = []
    start_windows = []
    end_windows = []
    factors = calculateNWindowedValues(1.0,files)
    number_of_genes = len(files)
    if wanna_plot:
        print """Negative skewness shows large proportion of experimental noise. Positive  = population of large structural variability. 
Kurtosis shows if the distribution is single peaked or not. High kt = many peaks, we need low KT to show a single peak """
    for i in range(number_of_genes):
        f = fileCheck(files[i])
        reads = valueReaderNWindow(f,window)  
        reads2 = []
        # We normalize the data depending on the number of reads.
        # We calculated beforehand the numbers of multiplication for the normalization
        reads = [read*factors[i] for read in reads ]           
        # get the minimum read counts and swap them with the minimum of all values. We don't take into account no reads in a fragment
        min_read = max(reads) #initialization
        for j in reads:
            if j != 1.0 and j < min_read:
                min_read = j
        reads = [min_read if x==1.0 else x for x in reads]
        # this is the one we want to compare to
        HEATMAP_DATA.append(reads)
        # apply Log10 to data to normalize it
        reads_normalized = [np.log10(read) for read in reads]
        HEATMAP_DATA_LOG.append(reads_normalized)

        #Z-score calculation
        ##### START      Divide for translocation data 
        translocation_exp = True
        translocation_bead = 59
        if (translocation_exp):
            chunk1 = reads_normalized[:translocation_bead]
            mean1 = np.mean(chunk1)
            std_dev1 = np.std(chunk1)
            chunk1 = [(read - mean1)/std_dev1 for read in chunk1]
            chunk1 = chunk1[::-1]
            chunk2 = reads_normalized[translocation_bead:]
            mean2 = np.mean(chunk2)
            std_dev2 = np.std(chunk2)
            chunk2 = [(read - mean2)/std_dev2 for read in chunk2]
            chunk2 = chunk2[::-1]
            reads_normalized = chunk1 + chunk2
        else:
            mean = np.mean(reads_normalized)
            std_dev = np.std(reads_normalized)
            reads_normalized = [(read - mean)/std_dev for read in reads_normalized]
        # Skewness shows if data is skewed toward the right or left tail of the normal distributed z scores. 
        # Negative skewness shows large proportion of experimental noise. Positive  = population of large structural variability.
        # Kurtosis shows if the distribution is single peaked or not. High kt = many peaks, we need low KT to show a single peak
        if wanna_plot:
            print "Skewness of {}: {}. -1 < x < 2.5.".format(i,skew(reads_normalized))
            print "Kurtosis of {}: {}. -1 < x < 8.".format(i,kurtosis(reads_normalized))
            print ""
        x2 = min(reads_normalized)
        x1 = max(reads_normalized)
        y1 = 300  #Angstroms width of chromatin 
        slope = (y2-y1) / (x2-x1)
        inside_window = False #when we are inside the 4C good values window, set True
        window_start = 0
        window_end = 0
        counter = 0
        for read in reads_normalized:
            counter += 1
            #when the z score is above the uZ, the window starts.
            if read >= uZ and not inside_window:
                inside_window = True
                window_start = counter
            #end of window
            if read >= uZ and inside_window:
                window_end = counter
        start_windows.append(window_start)
        end_windows.append(window_end)
        if show_z_scores:
            print "gene "+ str(i) +"---> window start: " + str(window_start) + "   end: "+str(window_end)
        for  read in reads_normalized:
            if read < uZ and read > lZ:  #take out the reads where the z score is between the lz and the uZ
                reads2.append (0) 
            else:
                reads2.append(slope*(read-x1)+y1)
        final_reads.append(reads2)       
        final_zscores.append(reads_normalized)
    if show_z_scores:    
        mean_tena = []    
        for i in final_zscores:      
            mean_tena.append(max(i))
        if show_z_scores:
            print "mean of top z scores: "
            print np.mean(mean_tena)
    #return data if we are using for the z-score empirical calculations
    if heatmap:
        return HEATMAP_DATA, HEATMAP_DATA_LOG
    # If we want to plot
    for i in range(number_of_genes):
        if plot:
            fig = plt.figure(figsize=(100, 100)) 
            plt.subplot(3,1,1)
            if translocation_exp:
                reversed_list_aux = HEATMAP_DATA[i][:translocation_bead][::-1]
                reversed_list_aux2 = HEATMAP_DATA[i][translocation_bead:][::-1]
                bar_list = plt.bar(range(len(HEATMAP_DATA[i])),reversed_list_aux+reversed_list_aux2,width=1)
                bar_list[translocation_bead:].set_color('r')
            else:
                plt.bar(range(len(HEATMAP_DATA[i])),HEATMAP_DATA[i],width=1)
            plt.xlim(0,len(HEATMAP_DATA[i]))  
            plt.ylabel("Number of Reads")
            plt.xlabel(files[i])
            plt.subplot(3,1,2)
            plt.plot(final_zscores[i])
            plt.xlim(0,len(final_zscores[i]))  
            plt.axhline(y=uZ)
            plt.axhline(y=lZ)
            plt.ylabel("Z score")
            plt.xlabel("Beads")
            plt.subplot(3,1,3)
            plt.bar(range(len(final_reads[i])),final_reads[i],width=1)
            plt.xlim(0,len(final_reads[i]))
            plt.ylabel("Distance restraints in Angstroms")
#             plt.switch_backend('QT4Agg')
            figManager = plt.get_current_fig_manager()
            plt.subplots_adjust(bottom=0.05, right=0.99, top=0.99, left=0.05)
            #figManager.window.showMaximized()
            #figManager.Maximize(True)
            plt.show()
    return final_reads, final_zscores, start_windows, end_windows

        

#test ###############################################################################################################################

if __name__ == "__main__":
    import ConfigParser
    number_of_arguments = len(sys.argv)
    print "TESTING READS "
    if number_of_arguments == 5:
        config_file = sys.argv[1]
        uZ = sys.argv[2]
        lZ = sys.argv[3]
        y2 = sys.argv[4]
    elif number_of_arguments == 2:
        config_file = sys.argv[1]
        uZ = 0.1
        lZ = -0.1
        y2 = 7000
    else:
        print "Not enough parameters. Config file is needed. uZ, lZ and max distance can also be passed. Default: uZ = 0.1, lZ = -0.1, max distance = 7000"
        sys.exit()

    #read the config file
    config = ConfigParser.ConfigParser()
    try:
        config.read(config_file)
        prefix = config.get("ModelingValues", "prefix")
        WINDOW = float(config.get("ModelingValues", "WINDOW"))
        files = config.get("ModelingValues", "files")
        files = re.sub('[\n\s\t]','',files)
        files = files.split(",")    
        viewpoints = config.get("ModelingValues", "viewpoints")
        viewpoints = re.sub('[\n\s\t]','',viewpoints)
        viewpoints = viewpoints.split(",")
        viewpoints = [ int(i) for i in viewpoints]
        viewpoints = [int(i/WINDOW) for i in viewpoints]
        genes = config.get("ModelingValues", "genes")
        genes = re.sub('[\n\s\t]','',genes)
        genes = genes.split(",")
        genes = [ int(i) for i in genes]
        genes = [int(i/WINDOW) for i in genes]
        NFRAGMENTS = int(config.get("ModelingValues", "NFRAGMENTS"))
        NFRAGMENTS = int(NFRAGMENTS/WINDOW)
    except:
        print "\nError reading the configuration file.\n"
        e = sys.exc_info()[1]
        print e
        sys.exit()
    calculateNWindowedDistances(WINDOW, uZ, lZ, y2, files, True, False)


    
