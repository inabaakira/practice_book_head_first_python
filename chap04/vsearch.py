#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: vsearch.py
#    Created:       <2018/02/08 20:36:09>
#    Last Modified: <2018/02/11 19:39:54>

def search4vowels(word):
    """Display any vowels found in a supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
