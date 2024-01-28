import math
import os
import sys
import random
import pandas as pd 
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
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
    avg = sum(floatArr)/len(floatArr)
    independent.append([avg])
    rating = int(movie[0])
    dependent.append(rating)
    
print("#")
print(len(dependent)) 
print(len(independent)) 
Xtrain,Xtest,ytrain,ytest = train_test_split(independent, dependent, test_size=0.3, shuffle=True)


model = GaussianNB()

model.fit(Xtrain, ytrain)

predY = model.predict(Xtest)
print(predY)

correct = 0
for i in range(0,len(ytest)):
    if(ytest[i] == predY[i]):
        correct+=1
accuracy = correct/len(ytest)

f1 = f1_score(ytest, predY,average= None)
f2 = f1_score(ytest, predY,average='micro')
f3 = f1_score(ytest, predY,average='macro')
f4 = f1_score(ytest, predY,average='weighted')


print("MAE: " , mean_absolute_error(ytest, predY))
print("RMSE: " , math.sqrt(mean_squared_error(ytest, predY)))
print("Acuracy: " , accuracy)
print("F1 None: ", f1)
print("F1 micro: ", f2)
print("F1 macro: ", f3)
print("F1 weighted: ", f4)
