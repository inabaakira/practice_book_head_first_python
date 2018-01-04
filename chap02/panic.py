#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: panic.py
#    Created:       <2018/01/04 15:05:55>
#    Last Modified: <2018/01/04 16:17:34>

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.pop(0)
plist.pop(2)
plist.insert(2, plist.pop(3))
plist.insert(4, plist.pop())
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
