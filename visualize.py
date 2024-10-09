import matplotlib.pyplot as plt
import pickle
import numpy as np
from google.colab import drive
drive.mount('/content/drive')

label = 'batch size' # feature number range(1, 21)

step = 2
intial = 0

file_paths_train = []
file_paths_val = []
file_paths_test = []
for i in range(2, 14, 2):
    file_paths_train.append(f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/train/mse{i}.pkl')
    file_paths_val.append(f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/val/mse{i}.pkl')
    file_paths_test.append(f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/test/mse{i}.pkl')

all_train_mse_data = []
all_val_mse_data = []
all_test_mse_data = []

for file_path in file_paths_train:
    with open(file_path, 'rb') as f:
        mean_mse = pickle.load(f)
        all_train_mse_data.append(mean_mse)

for file_path in file_paths_val:
    with open(file_path, 'rb') as f:
        mean_mse = pickle.load(f)
        all_val_mse_data.append(mean_mse)

for file_path in file_paths_test:
    with open(file_path, 'rb') as f:
        mean_mse = pickle.load(f)
        all_test_mse_data.append(mean_mse)

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

cmap = plt.get_cmap('rainbow')
colors = [cmap(i / len(all_train_mse_data)) for i in range(len(all_train_mse_data))]

for i, train_mse in enumerate(all_train_mse_data):
    epochs = range(1, len(train_mse) + 1)
    axs[0].plot(epochs, train_mse, label=f'Train {label} = {intial + step * (i + 1)}', color=colors[i])

axs[0].set_xlabel('Epoch')
axs[0].set_ylabel('Mean MSE')
axs[0].set_title(f'Train MSE across different {label}')
axs[0].legend(loc='upper right')

for i, val_mse in enumerate(all_val_mse_data):
    epochs = range(1, len(val_mse) + 1)
    axs[1].plot(epochs, val_mse, label=f'Val {label} = {intial + step * (i + 1)}', color=colors[i])

axs[1].set_xlabel('Epoch')
axs[1].set_ylabel('Mean MSE')
axs[1].set_title(f'Validation MSE across different {label}')
axs[1].legend(loc='upper right')

for i, test_mse in enumerate(all_test_mse_data):
    epochs = range(1, len(test_mse) + 1)
    axs[2].plot(epochs, test_mse, label=f'Test {label} = {intial + step * (i + 1)}', color=colors[i])

axs[2].set_xlabel('Epoch')
axs[2].set_ylabel('Mean MSE')
axs[2].set_title(f'Test MSE across different {label}')
axs[2].legend(loc='upper right')

plt.tight_layout()
plt.show()