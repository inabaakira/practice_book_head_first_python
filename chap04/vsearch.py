#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: vsearch.py
#    Created:       <2018/02/08 20:36:09>
#    Last Modified: <2018/02/12 11:41:24>

def search4vowels(word):
    """Display any vowels found in a supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)
