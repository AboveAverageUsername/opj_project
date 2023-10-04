import os
import re

path = "C:\\Users\\tmp\\Desktop\\Magnum corpus"
inFolder = os.listdir(path)

count = 0
for movie in inFolder:
    count+=1
    print(count)
    #tmpFile1 = open(path + "\\" + movie, encoding='cp855')
    tmpFile1 = open(path + "\\" + movie, encoding='latin')
    lines = tmpFile1.readlines()
    tmpFile1.close()
    outLine = ""
    
    for line in lines:
        outLine += line.replace("\n", " ")
    
    
    outfile = open("C:\\Users\\tmp\\Desktop\\1Lines\\" + movie, "w", encoding='latin')
    outfile.write(outLine)
    outfile.close()