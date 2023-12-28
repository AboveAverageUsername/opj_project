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
    
    
for i in range(0, len(names)):
    roll = random.randrange(1,101)
    if(roll==2):
        tmpFile = open('C:\\Users\\tmp\\Desktop\\test\\' + names[i] , 'w', encoding='latin')
        tmpFile.writelines(txts[i])
        tmpFile.close()  
    elif(roll==3):
        tmpFile = open('C:\\Users\\tmp\\Desktop\\train\\' + names[i] , 'w', encoding='latin')
        tmpFile.writelines(txts[i])
        tmpFile.close()          
        
    