from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
import math
import os
import sys
import random
import torch
from sklearn.model_selection import train_test_split

print(f"Is cuda available {torch.cuda.is_available()}")

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

path = "C:\\Users\\tmp\\Desktop\\train"
path2 = "C:\\Users\\tmp\\Desktop\\test"
outPath = "C:\\Users\\tmp\\Desktop\\linearReg"
inFolder = os.listdir(path)

names = []
txts = []

count = 0
for movie in inFolder:
    count+=1
    print(count)
    tmpFile1 = open(path + "\\" + movie, encoding='latin')
    lines = tmpFile1.readline()
    tmpFile1.close()
    names.append(movie)
    txts.append(lines)

data =  []
for i in range(0,len(names)):
    tmpList = [txts[i], float(names[i][0:3])]
    data.append(tmpList)

data_df = pd.DataFrame(data)
data_df.columns = ["text", "labels"]

train,test = train_test_split(data_df, test_size=0.3, shuffle=True)

model_args = ClassificationArgs()
model_args.num_train_epochs = 3
model_args.regression = True

model = ClassificationModel(
    "roberta",
    "roberta-base",
    num_labels=1,
    use_cuda=True,
    args=model_args
)

model.train_model(train,overwrite_output_dir = True)

# Evaluate the 
result, model_outputs, wrong_predictions = model.eval_model(test)

print("========================================================================================")
print("result")
print(result)
print(type(result))
tmpFile2 = open(outPath + "\\" + "result.txt", 'w', encoding='latin')
tmpFile2.write(str(result))
tmpFile2.close()
print("========================================================================================")
print("model_outputs")
print(model_outputs)
print(type(model_outputs))
tmpFile3 = open(outPath + "\\" + "model_outputs.txt", 'w', encoding='latin')
tmpFile3.write(str(model_outputs))
tmpFile3.close()
print("========================================================================================")
print("wrong_predictions")
print(type(wrong_predictions))
tmpFile4 = open(outPath + "\\" + "wrong_predictions.txt", 'w', encoding='latin')
tmpFile4.write(str(wrong_predictions))
tmpFile4.close()
print("========================================================================================")



count = 0
ratings = []
txts2 = []

inFolder = os.listdir(path2)
for movie in inFolder:
    count+=1
    print(count)
    tmpFilez = open(path2 + "\\" + movie, encoding='latin')
    lines = tmpFilez.readline()
    tmpFilez.close()
    ratings.append(float(movie[0:3]))
    txts2.append(lines)

print("expectedVals")
print(type(ratings))
tmpFile2 = open(outPath + "\\" + "expectedVals.txt", 'w', encoding='latin')
tmpFile2.write(str(ratings))
tmpFile2.close()


predictions, raw_outputs = model.predict(txts2)





pred = []
for p in predictions:
    pred.append(p)

print("predictions")
print(type(predictions))
tmpFile2 = open(outPath + "\\" + "predictions.txt", 'w', encoding='latin')
tmpFile2.write(str(pred))
tmpFile2.close()
print("========================================================================================")
print("raw_outputs")
print(type(raw_outputs))
tmpFile2 = open(outPath + "\\" + "raw_outputs.txt", 'w', encoding='latin')
tmpFile2.write(str(raw_outputs))
tmpFile2.close()

