#!/usr/bin/python3
""" starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a string at the root route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def string():
    """Returns a string at the root route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_text_cisfun(text):
    """Returns a string at the root route"""
    text_cisfun = text.replace('_', ' ')
    return "C {}".format(text_cisfun)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def default(text="is cool"):
    """Python is cool!"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
 