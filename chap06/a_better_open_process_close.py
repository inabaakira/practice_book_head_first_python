#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: a_better_open_process_close.py
#    Created:       <2018/12/05 00:50:26>
#    Last Modified: <2018/12/05 00:51:47>

tasks = open('todos.txt')
for chore in tasks:
    print(chore, end='')
tasks.close()

with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')
