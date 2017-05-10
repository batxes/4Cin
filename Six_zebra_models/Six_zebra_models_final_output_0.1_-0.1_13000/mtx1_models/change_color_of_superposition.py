#!/usr/bin/python

# 2017/Feb/14

#Script that takes the superposicion-cmd and changes the viewpoints colors.

import re

colors = ["#d7d719191c1c","#fdfdaeae6161","#ffffffffbfbf","#ababd9d9e9e9","#2c2c7b7bb6b6"]
number_of_models = 110
number_of_beads = 56
total_beads = number_of_beads * number_of_models
viewpoints = [4,25,27,47,51]


lines = []
no_viewpoint = False
with open ("superposition.cmd") as stdin:
    for line in stdin:
        result = re.match('color #(\w+) #(\d+)',line)
        if result:
            for viewpoint in viewpoints:
                color_beads = [viewpoint+number_of_beads*x for x in range(number_of_models)]
                if int(result.group(2)) in color_beads:
                    lines.append("color {} #{}\n".format(colors[viewpoints.index(viewpoint)],result.group(2)))
                    no_viewpoint = False
                    break
                else:
                    no_viewpoint = True
            if no_viewpoint:
                #lines.append(line)
                no_viewpoint = False
        else:
            lines.append(line)

with open ("superposition_modified.cmd", "w") as stdout:
    for line in lines:
        stdout.write(line)

