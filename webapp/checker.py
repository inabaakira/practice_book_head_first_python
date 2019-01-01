#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: checker.py
#    Created:       <2018/12/31 21:43:09>
#    Last Modified: <2019/01/01 15:03:57>

def check_logged_in(func):
    def wrapper() -> str:
        if 'logged_in' in session:
            return func()
        return 'You are NOT logged in.'
    return wrapper
