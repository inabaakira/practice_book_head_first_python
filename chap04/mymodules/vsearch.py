#!/usr/bin/env python
# -*- mode: python; coding: utf-8 -*-
# file: vsearch.py
#    Created:       <2018/02/08 20:36:09>
#    Last Modified: <2018/02/22 20:55:08>


def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
