import numpy as np
import math
from sklearn.model_selection import train_test_split
from tensorflow.keras import backend as K
import gc
import os
from google.colab import drive
drive.mount('/content/drive')

import pickle

# experiment
iterations = 100

# data
seed = 42

# training
batch_size = 10
epochs = 100
use_bias = True
validate_ratio = 0.2
test_ratio = 0.2

neuron_number_range = range(1, 21)
label = 'neuron number at intermediate layer'

for s in neuron_number_range:
    super_train_file = f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/train/mse{s}.pkl'
    super_val_file = f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/val/mse{s}.pkl'
    super_test_file = f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/test/mse{s}.pkl'
    if os.path.exists(super_train_file) and os.path.exists(super_val_file) and os.path.exists(super_test_file):
        print(f"{s} (skipped)")
        continue
    else:
        print(f"{s} (running)")
    for i in range(iterations):
        train_file = f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/sub/train/mse{s}_{i}.pkl'
        val_file = f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/sub/val/mse{s}_{i}.pkl'
        test_file = f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/sub/test/mse{s}_{i}.pkl'
        if os.path.exists(train_file) and os.path.exists(val_file) and os.path.exists(test_file):
            print(f"{i + 1} / {iterations} (skipped)")
            continue
        X_train, y_train = generate_data()
        X_temp, X_test, y_temp, y_test = train_test_split(X_train, y_train, test_size=test_ratio, random_state=seed)
        X_train_split, X_val, y_train_split, y_val = train_test_split(X_temp, y_temp, test_size=(validate_ratio / (1 - test_ratio)), random_state=seed)
        train_mse = []
        val_mse = []
        test_mse = []
        model = create_model(neurons = 1)
        for epoch in range(epochs):
            history = model.fit(X_train_split, y_train_split, validation_data=(X_val, y_val), epochs=1, batch_size=batch_size, verbose=0)
            train_mse.append(history.history['mean_squared_error'][0])
            val_mse.append(history.history['val_mean_squared_error'][0])
            test = model.evaluate(X_test, y_test, verbose=0)
            test_mse.append(test[1])
        with open(train_file, 'wb') as f:
            pickle.dump(train_mse, f)
        with open(val_file, 'wb') as f:
            pickle.dump(val_mse, f)
        with open(test_file, 'wb') as f:
            pickle.dump(test_mse, f)
        print(f"{i + 1} / {iterations} (saved)")
        K.clear_session()
        gc.collect()
    all_train_mse = []
    all_val_mse = []
    all_test_mse = []
    for i in range(iterations):
        with open(f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/sub/train/mse{s}_{i}.pkl', 'rb') as f:
            train_mse = pickle.load(f)
            all_train_mse.append(train_mse)
        with open(f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/sub/val/mse{s}_{i}.pkl', 'rb') as f:
            val_mse = pickle.load(f)
            all_val_mse.append(val_mse)
        with open(f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/sub/test/mse{s}_{i}.pkl', 'rb') as f:
            test_mse = pickle.load(f)
            all_test_mse.append(test_mse)
    all_train_mse = np.array(all_train_mse)
    mean_train_mse = np.mean(all_train_mse, axis=0)
    all_val_mse = np.array(all_val_mse)
    mean_val_mse = np.mean(all_val_mse, axis=0)
    all_test_mse = np.array(all_test_mse)
    mean_test_mse = np.mean(all_test_mse, axis=0)
    with open(super_train_file, 'wb') as f:
        pickle.dump(mean_train_mse, f)
    with open(super_val_file, 'wb') as f:
        pickle.dump(mean_val_mse, f)
    with open(super_test_file, 'wb') as f:
        pickle.dump(mean_test_mse, f)
