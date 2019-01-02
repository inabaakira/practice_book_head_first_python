#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: checker.py
#    Created:       <2018/12/31 21:43:09>
#    Last Modified: <2019/01/02 15:29:06>

from flask import session

from functools import wraps

def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper
