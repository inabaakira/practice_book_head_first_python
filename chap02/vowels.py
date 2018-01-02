#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: vowels.py
#    Created:       <2018/01/02 23:22:44>
#    Last Modified: <2018/01/02 23:29:24>

vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
for letter in word:
    if letter in vowels:
        print(letter)
