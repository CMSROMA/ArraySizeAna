## Python stuff
from array import array
import os
import math as mt
import numpy as np
import re
import argparse
from collections import defaultdict
import pandas as pd
import sys
import csv

#--- Options

parser = argparse.ArgumentParser(usage="python3 runAll.py --inputdir data/")
parser.add_argument('--inputdir',dest='inputdir',required=True)
args = parser.parse_args()

for filename in os.listdir(args.inputdir):
    #print (filename)

    filename_trunc = filename.split(".")[0]
    #print (filename_trunc)

    array = filename_trunc
    #print (array)

    command = ( "python3 Dimensions.py --array {} --data {}".format( array , args.inputdir+"/"+filename) ) 
    print (command)
    os.system(command)
    
