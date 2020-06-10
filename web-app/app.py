from flask import Flask, render_template, request, flash, redirect, jsonify, send_file
import os
from binascii import a2b_base64
import random
import numpy as np
from conv_model import GetPredict

#BE = pickle.load(open('kaggle-ip/labelBinarizerFinal.pickle', 'rb'))

app = Flask(__name__)

# model = load_model('kaggle-ip/conv_model_Final.hdf5', compile=False)
# graph1 = tf.get_default_graph()
# K.clear_session()

# Open it with Numpy Reshape it
# Start the Model
# Feed this Input Image
# Get Result Return Request


@app.route('/ref')
def ref():
    return render_template('ref.html')


@app.route('/upload', methods=['POST'])
def uploadAndPredict():
    image_b64 = request.values['imageBase64']
    count = random.randint(0, 10000)
    # Removing Prefix from Data URI
    data = image_b64.replace("data:image/png;base64,", '')
    binary_data = a2b_base64(data)
    # Get the Images Saved in Upload Folder
    fd = open(f'uploads/image-{count}.png', 'wb')
    fd.write(binary_data)
    fd.close()
    # Getting Prediction from Conv-model
    chrX = GetPredict(count)

    # Sending the JSON response of the Object
    res = {
        "imageID": count,
        "prediction": chrX
    }
    return jsonify(res)

# Function to send image according to Id


@app.route('/image/<imageID>')
def getImage(imageID):
    filename = f'uploads/image-{imageID}.png'
    return send_file(filename, mimetype='image/png')


@app.route('/')
def home():
    return render_template('home.html')
