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
number_of_cls = 40

input_size = number_of_cls * size_of_tensor * 2

epoch = 10

dataset_size = 1000

# Some initial setup
print(f"Is cuda available {torch.cuda.is_available()}")

#device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#print(f"Device is : {device}")

print("Generating the model")

model = torch.nn.Sequential(
    #torch.nn.Linear(input_size,
    #    input_size),

    torch.nn.Linear(input_size, 1).cuda()
)
# Print the model
print("The model is")
print(model)

model = model.cuda()

#debug_wait_key()

loss_fn = torch.nn.MSELoss(reduction='sum').cuda()

learning_rate = 1e-6

criterion = torch.nn.CrossEntropyLoss().cuda()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

# Load the dataset
# Pogledati torch.utils.data.DataLoader

path = os.path.join("..", "CLSembeddingsAll")
inFolder = os.listdir(path)
number_of_subs = len(inFolder)

dataset_x = []  # ulazni tenzori i att mask
dataset_y = []  # rejting od 0.0 do 1.0

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
    tensor = torch.from_numpy(array)
    dataset_x.append(tensor)


    # Ucitaj y
    tmp = float(movie[0:number_of_chars_in_raiting])
    tensor = torch.tensor([tmp], dtype = torch.float32)

    dataset_y.append(tensor)


print('Done loading')

# debug_wait_key()

print('Commencing training montage')

for epoch in tqdm(range(epoch), desc = 'Epochs'):
    for index in range(dataset_size): 
        x = dataset_x[index].cuda()
        y_pred = model(x)

        y = dataset_y[index].cuda()

        loss = criterion(y_pred, y)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

print('Done!')

