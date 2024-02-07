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
from sklearn.utils import resample
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from torch.optim.lr_scheduler import ExponentialLR
import torchmetrics

# Parameters
RANDOM_SEED = 8

number_of_chars_in_raiting = 3
size_of_tensor = 768
number_of_cls = 32

input_size = number_of_cls * size_of_tensor

epoch = 100

dataset_batch_size = 8
dataset_size = 25000

testset_size = 1000

learning_rate = 1e-2

do_training = False

classes = (
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        )
labels = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        ]

# GUI event loop
plt.ion()
figure, ax = plt.subplots(figsize=(10, 8))

# Functions
def debug_wait_key():
    # Debug / press any key to continue
    print("Press ANY key to continue...\n")
    input()

def plot_conf_mat(y_pred, y_test):
    ax.clear()
    
    disp = metrics.ConfusionMatrixDisplay.from_predictions(
            y_pred,
            y_test,
            display_labels=classes,
            normalize='all',
            ax=ax,
            colorbar=False
            )
    figure.canvas.draw()
    figure.canvas.flush_events()



def convert_score_to_class(score):
    class_index = math.floor(score) - 1
    if class_index < 0 or class_index >= len(classes):
        return 0
    return class_index

def load(offset, dataset_size, path, inFolder):

    dataset_x = np.zeros(
                (dataset_size, size_of_tensor, number_of_cls), 
                dtype = np.float32)
    #dataset_y = np.zeros(
    #            (dataset_size, len(classes)), 
    #            dtype = np.float32)
    dataset_y_int = np.zeros(
                dataset_size, 
                dtype = np.integer)
    
    for index in tqdm(range(dataset_size), desc = 'Loading dataset'):

        x = np.zeros(
                (size_of_tensor, number_of_cls), 
                dtype = np.float32)  # ulazni tenzori

        #y = np.zeros(
        #        len(classes), 
        #        dtype = np.float32)  # ulazni tenzori

        movie = inFolder[offset + index]
        json_input = open(os.path.join(path, movie), encoding='latin')

        json_load = json.load(json_input)
        L = np.array(json_load, dtype = np.float32)

        cls_count = L.shape[0]

        # trim the end
        if cls_count > number_of_cls:
            cls_count = number_of_cls

        x[:, 0:cls_count] = np.transpose(L[0:cls_count, :])
        
        # Ucitaj x
        dataset_x[index] = x

        # Ucitaj y
        tmp = float(movie[0:number_of_chars_in_raiting])
        clas = convert_score_to_class(tmp)

        #y[clas] = 1.0
        #dataset_y[index] = y
        dataset_y_int[index] = clas

    # Normalize
    final_dataset_x = np.empty((0, size_of_tensor, number_of_cls), dtype=np.float32)
    final_dataset_y = np.empty((0, len(classes)), dtype=np.float32)

    for i in range(0, len(classes)):
        odvojena_klasa = dataset_x[dataset_y_int == i]
        odvojena_klasa_resample = resample(odvojena_klasa, n_samples=6000, random_state=42)
        # np.full(odvojena_klasa_resample.shape[0], i, dtype=np.integer)

        resample_y = np.zeros(
                (len(odvojena_klasa_resample), len(classes)), 
                dtype = np.float32)

        resample_y[:,i] = 1.0

        final_dataset_x = np.concatenate((final_dataset_x, odvojena_klasa_resample), axis=0)
        final_dataset_y = np.concatenate((final_dataset_y, resample_y), axis=0)

    print(f"x shape {final_dataset_x.shape}")
    print(f"y shape {final_dataset_y.shape}")

    return (final_dataset_x, final_dataset_y)


# Some initial setup
print(f"Is cuda available {torch.cuda.is_available()}")

#device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#print(f"Device is : {device}")

print("Generating the model")

class SubModel(torch.nn.Module):

    def __init__(self):
        super(SubModel, self).__init__()

        self.transformer_encoder = torch.nn.TransformerEncoderLayer(d_model=number_of_cls, nhead=8)
        self.transformer = torch.nn.TransformerEncoder(self.transformer_encoder, num_layers=6)
        self.linear0 = torch.nn.Linear(number_of_cls * size_of_tensor, len(classes))
        self.smax = torch.nn.Softmax(dim=0)

    def forward(self, x):
        x = self.transformer(x)
        x = torch.flatten(x, start_dim=1)
        x = self.linear0(x)
        x = self.smax(x)
        return x


