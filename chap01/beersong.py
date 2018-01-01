#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: beersong.py
#    Created:       <2018/01/01 11:44:23>
#    Last Modified: <2018/01/01 12:17:40>

word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
            print(new_num, word, "of beer on the wall.")
    print
