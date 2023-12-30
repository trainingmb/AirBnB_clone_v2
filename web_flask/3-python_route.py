#!/usr/bin/python3
"""Python is cool!"""
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


@app.route("/c/<text>")
def c_is_fun(text):
    """Display "C" followed by the value of the
       text variable (replace underscore _ symbols
       with a space )
    """
    return "C " + text.replace("_", " ")


@app.route("/python/")
@app.route("/python/<text>")
def python_is_cool(text="is_cool"):
    """Display Python, followed by the value of the
       text variable (replacing underscores with spaces)
    """
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
