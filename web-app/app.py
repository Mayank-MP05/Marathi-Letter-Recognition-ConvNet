from flask import Flask, render_template, request, flash, redirect
import os
from binascii import a2b_base64
import random
import cv2
from keras.models import load_model
import pickle
from sklearn.preprocessing import LabelBinarizer
import numpy as np
import tensorflow as tf
from keras import backend as K
from conv_model import GetPredict

#BE = pickle.load(open('kaggle-ip/labelBinarizerFinal.pickle', 'rb'))

app = Flask(__name__)

# model = load_model('kaggle-ip/conv_model_Final.hdf5', compile=False)
# graph1 = tf.get_default_graph()
# K.clear_session()


@app.route('/ref')
def ref():
    return render_template('ref.html')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload', methods=['POST'])
def get_image():
    image_b64 = request.values['imageBase64']
    count = random.randint(0, 10000)
    # Removing Prefix from Data URI
    data = image_b64.replace("data:image/png;base64,", '')
    binary_data = a2b_base64(data)
    # Get the Images Saved in Upload Folder
    fd = open(f'uploads/image-{count}.png', 'wb')
    fd.write(binary_data)
    fd.close()
    # ---------------------------------------
    # arr = prepareImg(count)
    # chrX = load_conv_model(arr)
    # ---------------------------------------
    chrX = GetPredict(count)
    return f'{count} -> {chrX}'


# Open it with Numpy Reshape it
# Start the Model
# Feed this Input Image
# Get Result Return Request
