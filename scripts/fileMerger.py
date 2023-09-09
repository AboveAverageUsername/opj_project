import json


with open("C:\\Users\\tmp\\Desktop\\metadataPART1.json","r") as file1:
    content1 = json.load(file1)
with open("C:\\Users\\tmp\\Desktop\\metadataPART2.json","r") as file2:
    content2 = json.load(file2)
with open("C:\\Users\\tmp\\Desktop\\metadataPART3.json","r") as file3:
    content3 = json.load(file3)
with open("C:\\Users\\tmp\\Desktop\\metadataPART4.json","r") as file4:
    content4 = json.load(file4)

# print(type(content1))

# print(len(content1))

# print("yeet")
# print(content1[0]['Title'])

allContent = content1 + content2 + content3 + content4

print(len(allContent))
print(allContent[-1]['Title'])

with open("C:\\Users\\tmp\\Desktop\\metadata.json","w") as jsonFile:  
        backToJson = json.dump(allContent, jsonFile)
print("done")
