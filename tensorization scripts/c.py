#!../venv/bin/python3
import tensorflow as tf
from transformers import BertTokenizer, TFBertModel
# import torch
import math
import os
import sys
import numpy as np
import codecs, json

CLS = 101
SEP = 102
PAD = 0

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Debug / press any key to continue
# print("Press ANY key to continue...\n")
# input()

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

model = TFBertModel.from_pretrained("bert-base-multilingual-cased")
#=======================================================================================================================
#Functions
def separatorID(input_ids):
    returnArr = []
    
    size = len(input_ids)
    lastBlockLen = size % 510
    if(lastBlockLen == 0):
        lastBlockLen = 510
        
    blocks = math.ceil(size/510)
    
    slide = 0
    for block in range(1, blocks + 1):
        tmpArr = []

        if block < blocks:

            tmpArr = [CLS] + input_ids[slide:(slide+510)] + [SEP]
            # print(tokenizer.decode(tmpArr))

            slide += 510
            returnArr.append(tmpArr)

        else:
            tmpArr = [CLS] + input_ids[slide:] + ([PAD] * (510 - lastBlockLen)) + [SEP]
            # print(tokenizer.decode(tmpArr))
            returnArr.append(tmpArr)

    return returnArr

        

def separatorMask(attention_masks):
    returnMasks = []
    arr = attention_masks
    size = len(attention_masks)
    invlastBlock = 510 - (size % 510)
    
    blocks = math.floor(size/510)
    
    if(invlastBlock == 0):
        arr += [1]*(blocks*2)
    
    else:
        arr += [1]*(blocks*2) + [1] + [0]*invlastBlock + [1]
    
    buffer = 2
    
    if(invlastBlock == 510):
        buffer = 1
    
    slide = 0
    
    for i in range(1, blocks + buffer):
        returnMasks.append(arr[slide:(slide+512)])
        slide += 512

    return returnMasks


def getCLS(idBlocks,attentionBlocks,movie):
    
    listOfTensors = []
    
    for block in range (0, len(idBlocks)):
        #print(block)

        dict1 = {
            'input_ids': tf.convert_to_tensor([idBlocks[block]]),
            'attention_mask':  tf.convert_to_tensor([attentionBlocks[block]]),
            'output_hidden_states': True
        }
        with tf.device('/gpu:0'):
            outputs = model(**dict1)

        #print(len(outputs))
        #print(len(outputs[0]))
        #print(len(outputs[0][0]))
        #print(len(outputs[0][0][0]))
        
        last_hidden_states = outputs.hidden_states[-1]

        listOfTensors.append(last_hidden_states[:, 0, :].numpy()[0].tolist())
        
    #print(listOfTensors)
    
    
    # clsAvg = np.mean(np.concatenate((listOfTensors[:]), axis=0), axis=0)
    # clsTensor = tf.convert_to_tensor([clsAvg])
    #print(clsTensor)
    #print(type(clsTensor))
    
    # Old way of saving a tensor
    # np.savetxt(os.path.join("..", "CLSembeddingsAll", movie), listOfTensors[:])

    # We do it the JSON way now babyyy

    path = os.path.join("..", "CLSembeddingsAll", movie)

    json.dump(listOfTensors, codecs.open(path, 'w', encoding='utf-8'),
            separators=(',', ':'),
            sort_keys=False,
            indent=4)





    


#=======================================================================================================================




path = os.path.join("..", "stemStr")
inFolder = os.listdir(path)



#tmpFile1 = open(path)
#line = tmpFile1.readline()
#tmpFile1.close()

#arr = list(line)
#=======================================================================================================================
checkpoint = 18320
count = 0
for movie in inFolder:
    count+=1
    print(f"{count}\t\t{movie}")
    if count < checkpoint:
        continue
    
    tmpFile1 = open(os.path.join(path, movie), encoding='latin')

    text = tmpFile1.readline()
    tmpFile1.close()

    encoded_input = tokenizer(text, add_special_tokens=False)
    # print(encoded_input)
    idBlocks = separatorID(encoded_input['input_ids'])
    attentionBlocks = separatorMask(encoded_input['attention_mask'])

    
    
    cutLastTXT = movie[0:-4]
    getCLS(idBlocks, attentionBlocks, cutLastTXT)
