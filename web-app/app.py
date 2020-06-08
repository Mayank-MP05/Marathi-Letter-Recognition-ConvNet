from flask import Flask, render_template, request, flash, redirect
import os
from binascii import a2b_base64
import random
import cv2

from keras.models import load_model
import pickle
BE = pickle.load(open('kaggle-ip/labelBinarizerFinal.pickle', 'rb'))
model = load_model('kaggle-ip/conv_model_Final.hdf5', compile=False)

app = Flask(__name__)


@app.route('/ref')
def ref():
    return render_template('ref.html')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload', methods=['POST'])
def get_image():
    image_b64 = request.values['imageBase64']
    count = random.randint(0, 100)
    # Removing Prefix from Data URI
    data = image_b64.replace("data:image/png;base64,", '')
    binary_data = a2b_base64(data)
    # Get the Images Saved in Upload Folder
    fd = open(f'uploads/image-{count}.png', 'wb')
    fd.write(binary_data)
    fd.close()
    # ---------------------------------------
    arr = prepareImg(count)
    chrX = load_conv_model(arr)
    # ---------------------------------------
    load_conv_model()
    return f'{count} -> {chrX}'


# Open it with Numpy Reshape it
# Start the Model
# Feed this Input Image
# Get Result Return Request

# Starting and Loading the Modell
def load_conv_model(arr):
    result = model.predict(arr)
    character = BE.classes_[np.argmax(result)]
    return character

# Take the Image and return Resized Numpy Array


def prepareImg(number):
    img = cv2.imread(f'uploads/image-{number}.png')
    img = cv2.resize(img, (32, 32))
    img = img.reshape(1, 32, 32, 1)
    return img
