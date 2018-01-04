#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: panic.py
#    Created:       <2018/01/04 15:05:55>
#    Last Modified: <2018/01/04 16:32:39>

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.pop(0)
plist.pop(2)
plist.extend([plist.pop(2), plist.pop(), plist.pop()])
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
