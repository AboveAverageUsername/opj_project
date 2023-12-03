#!../venv/bin/python3
#import tensorflow as tf
#from transformers import BertTokenizer, TFBertModel
# import torch
import math
import os
import sys
import numpy as np
import codecs, json
import matplotlib.pyplot as plt
from tqdm import tqdm

CLS = 101
SEP = 102
PAD = 0

# Debug / press any key to continue
# print("Press ANY key to continue...\n")
# input()

path = os.path.join("..", "CLSembeddingsAll")
inFolder = os.listdir(path)



#==============================================================================
checkpoint = 0
current_max = 0

number_of_subs = len(inFolder)
cls_counts = np.zeros((number_of_subs), dtype=np.int32)

for index, movie in tqdm(enumerate(inFolder), total = number_of_subs, desc = 'Loading CLS counts'):
    if index < checkpoint:
        print(f"Skipping to checkpoint {index}\t\t{movie}")
        continue
    
    json_input = open(os.path.join(path, movie), encoding='latin')
    L = json.load(json_input)
    array = np.array(L)

    cls_counts[index] = array.shape[0];

    json_input.close()

cls_max = np.max(cls_counts)

print(f"FINAL RESULT IS {cls_max} CLS TOKENS!!!")

plt.hist(cls_counts, bins=cls_max)
plt.title("Histogram broja CLS embedinga")
plt.savefig(os.path.join(".", "hist_cls_counts.pdf"))
plt.show()

