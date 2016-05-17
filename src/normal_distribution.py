#!/usr/bin/python

import sys, re
import numpy as np
try:
    import matplotlib.pyplot as plt
except ImportError:
    pass
except:
    pass
#from variables import WINDOW, prefix, NFRAGMENTS, files, genes, zebrafish, amphioxus, mouse,IrxA, IrxB, bmp7, tbx, wnt, IrxAa, IrxAb, IrxBa,myf5_wt, myf5_mut, drome


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


#
#
# Reads the fragments starts from the files
def fragmentsStartReader(f):
    arrayList = []
    for line in f:
        values = re.split('\t',line)
        values[1] = values[1].strip() #remove \n from the list
        arrayList.append(int(values[1]))
    return arrayList


def calculateNWindowedValues(WINDOW, files):
 
#     print "CALCULATIN N WINDOWED VALUES FOR THE NORMALIZATION (BIGGER DIVIDED BY THE REST)"
    read_sums = []
    factors = []
    for i in range(len(files)):
     
        reads = []
     
        f = fileCheck(files[i])
        reads = valueReaderNWindow(f,WINDOW)
#         print "###  "+ files[i] +"  ### "+str(sum(reads))
        read_sums.append(sum(reads))

    for i in read_sums:
        value = max(read_sums)/i
        factors.append(value)
#         print "division -> {}".format(value)
        
    return factors



# EVERY LANE OF 4C DATA WILL BE INDEPENDENT
# SINCE WE WILL SURELY HAVE AT LEAST 5 POINTS WHERE THE DISTANCES ARE VERY LOW.
#IF WE TAKE ALL DATA TOGETHER, ONLY PDX1 WILL HAVE A POINT WHERE DISTANCE IS LOWEST
def calculateNWindowedDistances(window,uZ,lZ,y2,files,wanna_plot=False,heatmap=False):
    
    #print "CALCULATIN N WINDOWED DISTANCES"
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

#     i = file_number
    number_of_genes = len(files)
    for i in range(number_of_genes):
        f = fileCheck(files[i])
        reads = valueReaderNWindow(f,window)  
        # we normalize the data depending on the number of reads.
        # We calculated beforehand the numbers of multiplication for the normalization
        reads = [read*factors[i] for read in reads ]           
        ### HEAT MAP DATAAAAAAAAAAA
        # this is the one we want to compare to
        HEATMAP_DATA.append(reads)
        # apply Log10 to data to normalize it
        reads_normalized = [np.log10(read) for read in reads]
    
        HEATMAP_DATA_LOG.append(reads_normalized)

        mean = np.mean(reads_normalized)
        std_dev = np.std(reads_normalized)

        #Z-score calculation
        reads_normalized = [(read - mean)/std_dev for read in reads_normalized]


        x2 = min(reads_normalized)
#       y2 = 3000 #6400 
    
        x1 = max(reads_normalized)
        y1 = 300  #minimun distances 
    
    
        slope = (y2-y1) / (x2-x1)

#       reads = [slope*(read-x1)+y1 for read in reads2]
        reads = []

        
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
                reads.append (0) 
            else:
                reads.append(slope*(read-x1)+y1)

        #print "window_start: "+str(window_start)+" - window end:"+str(window_end)
        final_reads.append(reads)       
        final_zscores.append(reads_normalized)
    if show_z_scores:    
        mean_tena = []    
        for i in final_zscores:      
            print max(i)
            mean_tena.append(max(i))
        if show_z_scores:
            print "mean of top z scores: "
            print np.mean(mean_tena)

    #return data if we are using for the heat difference
    if heatmap:
        return HEATMAP_DATA, HEATMAP_DATA_LOG
    
    
#    FOR PLOTTING!!!!!
    
    for i in range(number_of_genes):
        if plot:
            plt.subplot(3,1,1)
            
            #ploteo de readcounts reales
            plt.bar(range(len(HEATMAP_DATA[i])),HEATMAP_DATA[i],width=1)
            plt.xlim(0,len(HEATMAP_DATA[i]))  #this varies depending on NFRAGMENTS right?
            plt.ylabel("Reads")
            
            #ploteo de Zscores
            plt.subplot(3,1,2)
            plt.plot(final_zscores[i])
            plt.xlim(0,len(final_zscores[i]))  #this varies depending on NFRAGMENTS right?
            plt.axhline(y=uZ)
            plt.axhline(y=lZ)
            plt.ylabel("Z score")
            
            
            plt.xlabel(files[i])
            
            plt.subplot(3,1,3)
            plt.bar(range(len(final_reads[i])),final_reads[i],width=1)
            plt.xlim(0,len(final_reads[i]))
            plt.ylabel("Restraint distance")
            plt.xlabel(files[i])
#             plt.switch_backend('QT4Agg')

            figManager = plt.get_current_fig_manager()
            plt.subplots_adjust(bottom=0.01, right=0.99, top=0.99, left=0.05)
            #figManager.window.showMaximized()
            #figManager.Maximize(True)
            
            plt.show()
            

    

    return final_reads, final_zscores, start_windows, end_windows



def calculate_heatmap (path_to_file):
    print "CALCULATIN HEATMAP"
    
    f = open(path_to_file, "r")
    all_arrays = []
    for line in f:
        array = re.split('\t',line)
        reads = np.genfromtxt(array)
        print reads
        # we want low distances red color in heatmap
        reads = [-1*read for read in reads]
        print reads
        all_arrays.append(reads)
    
    
    
    #output_0.2_-0.2_3000.0/paraHoxGenome324.txt

