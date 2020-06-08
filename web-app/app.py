from flask import Flask, render_template, request, flash, redirect
import os
from binascii import a2b_base64
import random

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
    load_conv_model()
    return f'{count}'


# Open it with Numpy Reshape it
# Start the Model
# Feed this Input Image
# Get Result Return Request

# Starting and Loading the Modell
def load_conv_model():
    from keras.models import load_model
    model = load_model('kaggle-ip/conv_model.hdf5')
    model.summary()
