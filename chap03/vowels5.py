#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: vowels.py
#    Created:       <2018/01/02 23:22:44>
#    Last Modified: <2018/01/19 00:51:50>

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).' )