model = SubModel()
# Loading is done like so
# model = SubModel()
if not do_training:
    model.load_state_dict(torch.load(os.path.join(".", "model")))
    model.eval()

# Print the model
print("The model is")
print(model)

model = model.cuda()

#debug_wait_key()

loss_fn = torch.nn.CrossEntropyLoss().cuda()


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

(dataset_x, testset_x, dataset_y, testset_y) = train_test_split(dataset_x, dataset_y, test_size=0.2, random_state=42)

print('Done loading')


if do_training:
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

            num_test_batches = math.ceil(x_test.shape[0]/dataset_batch_size)
            x_test_list = np.split(x_test, num_test_batches)

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

            # y_pred_all = np.zeros(y_test.shape)
            y_pred_all_tensor = torch.empty((0)).cpu()

            for batch in range(num_test_batches):

                y_pred = model(torch.tensor(x_test_list[batch]).cuda()).detach().cpu()

                y_pred_all_tensor = torch.cat((y_pred_all_tensor, y_pred.cpu()), dim=0)

                # y_pred_all[batch * dataset_batch_size : (batch + 1) * dataset_batch_size] = y_pred


            y_test_tmp = torch.argmax(torch.tensor(y_test), 1)
            #y_pred = np.argmax(y_pred_all, axis=1)
            y_pred_all_tensor = torch.argmax(y_pred_all_tensor, 1)

            acc = torchmetrics.Accuracy(task="multiclass", num_classes=len(classes))
            val = acc(y_pred_all_tensor, y_test_tmp)
            conf = torchmetrics.ConfusionMatrix(task="multiclass", num_classes=len(classes))
            # print(y_test_tmp)
            # print(y_pred)

            tqdm.write(str(val))
            tqdm.write(str(conf(y_pred_all_tensor, y_test_tmp)))

            # plot_conf_mat(y_pred, y_test_tmp)

            # End model evaluation
            model.train()

        if epoch < 40:
            scheduler.step()


    print('Done training!')

    torch.save(model.state_dict(), os.path.join(".", "model"))
    print('Model saved!')

print('Printing evaluation!')
model.eval()

num_batches = math.ceil(testset_x.shape[0]/dataset_batch_size)
x_list = np.split(testset_x, num_batches)
#y_list = np.split(y_train, num_batches)

y_pred_all_tensor = torch.empty((0)).cpu()

for batch in range(num_batches):

    y_pred = model(torch.tensor(x_list[batch]).cuda()).detach().cpu()

    y_pred_all_tensor = torch.cat((y_pred_all_tensor, y_pred.cpu()), dim=0)

y_test_tmp = torch.argmax(torch.tensor(testset_y), 1)
y_pred_all_tensor = torch.argmax(y_pred_all_tensor, 1)

acc = torchmetrics.Accuracy(task="multiclass", num_classes=len(classes))
f1_socre_micro = torchmetrics.classification.F1Score(task="multiclass", num_classes=len(classes), average='micro')
f1_socre_macro = torchmetrics.classification.F1Score(task="multiclass", num_classes=len(classes), average='macro')
f1_socre_weighted = torchmetrics.classification.F1Score(task="multiclass", num_classes=len(classes), average='weighted')
val = acc(y_pred_all_tensor, y_test_tmp)
conf = torchmetrics.ConfusionMatrix(task="multiclass", num_classes=len(classes))

tqdm.write(f"Accuracy: {str(val)}")
tqdm.write(f"MAE: {str(metrics.mean_absolute_error(y_pred_all_tensor, y_test_tmp))}")
tqdm.write(f"RMSE: {str(math.sqrt(metrics.mean_squared_error(y_pred_all_tensor, y_test_tmp)))}")
tqdm.write(f"F1 MICRO: {str(f1_socre_micro(y_pred_all_tensor, y_test_tmp))}")
tqdm.write(f"F1 MACRO: {str(f1_socre_macro(y_pred_all_tensor, y_test_tmp))}")
tqdm.write(f"F1 WEIGTED: {str(f1_socre_weighted(y_pred_all_tensor, y_test_tmp))}")
tqdm.write("ConfusionMatrix:")
tqdm.write(str(conf(y_pred_all_tensor, y_test_tmp)))
