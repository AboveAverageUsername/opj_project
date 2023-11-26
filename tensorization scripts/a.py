from transformers import BertTokenizer, TFBertModel
import tensorflow as tf
import torch
import math
import os
import sys
import numpy as np

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

        if(block < blocks):
            
            
            tmpArr = [101] + input_ids[slide:(slide+510)] + [102]
            slide += 510
            returnArr.append(tmpArr)

        
        else:
            tmpArr = [101] + input_ids[slide:-1] + [input_ids[-1]] + ([0] * (510 - lastBlockLen)) + [102]
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
    
    for i in range(1,blocks + buffer):

        returnMasks.append(arr[slide:(slide+512)])
        slide += 512

    return returnMasks

    
    
def getCLS(idBlocks,attentionBlocks,movie):
    
    listOfTensors = []
    
    for block in range (0, len(idBlocks)):
        #print(block)
        
    


        dict1 = {
            'input_ids' : tf.convert_to_tensor([idBlocks[block]]),
            'attention_mask' :  tf.convert_to_tensor([attentionBlocks[block]]),
            'output_hidden_states' : True
        }
  
        
        outputs = model(**dict1)

        #print(len(outputs))
        #print(len(outputs[0]))
        #print(len(outputs[0][0]))
        #print(len(outputs[0][0][0]))
        
        last_hidden_states = outputs.hidden_states[-1]

        listOfTensors.append(last_hidden_states[:,0,:])
        
    #print(listOfTensors)
    
    
    clsAvg = np.mean(np.concatenate((listOfTensors[:]), axis=0), axis=0)
    clsTensor = tf.convert_to_tensor([clsAvg])
    #print(clsTensor)
    #print(type(clsTensor))
    
    np.savetxt( "C:\\Users\\tmp\\Desktop\\CLSembeddings\\" + movie, clsTensor.numpy())





    


#=======================================================================================================================




path = "C:\\Users\\tmp\\Desktop\\stemStr"
inFolder = os.listdir(path)



#tmpFile1 = open(path)
#line = tmpFile1.readline()
#tmpFile1.close()

#arr = list(line)
#=======================================================================================================================

count = 0
for movie in inFolder:
    count+=1
    print(count)
    
    tmpFile1 = open(path + "\\" + movie, encoding='latin')

    text = tmpFile1.readline()
    tmpFile1.close()
    
    
    encoded_input = tokenizer(text, add_special_tokens=False)
    
    idBlocks = separatorID(encoded_input['input_ids'])
    attentionBlocks = separatorMask(encoded_input['attention_mask'])

    
    
    cutLastTXT = movie[0:-4]
    getCLS(idBlocks,attentionBlocks, cutLastTXT)



    







#output = model(encoded_input)


#print(output)
#print()
#print()
#print()
#print(len(output[0]))
#print(len(output[0][0][0]))
