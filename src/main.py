from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras import backend as K
import re
import os
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import argparse
from model import train_model

def main():

    X_train, X_test, y_train, y_test = get_images_and_wastes()
    train_model()
    %matplotlib inline
    img = X_test[30]
    plt.imshow(Image.fromarray(img.squeeze()*255))
    pred = model.predict(np.expand_dims(img, axis=0))
    print("================================================================================================================================")
    print("Probs -> Cardboard:{0:.5f} Glass:{1:.5f} Metal:{2:.5f} Paper:{3:.5f} Plastic:{4:.5f} Trash:{5:.5f}".format(pred[0,0], pred[0,1], pred[0,2],pred[0,3],pred[0,4],pred[0,5]))
    print("================================================================================================================================")


if __name__ == '__main__':
    main()