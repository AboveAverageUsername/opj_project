import os
import shutil
import pysrt


path = "C:\\Users\\tmp\\Desktop\\subs"
folders = os.listdir(path)


count = 0
tmpStr = ""
for movie in folders:
    #print(movie)
    subPath = path + "\\" + movie
    subFolder = os.listdir(subPath)
    
    
    for file in subFolder:
        if file[-3:-1] + file[-1] == "nfo":
            tmpFile1 = open(subPath + "\\" + file, encoding='utf8')
            read = tmpFile1.readlines()
            tmpStr = read[23][20:23]  
            
            tmpFile1.close

            
        if file[-3:-1] + file[-1] != "nfo":
            tmpFile = open(subPath + "\\" + file, encoding='latin')
            read = tmpFile.readlines()
            tmpFile.close()
            
            outFile = open("C:\\Users\\tmp\\Desktop\\subsNoDupes\\" + tmpStr + "      "  +  movie + ".txt", "w",encoding='latin')
            outFile.writelines(read)
            outFile.close

            

            count+=1
            print(count)

    
print(count)