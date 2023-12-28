from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
import math
import os
import sys
import random

path = "C:\\Users\\tmp\\Desktop\\firstLast"
inFolder = os.listdir(path)

names = []
txts = []

count = 0
for movie in inFolder:
    count+=1
    print(count)
    tmpFile1 = open(path + "\\" + movie, encoding='latin')
    lines = tmpFile1.readline()
    tmpFile1.close()
    names.append(movie)
    txts.append(lines)