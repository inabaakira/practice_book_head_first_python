#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: vsearch.py
#    Created:       <2018/02/08 20:36:09>
#    Last Modified: <2018/02/12 16:15:27>

def search4vowels(word:str) -> set:
    """Display any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
