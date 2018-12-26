#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: quick_session.py
#    Created:       <2018/12/26 00:56:16>
#    Last Modified: <2018/12/26 01:02:39>

from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
