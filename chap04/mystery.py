#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: mystery.py
#    Created:       <2018/02/22 12:50:15>
#    Last Modified: <2018/02/22 12:52:33>

def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)

def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)
