#!/usr/bin/python3
"""A script to start Flask web app with two different routes"""

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
