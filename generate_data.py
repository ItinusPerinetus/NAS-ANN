import numpy as np
import math

def generate_data(seed = 42, input_number = 10, output_number = 10, feature_number = 10, size_per_feature = 20):
    np.random.seed(seed)
    X_classes = []
    y_classes = []
    combinations = []
    non_random_input = math.floor(np.random.uniform(0, feature_number))
    while (len(combinations) <= feature_number):
        combination = []
        for input in range(input_number):
            combination.append(math.floor(np.random.uniform(0, 11)))
        if (len(combination) != non_random_input):
            add = True
        else:
            add = False
            for c in combination:
                if (c != 11):
                    add = True
                    break
        if (not add):
            continue
        for cs in combinations:
            if combination == cs:
                add = False
                break
        if (not add):
            continue
        combinations.append(combination)
    for feature in range(feature_number):
        X_ranges = []
        for input in range(input_number):
            combination = combinations[feature][input]
            if (combination == 0):
                ranges = np.random.uniform(0, 0.25, size_per_feature)
            elif (combination == 1):
                ranges = np.random.uniform(0.25, 0.5, size_per_feature)
            elif (combination == 2):
                ranges = np.random.uniform(0.5, 0.75, size_per_feature)
            elif (combination == 3):
                ranges = np.random.uniform(0.75, 1, size_per_feature)
            elif (combination == 4):
                ranges = np.random.uniform(0, 0.5, size_per_feature)
            elif (combination == 5):
                ranges = np.random.uniform(0.25, 0.75, size_per_feature)
            elif (combination == 6):
                ranges = np.random.uniform(0.5, 1, size_per_feature)
            elif (combination == 7):
                subrange_1 = np.random.uniform(0, 0.25, size_per_feature // 2)
                subrange_2 = np.random.uniform(0.5, 0.75, size_per_feature // 2)
                ranges = np.concatenate((subrange_1, subrange_2))
            elif (combination == 8):
                subrange_1 = np.random.uniform(0, 0.25, size_per_feature // 2)
                subrange_2 = np.random.uniform(0.75, 1, size_per_feature // 2)
                ranges = np.concatenate((subrange_1, subrange_2))
            elif (combination == 9):
                subrange_1 = np.random.uniform(0.25, 0.5, size_per_feature // 2)
                subrange_2 = np.random.uniform(0.75, 1, size_per_feature // 2)
                ranges = np.concatenate((subrange_1, subrange_2))
            else:
                ranges = np.random.uniform(0, 1, size_per_feature)
            X_ranges.append(ranges)
        X_class = np.vstack(X_ranges)
        X_classes.append(X_class)

        y_ranges = []
        for _ in range(output_number):
            steps = 10
            ranges = np.linspace(0, 1, steps)
            random_value = np.random.choice(ranges)
            ranges = np.full(size_per_feature, random_value)
            y_ranges.append(ranges)
        y_class = np.vstack(y_ranges)
        y_classes.append(y_class)

    X_train = np.concatenate(X_classes, axis=1)
    X_train = X_train.reshape(feature_number * size_per_feature, input_number)
    y_train = np.concatenate(y_classes, axis=1)
    y_train = y_train.reshape(feature_number * size_per_feature, output_number)
    return X_train, y_train
