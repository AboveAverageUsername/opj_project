import json
import requests



link = "http://www.omdbapi.com/?t="
token = "&apikey="


f = open("namesYears.csv","r", encoding='utf-8')
lines = f.readlines()

allElemts = []

for line in lines:
    tmpLine = line.split(",")
    allElemts.append(tmpLine)
    print(line)

print(allElemts[-1])
print(len(allElemts))
f.close
print(allElemts[-1][1])
print(allElemts[-2][1])



responses = []
count = 0
for i in range(60001,len(allElemts)):
    req = requests.get(link + allElemts[i][0] + "&Year=" + allElemts[i][1] + token)
    count+=1
    print("request number: " , count)
    print(req)
    if(req.status_code == 200):
        fullResponse = req.text
        pythonDictionary = json.loads(fullResponse)
        responses.append(pythonDictionary)



#dump to json
print("dump to json")
with open("metadataPART4.json","w") as jsonFile:  
        backToJson = json.dump(responses, jsonFile)

print("done")
