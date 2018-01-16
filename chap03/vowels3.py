#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: vowels.py
#    Created:       <2018/01/02 23:22:44>
#    Last Modified: <2018/01/17 00:15:45>

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
