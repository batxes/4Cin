#script that takes as argument the distance matrix and the expected TAD size and outputs the directionality index plot



#######!!! CARE THAT BOUDNARY CALLING CAN BE DIFFERENT FOR REVERSED DATA
import pylab

#!/usr/bin/python
import sys
import numpy as np
import math
from collections import defaultdict
import operator
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
try:
    plt.style.use('ggplot')
except ImportError:
    pass
except:
    pass

is_real_hi_data = False #where high values mean contact. In our vhic, high values = long distance = no contact
print "!!CARE, IS_REAL_HIC_DATA IS SET TO {}".format(is_real_hi_data)

add_mean_values = True

if len(sys.argv) < 2:
    print "wrong parameters. Virtual Hi-C Matrix is required."
    print " -Virtual Hi-C Matrix: file should be inside the final models directory."
    sys.exit()
try:
    input_path = sys.argv[1]
except Exception as e:
    print e
    sys.exit()


aux_list = []
lines = 0
with open(input_path,"r") as INPUT:
    for line in INPUT:
        lines += 1
        values = line.split(",")
        size = int(values[0])
        aux_list.append(float(values[2][:-1]))
quarter = size/4
tad_to = size - quarter
tad_from = 1 + quarter
if not is_real_hi_data:
    max_value = max(aux_list)
    aux_list = []
    with open(input_path,"r") as INPUT:
        for line in INPUT:
            values = line.split(",")
            aux_list.append(max_value - float(values[2][:-1]))
mean_value = np.mean(aux_list)
#print len(aux_list)
#print mean_value
size += 1
#size = int(np.sqrt(lines))



matrix = np.zeros((size,size)) 
with open(input_path,"r") as INPUT:
    for line in INPUT:
        values = line.split(",")
        if is_real_hi_data: 
            #for original HIC
            matrix[int(values[0])][int(values[1])] = float(values[2][:-1])
            matrix[int(values[1])][int(values[0])] = float(values[2][:-1])
        else:
            #ONLY for virtual HIC
            matrix[int(values[0])][int(values[1])] = max_value - float(values[2][:-1])
            matrix[int(values[1])][int(values[0])] = max_value - float(values[2][:-1])


#Calculate the directionality index (Dixo et. al. 2012 Nature)
#DI = ((B-A)/(|B-A|))((((A-E)^2)/E)+((((B-E)^2)/E)))
# E = (A+B)/2
# A = Sum of upstream read counts
# B = SUm or downstream read counts
index = np.arange(size)
### Many times to find the boundaries:
boundaries = defaultdict(int)
complete_di_list = []
for tad_size in range(tad_from,tad_to):
    di_list = []
    for i in range(size):
        #print "bin {}".format(i)
        upstream = 0
        up_cont = 0
        if ((size-i) + tad_size) > size:
            from_ = 0
        else:
            from_ = i - tad_size
        to_ = i
        for j in range(from_ ,to_):
            if j != i:
                up_cont = up_cont + 1
                upstream = upstream + matrix[j][i]
        if add_mean_values: 
            if up_cont < tad_size:
                upstream = upstream + mean_value * (tad_size - up_cont)
        downstream = 0
        down_cont = 0
        if i + tad_size < size:
            to_ = i+tad_size+1 
        else:
            to_ = size
        from_ = i
        for j in range(from_, to_):
            if j != i:
                down_cont = down_cont + 1
                downstream = downstream + matrix[j][i]
        if add_mean_values: 
            if down_cont < tad_size:
                downstream = downstream + mean_value * (tad_size - down_cont)
        #apply the equation
        E = (downstream + upstream)/2
        if E != 0:
            di1 = ((downstream-upstream)/(abs(downstream-upstream)))
            di2 = ((((upstream-E)**2)/E)+((((downstream-E)**2)/E)))
            di = di1 * di2
        else:
            di = 0
        
    #print "total= u - d    {}={} - {}".format(total, upstream, downstream)
        di_list.append(di)

    #for i in range(len(di_list)):
    #    print "{}: {}".format(i,di_list[i])


    ###############
    positive = False
    boundary = False
    counter = 0
    for i in di_list:
        if i <= 0: #----
            if positive:
                positive = False 
        if i > 0: #+++
            if positive == False:
                positive = True
                try:
                    if di_list[counter+1] > 0: #I check also that next value is positive, to filter out false positives
                        boundary = True  
                except:
                    pass
        if boundary:
            #print "Boundary: {}".format(di_list.index(i))
            boundaries[di_list.index(i)] += 1
            boundary = False
        counter += 1
    complete_di_list.append(di_list)

