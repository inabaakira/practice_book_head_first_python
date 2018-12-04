#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: open_process_close.py
#    Created:       <2018/12/05 00:18:06>
#    Last Modified: <2018/12/05 00:20:04>

todos = open('todos.txt', 'a')
print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)
todos.close()
