import numpy as np
import pathlib
import os
data_dir = pathlib.Path("/content/Valid") # turn our training path into a Python path
class_Names = np.array(sorted([item.name for item in data_dir.glob('*')])) # created a list of class_names from the subdirectories

import glob
from PIL import Image
import random

class_Names = []
class_train = []
class_test = []
class_val = []
sum = 0
for i in class_Names[::]:
    source_folder = '/content/drive/MyDrive/all data /' + i + "/"
    test_data = "/content/drive/MyDrive/Test data/" + i
    train_data = "/content/drive/MyDrive/Train data/" + i
    valid_data = "/content/drive/MyDrive/Valid data/" + i
    directory = os.listdir(source_folder)
    orginal = []
    test = []
    train = []
    valid = []
    print("class Name", i)
    for item in directory:
        img = Image.open(source_folder + item)
        print(len(orginal))
        orginal.append(img)
    train_score = 50 * len(orginal) // 100

    for i1 in range(train_score):
        int1 = random.randint(0, len(orginal) - 1)
        if not os.path.exists(train_data):
            os.makedirs(train_data)

        int2 = orginal[int1]
        train.append(int2)
        int2.save(train_data + "/" + i + str(i1) + ".jpg")
        orginal.remove(int2)
    test_score = 60 * len(orginal) // 100

    for i2 in range(test_score):
        int1 = random.randint(0, len(orginal) - 1)
        if not os.path.exists(test_data):
            os.makedirs(test_data)
        int2 = orginal[int1]
        test.append(int2)
        int2.save(test_data + "/" + i + str(i2) + ".jpg")
        orginal.remove(int2)

    for i3 in range(len(orginal)):
        if not os.path.exists(valid_data):
            os.makedirs(valid_data)
        valid.append(orginal[i3])
        orginal[i3].save(valid_data + "/" + i + str(i3) + ".jpg")

    print(i, len(test), len(train), len(valid))
    class_Names.append(i)
    class_train.append(len(train))
    class_test.append(len(test))
    class_val.append(len(valid))