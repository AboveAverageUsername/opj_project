import os
import re

path = "C:\\Users\\tmp\\Desktop\\Magnum corpus"
inFolder = os.listdir(path)


count = 0

regex = "^[" +"'"+ '"' +".,\-?ÄÑèÈÅ¡!æð0-9a-zA-Z\s]+$"
regex = "^[^.,\-?ÄÑèÈÅ¡!æð0-9a-zA-Z\s]+$"

upper = "Л"
lower = "л"




for movie in inFolder:
    #tmpFile1 = open(path + "\\" + movie, encoding='cp855')
    tmpFile1 = open(path + "\\" + movie, encoding='latin')
    lines = tmpFile1.readlines()
    tmpFile1.close()
    lcount = 0
    ympStr = lines[24][0:11]
    print(lines[20][0:-2])
    count+=1
    
    
    #for letter in ympStr:
        #if(lower == letter or upper == letter):
            #lcount+=1

    #if (lcount>2):
        #count+=1
        #print(count)
        #print(movie)
        #print(ympStr)
        #os.remove(path + "\\" + movie)

        
    
    #if(lines[7]== "\n" and lines[8]== "\n" and lines[9]== "\n" ):
        #print(movie)
        #os.remove(path + "\\" + movie)
        #count+=1
    
    #for line in lines:

print(count)
print("done")    
    
    