#     labels2 = ['GSX1','PDX1','CDX2','INS_CDX2','INS_GSX1']    
#     labels2 = ['hoxd3a','hoxd4a','hoxd10a','hoxd11a','hoxd13a']  
#     labels2 = ['AMHOX2','AMHOX5','AMHOX6','AMHOX9','AMHOX11','AMHOX13','AMHOX15'] #old anphioxus
    labels2 = ['GPATCH','LNPA','EVX2','Hox15','Hox13','Hox11','Hox9','Hox7',
               'Hox6','Hox5','Hox2','MTX','CBX','NFE','MEOX',]
    
    ax = plt.subplot(2,1,1)
    z = np.array(all_arrays)
    plt.pcolor(z)
    # plt.set_cmap('gray')
    plt.colorbar()
    # c = plt.pcolor(z, edgecolors='w', linewidths=1)
    plt.axis([0,z.shape[1],0,z.shape[0]])
    ax.set_yticklabels(['']+labels2)
#     plt.xlabel("Genomic Position")
    plt.show()
        

#test ###############################################################################################################################

if __name__ == "__main__":
    print "TESTING READS \n\n"
    import ConfigParser
    
    show_z_scores = True    
    calculate_heat_map = False
    do_the_plots = False
    
    #read the config file
    config = ConfigParser.ConfigParser()
    try:
        config.read("config.ini")
        
        prefix = config.get("ModelingValues", "prefix")
        
        WINDOW = float(config.get("ModelingValues", "WINDOW"))
        
        files = config.get("ModelingValues", "files")
        files = re.sub('[\n\s\t]','',files)
        files = files.split(",")    
        
        viewpoints = config.get("ModelingValues", "viewpoints")
        viewpoints = re.sub('[\n\s\t]','',viewpoints)
        viewpoints = viewpoints.split(",")
        viewpoints = [ int(i) for i in viewpoints]
        viewpoints = [int(round(i/WINDOW)) for i in viewpoints]
        
        genes = config.get("ModelingValues", "genes")
        genes = re.sub('[\n\s\t]','',genes)
        genes = genes.split(",")
        genes = [ int(i) for i in genes]
        genes = [int(round(i/WINDOW)) for i in genes]
        
        NFRAGMENTS = int(config.get("ModelingValues", "NFRAGMENTS"))
        NFRAGMENTS = int(NFRAGMENTS/WINDOW)
    except:
        print "\nError reading the configuration file.\n"
        e = sys.exc_info()[1]
        print e
        sys.exit()
    if (do_the_plots):
        #calculate10WindowedValues()
        #upper bound Z-score
        uZ = 0.1
        #lower bound Z-score
        lZ = -0.1
        # Max distance BETWEEN bead
        y2 = 6000 
        HEATMAP_DATA,HEATMAP_DATA_LOG = calculateNWindowedDistances(WINDOW, uZ, lZ, y2, True)

        if (calculate_heat_map):
            labels = ['INS_GSX1','INS_CDX2','CDX2','PDX1','GSX1']
            labels = ['hoxd3a','hoxd4a','hoxd10a','hoxd11a','hoxd13a']
    #         labels = ['AMHOX2','AMHOX5','AMHOX6','AMHOX9','AMHOX11','AMHOX13','AMHOX15'] #old amphioxus
            labels = ['GPATCH','LNPA','EVX2','Hox15','Hox13','Hox11','Hox9','Hox7',
                   'Hox6','Hox5','Hox2','MTX','CBX','NFE','MEOX',]
        
            #the heatmap (with the no-sqared elements) prints the values reversed so we do this
            HEATMAP_DATA_REVERSED = []
            HEATMAP_DATA_LOG_REVERSED = []
            for i in reversed(HEATMAP_DATA):
                HEATMAP_DATA_REVERSED.append(i)
            for i in reversed(HEATMAP_DATA_LOG):
                HEATMAP_DATA_LOG_REVERSED.append(i) 
            labels2 = ['GSX1','PDX1','CDX2','INS_CDX2','INS_GSX1']    
            labels2 = ['hoxd13a','hoxd11a','hoxd10a','hoxd4a','hoxd3a']
    #         labels2 = ['AMHOX15','AMHOX13','AMHOX11','AMHOX9','AMHOX6','AMHOX5','AMHOX2'] #old amphioxus
            labels2 = ['MEOX','NFE','CBX','MTX','Hox2','Hox5','Hox6','Hox7',
                   'Hox9','Hox11','Hox13','Hox15','EVX2','LNPA','GPATCH',]
            

            ax = plt.subplot(2,1,1)
            z = np.array(HEATMAP_DATA_REVERSED)
            c = plt.pcolor(z)
            # plt.set_cmap('gray')
            plt.colorbar()
            # c = plt.pcolor(z, edgecolors='w', linewidths=1)
            plt.axis([0,z.shape[1],0,z.shape[0]])
            ax.set_yticklabels(['']+labels2)
            
            ax = plt.subplot(2,1,2)
            z = np.array(HEATMAP_DATA_LOG_REVERSED)
            c = plt.pcolor(z)
            # plt.set_cmap('gray')
            plt.colorbar()
            # c = plt.pcolor(z, edgecolors='w', linewidths=1)
            plt.axis([0,z.shape[1],0,z.shape[0]])
            ax.set_yticklabels(['']+labels2)
            plt.xlabel("Genomic Position")
            plt.show()
            

    
    
        plt.show()
        
        
    # calculate_heatmap("../src/output_1.0_-0.3_6000/HoxGenome0.txt")
    #calculate_mean_heatmap("../output_1.0_-0.3_6000.0")
    
    
    
    #upper bound Z-score

    uZ = 1.1
    #lower bound Z-score
    lZ = -0.3
    # Max distance BETWEEN bead
    y2 = 13000 
    calculateNWindowedDistances(WINDOW, uZ, lZ, y2, files, True, False)


    
