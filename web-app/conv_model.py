import pickle
import cv2
from keras.models import load_model
import tensorflow as tf
import numpy as np
from labels import labels

import warnings
warnings.simplefilter("ignore")

model = load_model('kaggle-ip/conv_model_Final.hdf5', compile=False)
graph = tf.get_default_graph()

"""
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
firstConv (Conv2D)           (None, 29, 29, 32)        544
_________________________________________________________________
FirstPool (MaxPooling2D)     (None, 14, 14, 32)        0
_________________________________________________________________
SecondConv (Conv2D)          (None, 12, 12, 64)        18496
_________________________________________________________________
SecondPool (MaxPooling2D)    (None, 6, 6, 64)          0
_________________________________________________________________
dropout_2 (Dropout)          (None, 6, 6, 64)          0
_________________________________________________________________
flatten_2 (Flatten)          (None, 2304)              0
_________________________________________________________________
dense_1 (Dense)              (None, 128)               295040
_________________________________________________________________
dense_2 (Dense)              (None, 50)                6450
_________________________________________________________________
modeloutput (Dense)          (None, 46)                2346
=================================================================
Total params: 322,876
Trainable params: 322,876
Non-trainable params: 0
_________________________________________________________________


"""


def prepareImg(number):
    img = cv2.imread(f'uploads/image-{number}.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (32, 32))
    img = img.reshape(1, 32, 32, 1)
    print(img.shape)
    return img


model.summary()
#BE = pickle.load(open('kaggle-ip/labelBinarizerFinal.pickle', 'rb'))

with graph.as_default():
    pred = model.predict(prepareImg(39))
    index = np.argmax(pred)
    print(labels[index])
    #chr = BE.classes_[index]
    # print(chr)

"""
Running Script :
python -W ignore conv_model.py

"""
