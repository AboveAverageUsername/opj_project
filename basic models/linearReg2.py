import math
import os
import sys
import random
import pandas as pd 
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import f1_score


path = "C:/Users/tmp/Desktop/normalCLS"
inFolder = os.listdir(path)

independent = []
dependent = []
count = 0
for movie in inFolder:
    count+=1
    print(count)
    tmpFile1 = open(path + "/" + movie, encoding='latin')
    lines = tmpFile1.readline()
    tmpFile1.close()
    arr = lines.split(" ")
    floatArr = []
    for num in arr:
        floatArr.append(float(num))
    independent.append(floatArr)
    rating = float(movie[0:3])
    dependent.append(rating)



#frame = pd.DataFrame(cls)


Xtrain,Xtest,ytrain,ytest = train_test_split(independent, dependent, test_size=0.3, shuffle=True)

lr = LinearRegression()
lr.fit(Xtrain,ytrain)

predictY = lr.predict(Xtest)

print("predictY")
print(predictY)

values = ""

count = 0
total = 0
ty = []
predy = []

acurateCount = 0
for i in range(0,len(ytest)):
    count += 1
    total += abs(ytest[i] - predictY[i])
    values += str(predictY[i]) + " "
    ty.append(math.floor(ytest[i]))
    predy.append(math.floor(predictY[i]))
    if(math.floor(ytest[i]) == math.floor(predictY[i])):
        print()
        acurateCount += 1
print(acurateCount)
print(count)
accuracy = acurateCount/count
print(accuracy)
mae = total/count
print(mae)


tmpFile2 = open("C:/Users/tmp/Desktop/predictions.txt" , "w", encoding='latin')
tmpFile2.write(values)
tmpFile2.close()

print(math.sqrt(mean_squared_error(ytest, predictY)))

f1 = f1_score(ty, predy,average=None)
f2 = f1_score(ty, predy,average='micro')
f3 = f1_score(ty, predy,average='macro')
f4 = f1_score(ty, predy,average='weighted')

print(f1)
print(f2)
print(f3)
print(f4)

