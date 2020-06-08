from flask import Flask, render_template
app = Flask(__name__)


@app.route('/ref')
def ref():
    return render_template('ref.html')


@app.route('/')
def home():
    return render_template('home.html')
