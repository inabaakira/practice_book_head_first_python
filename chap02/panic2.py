#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: panic.py
#    Created:       <2018/01/04 15:05:55>
#    Last Modified: <2018/01/04 23:11:29>

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)
