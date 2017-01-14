#!/usr/bin/env python3

from flask import Flask
app = Flask("CitiZen")


@app.route('/')
def hello_world():
    return 'Hello, World!'
