#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: countfromby.py
#    Created:       <2018/12/18 20:46:15>
#    Last Modified: <2018/12/19 20:51:34>

class CountFromBy:

    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)
