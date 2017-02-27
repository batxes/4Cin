#!/usr/bin/python

# Script that runs small rounds of modeling with different Max distances

import sys
import os
import re
import getopt
import ConfigParser
import subprocess
from multiprocessing import Process, Lock, Pool, current_process
import argparse


def worker(instructions):
    p = subprocess.Popen(instructions)
    p.wait()

parser = argparse.ArgumentParser(
description=''' Pre Modeling process. Will set the best MAX distance fore the modeling and the best Z scores.''',
epilog= """ Simple usage: python run_genome_maxd.py --config config_template.ini.""")
parser.add_argument("--cpu",type=int, default=1, action="store", dest="number_of_cpu",help='number of CPUs that will be used in this script')
parser.add_argument("--nmodels",type=int, default=50, action="store", dest="number_of_models",help='number of models that will be generated in the pre-modeling phase')
parser.add_argument("--from_dist",type=int, default=5000, action="store", dest="from_dist",help='minimum max-distance that will be used in the pre-modeling phase')
parser.add_argument("--to_dist",type=int, default=12000, action="store", dest="to_dist",help='maximum max-distance that will be used in the pre-modeling phase')
parser.add_argument("--dist_bins",type=int, default=1000, action="store", dest="dist_bins",help='size of jump between from_dist and to_dist')
parser.add_argument("config", action="store",help='Config file with all the data for the modeling')
args = parser.parse_args()

number_of_cpu = args.number_of_cpu
ini_file = args.config
number_of_models = args.number_of_models
from_dist = args.from_dist
to_dist = args.to_dist
dist_bins = args.dist_bins

p = Pool(number_of_cpu)

execute = []
for dist in range(from_dist,to_dist+dist_bins,dist_bins):
    instructions = ['/usr/bin/python', 'src/run_modeling.py', '0.1' ,'-0.1', str(dist),' 0' ,str(ini_file) ,'False']
    execute.append(instructions)
p.map(worker,execute)

print("\n\nWhen the jobs have finished, run 'python src/calculate_best_maxd.py {}'".format(sys.argv[1]))


