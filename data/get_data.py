#!/usr/bin/python

first_gen_position = 85300000
last_gen_position = 86780000

size = 20000
path = "Esc_20kb_NcoI_Six_3cols.txt"
path2 = "4c_Six_mouse/"

for i in range(first_gen_position,last_gen_position+1,size):
    print i
    output = open (path2+str(i)+".txt", "w")
    with open(path, "r") as raw_data:
        dic = {}
        for line in raw_data:
            values = line.split("\t")
            bead_from = int(values[0])    
            bead_to = int(values[1])    
            count = float(values[2])
            if bead_from == i:
                dic[bead_to] = count
        print dic
        for j in range(first_gen_position,last_gen_position+1,size):
            if j in dic.keys():
                output.write("Chr17\t{}\t{}\t{}\n".format(j,j+size , dic[j])) 
            else:
                output.write("Chr17\t{}\t{}\t{}\n".format(j, j+size, 0)) 


    output.close()


