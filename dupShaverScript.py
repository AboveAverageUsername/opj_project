

f = open("moviesOnly.csv","r", encoding='utf-8')
lines = f.readlines()

nameList = []
yearList = []
allElemts = []

for line in lines:
    tmpLine = line.split(",")
    
    if(not allElemts or allElemts[-1][1] != tmpLine[1]):
        allElemts.append(tmpLine)
        print(line)
    else:
        a=1

#print("nameList size: " , len(nameList) , " last element: " , nameList[-1])
#print("yearList size: " , len(yearList) , " last element: " , yearList[-1])
print(allElemts[-1])
print(len(allElemts))
f.close

outfile = open("moviesOnlyNoDupes.csv", "w", encoding='utf-8')

for elem in allElemts:
    newLine = ""
    for i in elem:
        newLine += i
        newLine += ","

    outfile.writelines(newLine)
outfile.close