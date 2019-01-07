#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: try_examples.py
#    Created:       <2019/01/07 20:12:44>
#    Last Modified: <2019/01/07 20:13:26>

with open("myfile.txt") as fh:
    file_data = fh.read()
print(file_data)
