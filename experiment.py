import numpy as np
import math
from sklearn.model_selection import train_test_split
from tensorflow.keras import backend as K
import gc
from google.colab import drive
drive.mount('/content/drive')

import pickle

seed = 42

# experiment
iterations = 100

# data
seed = 42
feature_number = 10
size_per_feature = 20

# architecture
input_number = 10
output_number = 10
learning_rate = 0.001
kernel_initializer = 'glorot_uniform'
bias_initializer = 'zeros'

# training
batch_size = 10
epochs = 100
use_bias = True
validate_ratio = 0.2
test_ratio = 0.2

input_number_range = range(1, 21) # 1 -> 20

label = 'input number'

for s in input_number_range:
    print(s)
    all_train_mse = []
    all_val_mse = []
    all_test_mse = []
    for i in range(iterations):
        X_train, y_train = generate_data(s, output_number, feature_number, size_per_feature)
        X_temp, X_test, y_temp, y_test = train_test_split(X_train, y_train, test_size=test_ratio, random_state=seed)
        X_train_split, X_val, y_train_split, y_val = train_test_split(X_temp, y_temp, test_size=(validate_ratio / (1 - test_ratio)), random_state=seed)
        train_mse = []
        val_mse = []
        test_mse = []
        model = create_model(s, output_number, learning_rate, kernel_initializer, bias_initializer)
        for epoch in range(epochs):
            history = model.fit(X_train_split, y_train_split, validation_data=(X_val, y_val), epochs=1, batch_size=batch_size, verbose=0)
            if (i == 0 and epoch == 0):
                model.summary()
            train_mse.append(history.history['mean_squared_error'][0])
            val_mse.append(history.history['val_mean_squared_error'][0])
            test = model.evaluate(X_test, y_test, verbose=0)
            test_mse.append(test[1])
        all_train_mse.append(train_mse)
        all_val_mse.append(val_mse)
        all_test_mse.append(test_mse)
        print(f"{i + 1} / {iterations}")
        K.clear_session()
        gc.collect()
    all_train_mse = np.array(all_train_mse)
    mean_train_mse = np.mean(all_train_mse, axis=0)
    all_val_mse = np.array(all_val_mse)
    mean_val_mse = np.mean(all_val_mse, axis=0)
    all_test_mse = np.array(all_test_mse)
    mean_test_mse = np.mean(all_test_mse, axis=0)
    with open(f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/train/mse{s}.pkl', 'wb') as f:
        pickle.dump(mean_train_mse, f)
    with open(f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/val/mse{s}.pkl', 'wb') as f:
        pickle.dump(mean_val_mse, f)
    with open(f'/content/drive/MyDrive/Colab_Datasets/XAI/{label}/test/mse{s}.pkl', 'wb') as f:
        pickle.dump(mean_test_mse, f)