print "\nReminder: boundaries are found between bins that change from negative to positive values."

fig = plt.figure(figsize=(15,10)) 
plt.title("TAD calling")
ax = fig.add_subplot(111)
ax.set_xlim(-0.5,size)
#find max min values form list of lists and set half of it as plot limits
max_di_list = [max(l) for l in complete_di_list]
max_di = max(max_di_list) 
min_di_list = [min(l) for l in complete_di_list]
min_di = min(min_di_list)
ax.set_ylim(min_di/2,max_di/2) 
fig.set_facecolor('white')

sorted_x = sorted(boundaries.items(), key=operator.itemgetter(1), reverse=True)
print "\nCalculating Tad boundaries, with TAD sizes ranging between {} and {}.".format(tad_from, tad_to)
print "Number of times a boundary was found: "
tad_list = [0]*len(index)
black_b1 = []
black_b2 = []
black_b3 = []
black_b4 = []
black_b5 = []
for i in sorted_x:
    if i[0] != 0:
        print "Boundary: {} -  found {} times out of {}".format(i[0],i[1],tad_to-tad_from)
        tad_list[i[0]]=i[1]
        #set the boundaries that appear more than 50% of the time
        percen = i[1]/float((tad_to-tad_from))
        if percen >= 0.5:
            if percen >=0.5 and percen <= 0.6:
                label1="0.5 >= x <= 0.6"
                black_b1.append(i[0])
            elif percen >0.6 and percen <= 0.7:
                label2="0.6 > x <= 0.7"
                black_b2.append(i[0])
            elif percen >0.7 and percen <= 0.8:
                label3="0.7 > x <= 0.8"
                black_b3.append(i[0])
            elif percen >0.8 and percen <= 0.9:
                label4="0.8 > x <= 0.9"
                black_b4.append(i[0])
            elif percen >0.9 and percen <= 1.0:
                label5="0.9 > x <= 1.0"
                black_b5.append(i[0])
if len(black_b1) > 0:
    arrayx_1 = np.asarray(black_b1)
    arrayy_1 = np.zeros((len(arrayx_1)))
    legend = plt.plot(arrayx_1,arrayy_1,'ko',ms=3,mfc='k',mew=2,mec='k',label=label1)
if len(black_b2) > 0:
    arrayx_2 = np.asarray(black_b2)
    arrayy_2 = np.zeros((len(arrayx_2)))
    legend = plt.plot(arrayx_2,arrayy_2,'ko',ms=5,mfc='k',mew=2,mec='k',label=label2)
if len(black_b3) > 0:
    arrayx_3 = np.asarray(black_b3)
    arrayy_3 = np.zeros((len(arrayx_3)))
    legend = plt.plot(arrayx_3,arrayy_3,'ko',ms=7,mfc='k',mew=2,mec='k',label=label3)
if len(black_b4) > 0:
    arrayx_4 = np.asarray(black_b4)
    arrayy_4 = np.zeros((len(arrayx_4)))
    legend = plt.plot(arrayx_4,arrayy_4,'ko',ms=9,mfc='k',mew=2,mec='k',label=label4)
if len(black_b5) > 0:
    arrayx_5 = np.asarray(black_b5)
    arrayy_5 = np.zeros((len(arrayx_5)))
    legend = plt.plot(arrayx_5,arrayy_5,'wo',ms=11,mfc='w',mew=2,mec='k',label=label5)
print "Boundaries that appear more than 50% of the time are depicted as black spheres."
plt.legend()
alpha = 1.0/len(complete_di_list)
#create a color array depending on Below 0 or not
for di_list in complete_di_list:
    x = np.asarray(index)
    y = np.asarray(di_list)
    plt.fill_between(x,y,0,where=y<=0,facecolor="red",alpha=alpha,interpolate=True)
    plt.fill_between(x,y,0,where=y>0,facecolor="blue",alpha=alpha,interpolate=True)
    #for one on one checking
    #plt.bar(index,di_list,facecolor='#ff0000',alpha = 1 )
    #print di_list[40],di_list[41]
    #plt.show()

try:
    saved_in = input_path.split("/")
    add_string = "/".join(saved_in[:-1])
    fig.savefig("{}/Hi-C_TADs.png".format(add_string))
    print "----\nPlot saved in {}/Hi-C_TADs.png\n----".format(add_string)
except:
    pass

plt.show()
