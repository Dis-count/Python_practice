import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision = 3, suppress = True)
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import scale, StandardScaler

import keras
from keras.datasets import mnist

import tensorflow as tf
from tensorflow import keras

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train.shape

X_test.shape

pip show tensorflow

pip show keras

X_train = X_train.reshape(60000,784)
X_test = X_test.reshape(10000,784)
X_train =X_train.astype('float32')
X_test =X_train.astype('float32')
X_train /= 255
X_test /= 255

num_classes =10
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test  = keras.utils.to_categorical(y_test, num_classes)

from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential([Dense(32, input_shape = (784, )), Activation('relu'), Dense(10), Activation('softmax'),])

model = Sequential()
model.add(Dense(32, input_dim = 784))

model.compile('adam', 'categorical_crossentropy', metrics =['accuracy'])

model.summary()

784 * 32 + 1*32
32 * 10 + 1*10

model.fit(X_train, y_train, batch_size = 128, epochs =10, verbose =1)

model.fit(X_train, y_train, batch_size = 128, epochs =10, verbose =1, validation_split =0.1)

model.evaluate(X_test, y_test, verbose = 0)


model = Sequential([Dense(32, input_shape = (784, )), Activation('relu'), Dense(10), Activation('softmax'),])

model.compile('adam', 'categorical_crossentropy', metrics =['accuracy'])
history_callback = model.
