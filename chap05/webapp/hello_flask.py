#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: hello_flask.py
#    Created:       <2018/02/26 20:27:55>
#    Last Modified: <2018/02/26 20:35:52>

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

app.run()
