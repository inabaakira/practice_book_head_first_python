#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: hello_flask.py
#    Created:       <2018/02/26 20:27:55>
#    Last Modified: <2018/04/09 13:08:11>

from flask import Flask, render_template
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

app.run(debug=True)
