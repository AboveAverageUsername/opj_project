import os
import re

path = "C:\\Users\\tmp\\Desktop\\subsNoDupes"
inFolder = os.listdir(path)

count1 = 0
count2 = 0
count3 = 0
count4 = 0



for movie in inFolder:
    count1+=1
    print(count1)
    print(movie)
    tmpFile1 = open(path + "\\" + movie, encoding='latin')
    lines = tmpFile1.readlines()
    tmpFile1.close()
    
    outTxt = []
    
    for line in lines:
        if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
            
            if(line.count("Ð")>10 or line.count("FLAFILMS") > 0 or line.count("font color=") > 0 or line.count("@")>0 or line.count("Prevod:")>0 or line.upper().count("OBRADA I SINHRON")>0 or line.lower().count("opensubtitles")>0):
                true=True
            elif(line.lower().count("prevod i obrada")>0 or line.count("Milo Spasojeviæ")>0 or line.count("www.")>0 or line.lower().count("preveo")>0):
                true=True
            #elif(line == lines[-1] and (line[-1] !="." or line[-1] !="?" or line[-1] !="!" )):
                #true=True
            else:
                if(len(re.split("<[^>]*>", line)) > 1):
                    line = re.split("<[^>]*>", line)[1]
                if(len(re.split("{[^}]*}", line)) > 1):
                    fractured = re.split("{[^}]*}", line)
                    for seg in fractured:
                        if(seg != ""):
                            line = seg
                
                line = line.replace("- ","")
            
                
                
                
                outTxt.append(line)
                
    outFile = open("C:\\Users\\tmp\\Desktop\\test\\" +  movie + ".txt", "w",encoding='latin')
    outFile.writelines(outTxt)
    outFile.close
    #print(outTxt[-1])
    
print("done")    
    
    

    #if(line[0] == "1"):
        #count1+=1
    #elif(line[0] == "{"):
        #count2+=1
    #elif(line[0:4] == "ï»¿1"):
        #count3+=1        
    #else:
        #count4+=1
        #print(movie)
        #print(line)
    
    
    
#print(len(inFolder))
#print(count1)
#print(count2)
#print(count3)
#print(count4)