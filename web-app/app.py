from flask import Flask, render_template, request, flash, redirect
import os
import numpy as np
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

    fd = open(f'uploads/image-{count}.png', 'wb')
    fd.write(binary_data)
    fd.close()
    count += 1
    return f'Image {count} - Saved in DB'
