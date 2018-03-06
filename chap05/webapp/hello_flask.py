#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: hello_flask.py
#    Created:       <2018/02/26 20:27:55>
#    Last Modified: <2018/03/06 23:13:48>

from flask import Flask
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))

app.run()
