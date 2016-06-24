#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
tad_size = 10
add_mean_values = True

if len(sys.argv) < 3:
    print "wrong parameters"
    sys.exit()
input_path = sys.argv[1]
size = int(sys.argv[2])
print "input_path is {}".format(input_path)


aux_list = []
with open(input_path,"r") as INPUT:
    for line in INPUT:
        values = line.split(",")
        aux_list.append(float(values[2][:-1]))
max_value = max(aux_list)
mean_value = np.mean(aux_list)
print "Max Value is: {}".format(max_value)
print "Mean value is {}".format(mean_value)
print "Size of matrix: {}".format(size)



matrix = np.zeros((size,size)) 
with open(input_path,"r") as INPUT:
    for line in INPUT:
        values = line.split(",")
        matrix[int(values[0])][int(values[1])] = max_value - float(values[2][:-1])
        matrix[int(values[1])][int(values[0])] = max_value - float(values[2][:-1])


#Calculate the directionality index (Dixo et. al. 2012 Nature)
#DI = ((B-A)/(|B-A|))((((A-E)^2)/E)+((((B-E)^2)/E)))
# E = (A+B)/2
# A = Sum of upstream read counts
# B = SUm or downstream read counts


di_list = []
for i in range(size):
    print "bin {}".format(i)
    upstream = 0
    up_cont = 0
    if ((size-i) + tad_size) > size:
        from_ = 0
    else:
        from_ = i - tad_size
    to_ = i
    for j in range(from_ ,to_):
        if j != i:
#print "upstream: [{}][{}]: {}".format(j,i,matrix[j][i])
            up_cont = up_cont + 1
#downstream = downstream + matrix[j][i]/(size-i) 
            upstream = upstream + matrix[j][i]
    if add_mean_values: 
        if up_cont < tad_size:
            print "added {}".format(mean_value*(tad_size - up_cont))
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
            print "added {}".format(mean_value*(tad_size - down_cont))
            downstream = downstream + mean_value * (tad_size - down_cont)
    #apply the equation
    E = (downstream + upstream)/2
    di1 = ((downstream-upstream)/(abs(downstream-upstream)))
    di2 = ((((upstream-E)**2)/E)+((((downstream-E)**2)/E)))
    di = di1 * di2
    
#print "total= u - d    {}={} - {}".format(total, upstream, downstream)
    di_list.append(di)

for i in range(len(di_list)):
    print "{}: {}".format(i,di_list[i])

###PLOTTING


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

#ax.bar(index,di_list_pos)
#ax.bar(index,di_list_neg)
plt.bar(index,di_list_pos,facecolor='#9999ff')
plt.bar(index,di_list_neg,facecolor='#ff9999')
plt.show()

print matrix
print mean_value
