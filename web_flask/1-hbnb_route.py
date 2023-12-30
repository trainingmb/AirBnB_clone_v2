#!/usr/bin/python3
"""HBNB"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """At the home address displays hello hbnh"""
    return "Hello HBNB!"
@app.route("/hbnb")
def hbnb():
    """Adds the route for HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
