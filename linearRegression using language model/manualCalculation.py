import math
import os
import sys
import random

path = "C:\\Users\\tmp\\Desktop"


tmpFile1 = open(path + "\\" + "expectedVals.txt", encoding='latin')
lines = tmpFile1.readline()
vals = lines.split(",")
vals[0] = '1.7'
vals[-1] = '9.3'


total = 0
for val in vals:
    floatVal = float(val)
    total += abs(floatVal-6.438)

tmpFile1.close()
print(vals)

mae = total/len(vals)
print(mae)