#!../venv/bin/python3
import torch
import math
import os
import sys
import numpy as np
import codecs, json
import matplotlib.pyplot as plt
from tqdm import tqdm


def debug_wait_key():
    # Debug / press any key to continue
    print("Press ANY key to continue...\n")
    input()

# Parameters
number_of_chars_in_raiting = 3
size_of_tensor = 768
number_of_cls = 10

input_size = number_of_cls * size_of_tensor

epoch = 10000

dataset_size = 100
testset_size = 10

learning_rate = 1e-4

# Some initial setup
print(f"Is cuda available {torch.cuda.is_available()}")

#device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#print(f"Device is : {device}")

print("Generating the model")

class SubModel(torch.nn.Module):

    def __init__(self):
        super(SubModel, self).__init__()

        self.linear1 = torch.nn.Linear(input_size, 32)
        self.activation = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(32, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.linear1(x)
        x = self.activation(x)
        x = self.linear2(x)
        x = self.sigmoid(x)
        return x


model = SubModel()

# Print the model
print("The model is")
print(model)

model = model.cuda()

#debug_wait_key()

loss_fn = torch.nn.MSELoss(reduction='sum').cuda()


criterion = torch.nn.BCELoss().cuda()
#criterion = torch.nn.CrossEntropyLoss().cuda()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)
#optimizer = torch.optim.Adam(model.parameters(), lr = 0.01)

# Load the dataset
# Pogledati torch.utils.data.DataLoader

path = os.path.join("..", "CLSembeddingsAll")
inFolder = os.listdir(path)
number_of_subs = len(inFolder)

dataset_x = np.zeros((dataset_size, input_size), dtype = np.float32)  # ulazni tenzori i att mask
dataset_y = np.zeros((dataset_size, 1), dtype = np.float32)  # rejting od 0.0 do 1.0

for index in tqdm(range(dataset_size), desc = 'Loading dataset'):
    movie = inFolder[index]
    json_input = open(os.path.join(path, movie), encoding='latin')

    json_load = json.load(json_input)
    L = np.array(json_load, dtype = np.float32)

    array = np.zeros((input_size), dtype = np.float32)

    cls_count = L.shape[0];
    # print(f"cls_count {cls_count}")

    # trim the end
    if cls_count > number_of_cls:
        cls_count = number_of_cls

    # print(f"cls_count {cls_count}")

    # print(f"type of array {array.shape}")
    # print(f"type of L {L.shape}")
    # print(f"cls * sot {cls_count * size_of_tensor}")

    array[0:(cls_count * size_of_tensor)] = L.flatten()[0:(cls_count * size_of_tensor)]
    
    # Ucitaj x
    dataset_x[index] = array


    # Ucitaj y
    tmp = float(movie[0:number_of_chars_in_raiting]) / 10.0
    # tensor = torch.tensor([tmp], dtype = torch.float32)

    dataset_y[index, 0] = tmp

dataset_x = torch.tensor(dataset_x).cuda()
dataset_y = torch.tensor(dataset_y).cuda()

print('Done loading')

testset_x = np.zeros((testset_size, input_size), dtype = np.float32)  # ulazni tenzori i att mask
testset_y = np.zeros((testset_size, 1), dtype = np.float32)  # rejting od 0.0 do 1.0

for index in tqdm(range(testset_size), desc = 'Loading testset'):
    movie = inFolder[dataset_size + index]
    json_input = open(os.path.join(path, movie), encoding='latin')

    json_load = json.load(json_input)
    L = np.array(json_load, dtype = np.float32)

    array = np.zeros((input_size), dtype = np.float32)

    cls_count = L.shape[0]
    # print(f"cls_count {cls_count}")

    # trim the end
    if cls_count > number_of_cls:
        cls_count = number_of_cls

    # print(f"cls_count {cls_count}")

    # print(f"type of array {array.shape}")
    # print(f"type of L {L.shape}")
    # print(f"cls * sot {cls_count * size_of_tensor}")

    array[0:(cls_count * size_of_tensor)] = L.flatten()[0:(cls_count * size_of_tensor)]
    
    # Ucitaj x
    testset_x[index] = array


    # Ucitaj y
    tmp = float(movie[0:number_of_chars_in_raiting]) / 10.0
    testset_y[index, 0] = tmp

testset_x = torch.tensor(testset_x).cuda()
testset_y = torch.tensor(testset_y).cuda()


print('Commencing training montage')

for epoch in tqdm(range(epoch), desc = 'Epochs'):
    #for index in range(dataset_size): 
    #x = dataset_x[index].cuda()
    y_pred = model.forward(dataset_x)

    # y = dataset_y[index].cuda()

    loss = criterion(y_pred, dataset_y)

    optimizer.zero_grad()

    

    if epoch % 1 == 0:
        print(f"Epoch {epoch}")
        y_pred = model.forward(testset_x)

        print(f"{testset_y}\n{y_pred}")

    loss.backward()

    optimizer.step()

print('Done training!')


