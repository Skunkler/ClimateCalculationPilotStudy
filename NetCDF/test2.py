import os
import math
from math import *

file_name = r'H:\Keely_PythonProject\NetCDF\Upper_East\MPI-ESM-LR\future\rcp85\Future_pr_85.csv'
ReadFile = open(file_name, 'r')
out_file = open(r'H:\Keely_PythonProject\NetCDF\Upper_East\MPI-ESM-LR\future\rcp85\Future_pr_85_converted.csv', 'w')
out_file.write('time,pr\n')
lines = ReadFile.readlines()

for i in lines:
    if i.split(',')[0] != 'time': 
        converted_value = float(i.split(',')[1]) * 365
        file_line = i.split(',')[0] + ',' + str(converted_value) + '\n'
        out_file.write(file_line)

out_file.close
ReadFile.close
    
