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


def debug_wait_key():
    # Debug / press any key to continue
    print("Press ANY key to continue...\n")
    input()

def load(batch_size, number_of_batches, offset, path, inFolder):

    dataset_x = []
    dataset_y = []
    
    for batch in tqdm(range(number_of_batches), desc = 'Loading batches'):

        batch_x = np.zeros((batch_size, input_size), dtype = np.float32)  # ulazni tenzori i att mask
        batch_y = np.zeros((batch_size, 1), dtype = np.float32)  # rejting od 0.0 do 1.0

        for index in range(batch_size):

            movie = inFolder[offset + batch * batch_size + index]
            json_input = open(os.path.join(path, movie), encoding='latin')

            json_load = json.load(json_input)
            L = np.array(json_load, dtype = np.float32)

            array = np.zeros((input_size), dtype = np.float32)

            cls_count = L.shape[0]

            # trim the end
            if cls_count > number_of_cls:
                cls_count = number_of_cls

            array[0:(cls_count * size_of_tensor)] = L.flatten()[0:(cls_count * size_of_tensor)]
            
            # Ucitaj x
            batch_x[index] = array

            # Ucitaj y
            tmp = float(movie[0:number_of_chars_in_raiting]) / 10.0
<<<<<<< HEAD

=======
>>>>>>> 7cca136623 (cv)
            batch_y[index, 0] = tmp

        batch_x = torch.tensor(batch_x)
        batch_y = torch.tensor(batch_y)

        dataset_x.append(batch_x)
        dataset_y.append(batch_y)

    return (dataset_x, dataset_y)

# Parameters
number_of_chars_in_raiting = 3
size_of_tensor = 768
number_of_cls = 30

input_size = number_of_cls * size_of_tensor

epoch = 1000

<<<<<<< HEAD
dataset_batch_size = 200
=======
dataset_batch_size = 240
>>>>>>> 7cca136623 (cv)
dataset_number_of_batches = 100
dataset_size = dataset_number_of_batches * dataset_batch_size

testset_batch_size = 100
testset_number_of_batches = 10
testset_size = testset_number_of_batches * testset_batch_size

learning_rate = 1e-6

# Some initial setup
print(f"Is cuda available {torch.cuda.is_available()}")

#device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#print(f"Device is : {device}")

print("Generating the model")

class SubModel(torch.nn.Module):

    def __init__(self):
        super(SubModel, self).__init__()

        self.linear1 = torch.nn.Linear(input_size, 64)
        self.activation1 = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(64, 32)
        self.activation2 = torch.nn.ReLU()
        self.linear3 = torch.nn.Linear(32, 16)
        self.activation3 = torch.nn.ReLU()
        self.linear4 = torch.nn.Linear(16, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.linear1(x)
        x = self.activation1(x)
        x = self.linear2(x)
        x = self.activation2(x)
        x = self.linear3(x)
        x = self.activation3(x)
        x = self.linear4(x)
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

print('Loading dataset!')
path = os.path.join("..", "CLSembeddingsAll")
inFolder = os.listdir(path)
number_of_subs = len(inFolder)

(dataset_x, dataset_y) = load(dataset_batch_size, dataset_number_of_batches,
        0,
        path,
        inFolder)

print('Loading testset!')
(testset_x, testset_y) = load(testset_batch_size, testset_number_of_batches,
<<<<<<< HEAD
        testset_size,
=======
        dataset_size,
>>>>>>> 7cca136623 (cv)
        path,
        inFolder)

print('Done loading')

print('Commencing training montage')

for epoch in tqdm(range(epoch), desc = 'Epochs'):
    for batch in range(dataset_number_of_batches):

        y_pred = model(dataset_x[batch].cuda())

        loss = criterion(y_pred, dataset_y[batch].cuda())

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

<<<<<<< HEAD
    #if epoch % 10 == 0:
    #    model.eval()
    #    for batch in range(testset_number_of_batches):
    #        y_pred = model.forward(testset_x[batch].cuda())
    #        loss = criterion(y_pred, testset_y[batch].cuda())
    #    tqdm.write(f"Epoch {epoch} loss = {loss}")
=======
    if epoch % 10 == 0:
        model.eval()
        outputs = []

        for batch in range(testset_number_of_batches):
            y_pred = model(testset_x[batch].cuda())
            mean = metrics.mean_absolute_error(
                    testset_y[batch].cpu().numpy(), 
                    y_pred.detach().cpu().numpy()
                    )
            outputs.append(mean)

        loss = sum(outputs) / len(outputs)
        tqdm.write(f"Epoch {epoch} loss = {loss}")
        model.train()
>>>>>>> 7cca136623 (cv)

print('Done training!')

torch.save(model.state_dict(), os.path.join(".", "model"))

# Loading is done like so
# model = SubModel()
# model.load_state_dict(torch.load(os.path.join(".", "model"))
# model.eval()

print('Model saved!')
print('Printing evaluation!')
model.eval()

outputs = []
for batch in range(testset_number_of_batches):
    y_pred = model(testset_x[batch].cuda())
<<<<<<< HEAD
    # loss = criterion(y_pred, testset_y[batch].cuda())
    # diff = abs( - y_pred)
    # outputs.append(sum(diff) / len(diff))
=======
>>>>>>> 7cca136623 (cv)
    mean = metrics.mean_absolute_error(
            testset_y[batch].cpu().numpy(), 
            y_pred.detach().cpu().numpy()
            )

    outputs.append(mean)
<<<<<<< HEAD
    # tqdm.write(f"{epoch} loss = {loss}")
=======
>>>>>>> 7cca136623 (cv)

final = sum(outputs) / len(outputs)

print(f"Final accuracy = {final * 10.0}")
