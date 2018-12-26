#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: simple_webapp.py
#    Created:       <2018/12/26 20:25:41>
#    Last Modified: <2018/12/26 20:40:17>

from flask import Flask, session

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'

@app.route('/page1')
def page1() -> str:
    return 'This is page 1.'

@app.route('/page2')
def page2() -> str:
    return 'This is page 2.'

@app.route('/page3')
def page3() -> str:
    return 'This is page 3.'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'

app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
