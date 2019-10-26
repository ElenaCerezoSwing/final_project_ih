from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import sklearn
from sklearn.model_selection import train_test_split
from get_x_y import get_images_and_wastes
from train_tets_split import get_train_test_split
import numpy as np
import pandas as pd


def train_model():

    # get x and y (images and wastes)
    images, wastes = get_images_and_wastes()

    x = np.array(images)
    y = np.array(wastes)

    # train-test split
    X_train, X_test, y_train, y_test = get_train_test_split(x, y)

    # types cast, from uint-8 to unit32
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')

    # normalize
    X_train /= 255
    X_test /= 255

    # project constant
    num_classes = 6

    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),activation='relu', input_shape=(x.shape[1:])))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])

    batch_size = 20
    epochs = 10
    model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(X_test,  y_test))

    print(model.summary())

    score = model.evaluate(X_train, y_train, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    score = model.evaluate(X_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    model.save('good_model.h5')



