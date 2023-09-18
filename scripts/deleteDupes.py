import os
import shutil


path = "C:\\Users\\tmp\\Desktop\\Subs"
folders = os.listdir(path)

count = 0
prevStr = ""
for movie in folders:
    tmpStr = ""
    flag = True
    
    for char in movie:
        if(flag and char != '('):
            tmpStr += char
        else:
            flag = False
    
    
    if (tmpStr == prevStr):
        print(movie)
        count+=1
        shutil.rmtree(path+ "\\" + movie)
        #os.remove(path+ "\\" + movie)
    prevStr = tmpStr
       


print(count)