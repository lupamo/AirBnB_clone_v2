#!/usr/bin/python3
"""A script to start Flask web app with two different routes"""

from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """display a HTML page only if n is an integer"""
    val = ""
    if n % 2 == 0:
        val = "is even"
    else:
        val = "is odd"
    return render_template('6-number_odd_or_even.html', n=n, val=val)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
