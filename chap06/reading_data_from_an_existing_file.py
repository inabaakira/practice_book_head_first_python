#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: reading_data_from_an_existing_file.py
#    Created:       <2018/12/05 00:26:05>
#    Last Modified: <2018/12/05 00:27:46>

tasks = open('todos.txt')
for chore in tasks:
    print(chore)
tasks.close()
