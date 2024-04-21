#!/usr/bin/python3
"""A script to start Flask web app with two different routes"""

from flask import Flask
from markupsafe import escape

"""Creating a new Flask application instance"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Handles requests to the route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    """Handles request to another route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Handles request to C"""
    txt_escaped = text.replace('_', ' ')
    return 'C ' + escape(txt_escaped)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """routes to python text"""
    txt_escaped = text.replace('_', ' ')
    return 'Python ' + escape(txt_escaped)


@app.route('/number/<int:value>', strict_slashes=False)
def num(value):
    """only integer in the route value"""
    return '{} is a number'.format(value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
