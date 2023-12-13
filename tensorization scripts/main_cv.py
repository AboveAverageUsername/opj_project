#!../venv/bin/python3
import torch
import math
import os
import sys
import numpy as np
import codecs, json
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn import metrics
from sklearn.model_selection import KFold
from torch.optim.lr_scheduler import ExponentialLR

def debug_wait_key():
    # Debug / press any key to continue
    print("Press ANY key to continue...\n")
    input()

def load(offset, dataset_size, path, inFolder):

    dataset_x = np.zeros(
                (dataset_size, input_size), 
                dtype = np.float32)
    dataset_y = np.zeros(
                (dataset_size, 1), 
                dtype = np.float32)
    
    for index in tqdm(range(dataset_size), desc = 'Loading dataset'):

        x = np.zeros(
                input_size, 
                dtype = np.float32)  # ulazni tenzori
        y = np.zeros(
                1, 
                dtype = np.float32)  # rejting od 0.0 do 1.0

        movie = inFolder[offset + index]
        json_input = open(os.path.join(path, movie), encoding='latin')

        json_load = json.load(json_input)
        L = np.array(json_load, dtype = np.float32)

        array = np.zeros((input_size), dtype = np.float32)

        cls_count = L.shape[0]

        # trim the end
        if cls_count > number_of_cls:
            cls_count = number_of_cls

        array[0:(cls_count * size_of_tensor)] = L.flatten()[
                0:(cls_count * size_of_tensor)]
        
        # Ucitaj x
        dataset_x[index] = array

        # Ucitaj y
        tmp = float(movie[0:number_of_chars_in_raiting]) / 10.0

        dataset_y[index, 0] = tmp

    return (np.array(dataset_x), np.array(dataset_y))

# Parameters
RANDOM_SEED = 8

number_of_chars_in_raiting = 3
size_of_tensor = 768
number_of_cls = 30

input_size = number_of_cls * size_of_tensor

epoch = 1000

dataset_batch_size = 1000
dataset_size = 24000

testset_batch_size = 100
testset_size = 1000

learning_rate = 1e-2

# Some initial setup
print(f"Is cuda available {torch.cuda.is_available()}")

#device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#print(f"Device is : {device}")

print("Generating the model")

class SubModel(torch.nn.Module):

    def __init__(self):
        super(SubModel, self).__init__()

        self.linear1 = torch.nn.Linear(input_size, 4096)
        self.activation1 = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(4096, 1024)
        self.activation2 = torch.nn.ReLU()
        self.linear3 = torch.nn.Linear(1024, 1024)
        self.activation3 = torch.nn.ReLU()
        self.linear4 = torch.nn.Linear(1024, 256)
        self.activation4 = torch.nn.ReLU()
        self.linear5 = torch.nn.Linear(256, 256)
        self.activation5 = torch.nn.ReLU()
        self.linear6 = torch.nn.Linear(256, 256)
        self.activation6 = torch.nn.ReLU()
        self.linear7 = torch.nn.Linear(256, 128)
        self.activation7 = torch.nn.ReLU()
        self.linear8 = torch.nn.Linear(128, 128)
        self.activation8 = torch.nn.ReLU()
        self.linear9 = torch.nn.Linear(128, 128)
        self.activation9 = torch.nn.ReLU()
        self.linear10 = torch.nn.Linear(128, 128)
        self.activation10 = torch.nn.ReLU()
        self.linear11 = torch.nn.Linear(128, 64)
        self.activation11 = torch.nn.ReLU()
        self.linear12 = torch.nn.Linear(64, 64)
        self.activation12 = torch.nn.ReLU()
        self.linear13 = torch.nn.Linear(64, 64)
        self.activation13 = torch.nn.ReLU()
        self.linear14 = torch.nn.Linear(64, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.linear1(x)
        x = self.activation1(x)
        x = self.linear2(x)
        x = self.activation2(x)
        x = self.linear3(x)
        x = self.activation3(x)
        x = self.linear4(x)
        x = self.activation4(x)
        x = self.linear5(x)
        x = self.activation5(x)
        x = self.linear6(x)
        x = self.activation6(x)
        x = self.linear7(x)
        x = self.activation7(x)
        x = self.linear8(x)
        x = self.activation8(x)
        x = self.linear9(x)
        x = self.activation9(x)
        x = self.linear10(x)
        x = self.activation10(x)
        x = self.linear11(x)
        x = self.activation11(x)
        x = self.linear12(x)
        x = self.activation12(x)
        x = self.linear13(x)
        x = self.activation13(x)
        x = self.linear14(x)
        x = self.sigmoid(x)
        return x


model = SubModel()
# Loading is done like so
# model = SubModel()
# model.load_state_dict(torch.load(os.path.join(".", "model")))
# model.eval()

# Print the model
print("The model is")
print(model)

model = model.cuda()

#debug_wait_key()

loss_fn = torch.nn.MSELoss(reduction='sum').cuda()


criterion = torch.nn.BCELoss().cuda()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
scheduler = ExponentialLR(optimizer, gamma=0.8)

# Load the dataset
# Pogledati torch.utils.data.DataLoader

print('Loading dataset!')
path = os.path.join("..", "CLSembeddingsAll")
inFolder = os.listdir(path)
number_of_subs = len(inFolder)

(dataset_x, dataset_y) = load(
        0,
        dataset_size,
        path,
        inFolder)

print('Loading testset!')
(testset_x, testset_y) = load(
        dataset_size,
        testset_size,
        path,
        inFolder)

print('Done loading')

print('Commencing training montage')

cv = KFold(n_splits=5, shuffle=True, random_state=RANDOM_SEED)
for epoch in tqdm(range(epoch), desc='Epochs'):

    outputs = []
    
    for train_index, test_index in cv.split(dataset_x):
        x_train, x_test = dataset_x[train_index, :], dataset_x[test_index, :]
        y_train, y_test = dataset_y[train_index], dataset_y[test_index]

        num_batches = math.ceil(x_train.shape[0]/dataset_batch_size)
        x_list = np.split(x_train, num_batches)
        y_list = np.split(y_train, num_batches)

        for batch in range(num_batches):
            x = torch.tensor(x_list[batch]).cuda()
            y = torch.tensor(y_list[batch]).cuda()
            y_pred = model(x)

            loss = criterion(y_pred, y)

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

        # Evaluate the model
        model.eval()

        y_pred = model(torch.tensor(x_test).cuda())

        mean = metrics.mean_absolute_error(
                y_test,
                y_pred.detach().cpu().numpy()
                )

        outputs.append(mean)
        
        # End model evaluation
        model.train()

    final = sum(outputs) / len(outputs) * 10.0
    tqdm.write(f"Epoch {epoch:05} MSE = {final}")

    if epoch < 40:
        scheduler.step()


print('Done training!')

torch.save(model.state_dict(), os.path.join(".", "model"))



print('Model saved!')
print('Printing evaluation!')
model.eval()

outputs = []

num_batches = math.ceil(testset_x.shape[0]/testset_batch_size)
x_list = np.split(testset_x, num_batches)
y_list = np.split(testset_y, num_batches)

for batch in range(num_batches):
    y_pred = model(torch.tensor(x_list[batch]).cuda())

    mean = metrics.mean_absolute_error(
            y_list[batch],
            y_pred.detach().cpu().numpy()
            )

    outputs.append(mean)

final = sum(outputs) / len(outputs) * 10.0

print(f"Final accuracy = {final}")
