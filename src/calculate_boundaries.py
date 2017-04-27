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

if len(sys.argv) < 3:
    print "wrong parameters. Virtual Hi-C Matrix and Tad size (in bins) for the plot are required."
    print " -Virtual Hi-C Matrix: file generated after calculate_vhic.py."
    print " -Tad size: expected size of a TAD in the locus (in bins). Check the Virtual Hi-C plot if needed."

    sys.exit()
try:
    input_path = sys.argv[1]
    tad_size = int(sys.argv[2])
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
tad_to = size
tad_from = 1
if not is_real_hi_data:
    max_value = max(aux_list)
    aux_list = []
    with open(input_path,"r") as INPUT:
        for line in INPUT:
            values = line.split(",")
            aux_list.append(max_value - float(values[2][:-1]))
mean_value = np.mean(aux_list)
print len(aux_list)
print mean_value
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
 #           print "upstream: [{}][{}]: {}".format(j,i,matrix[j][i])
            up_cont = up_cont + 1
#downstream = downstream + matrix[j][i]/(size-i) 
            upstream = upstream + matrix[j][i]
    if add_mean_values: 
        if up_cont < tad_size:
            #print "added {}".format(mean_value*(tad_size - up_cont))
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
#print "downstream: [{}][{}]:  {}".format(j,i,matrix[j][i])
#upstream = upstream + matrix[j][i]/i
            down_cont = down_cont + 1
            downstream = downstream + matrix[j][i]
    if add_mean_values: 
        if down_cont < tad_size:
            #print "added {}".format(mean_value*(tad_size - down_cont))
            downstream = downstream + mean_value * (tad_size - down_cont)
    #apply the equation
    E = (downstream + upstream)/2
    #print "{}: {}+{}/2".format(i,downstream,upstream)
    if E != 0:
        di1 = ((downstream-upstream)/(abs(downstream-upstream)))
        di2 = ((((upstream-E)**2)/E)+((((downstream-E)**2)/E)))
        di = di1 * di2
    else:
        di = 0
    #print "{} di: {} ".format(i,di)
#print "total= u - d    {}={} - {}".format(total, upstream, downstream)
    di_list.append(di)

#for i in range(len(di_list)):
#    print "{}: {}".format(i,di_list[i])

###PLOTTING

#we apply log2 so we have a smaller plotting
positive = False
boundary = False
#print di_list
print "Boundaries found in the plot (Tad size: {}):".format(tad_size)
boundaries = []
for i in di_list:
    if i <= 0: #----
        if positive:
            positive = False 
            #boundary = True 
    if i > 0: #+++
        if positive == False:
            positive = True
            boundary = True 
    if boundary:
        boundaries.append(di_list.index(i))
        boundary = False
        
for b in boundaries:
    if b != 0:
        print "Boundary: {}".format(b)
index = np.arange(size)
di_list_pos = []
di_list_neg = []
for x in di_list:
    if x < 0:
        di_list_neg.append(x)
    else:
        di_list_neg.append(0)
        
for x in di_list:
    if x > 0:
        di_list_pos.append(x)
    else:
        di_list_pos.append(0)
fig = plt.figure()
plt.title("Differential Analysis.")
ax = fig.add_subplot(111)
ax.set_xlim(-0.5,size)
#limits will be 3/4 of maximum data
lim = [abs(x) for x in di_list]
ax.set_ylim(-1*max(lim)*3/4,max(lim)*3/4)
#ax.set_ylim(-20000,20000)
#for real Hi-C
#ax.set_ylim(-100,100)
ax.set_facecolor('white')

if is_real_hi_data:
    di_list_neg = [i * -1 for i in di_list_neg] 
    di_list_pos = [i * -1 for i in di_list_pos] 
    plt.bar(index,di_list_neg,facecolor='#9999ff')
    plt.bar(index,di_list_pos,facecolor='#ff9999')

else:
    plt.bar(index,di_list_pos,facecolor='#9999ff')
    plt.bar(index,di_list_neg,facecolor='#ff9999')

try:
    saved_in = input_path.split("/")
    add_string = "/".join(saved_in[:-1])
    fig.savefig("{}/Hi-C_DI_plot.png".format(add_string))
    print "----\nPlot saved in {}/Hi-C_DI_plot.png\n----".format(add_string)
except:
    pass

plt.show()




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
    #we apply log2 so we have a smaller plotting
    for i in di_list:
        if i <= 0: #----
            if positive:
                positive = False 
                #boundary = True  
        if i > 0: #+++
            if positive == False:
                positive = True
                boundary = True  
        if boundary:
            #print "Boundary: {}".format(di_list.index(i))
            boundaries[di_list.index(i)] += 1
            boundary = False
    complete_di_list.append(di_list)
sorted_x = sorted(boundaries.items(), key=operator.itemgetter(1), reverse=True)
print "\nCalculating Tad boundaries, with TAD sizes ranging between {} and {}.".format(tad_from, tad_to)
print "Number of times a boundary was found: "
tad_list = [0]*len(index)
for i in sorted_x:
    if i[0] != 0:
        print "Boundary: {} -  found {} times out of {}".format(i[0],i[1],tad_to-tad_from)
        tad_list[i[0]]=i[1]

print "\nReminder: boundaries are found between bins that change from negative to positive values."

fig = plt.figure() 
plt.title("TAD calling")
ax = fig.add_subplot(111)
ax.set_xlim(-0.5,size)
ax.set_facecolor('white')

#create a color array depending on Below 0 or not


for di_list in complete_di_list:
    x = np.asarray(index)
    y = np.asarray(di_list)
    #plt.plot(x,y,"r",alpha=0.05)
    plt.fill_between(x,y,0,where=y<=0,facecolor="red",alpha=0.01,interpolate=True)
    plt.fill_between(x,y,0,where=y>0,facecolor="blue",alpha=0.01,interpolate=True)
    #plt.scatter(index,di_list,facecolor='#ff0000',alpha =0.05 )
    #plt.bar(index,di_list,facecolor='#ff0000',alpha =0.05 )

try:
    saved_in = input_path.split("/")
    add_string = "/".join(saved_in[:-1])
    fig.savefig("{}/Hi-C_TADs.png".format(add_string))
    print "----\nPlot saved in {}/Hi-C_TADs.png\n----".format(add_string)
except:
    pass

plt.show()
