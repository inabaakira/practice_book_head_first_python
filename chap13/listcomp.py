#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: listcomp.py
#    Created:       <2019/02/14 21:32:03>
#    Last Modified: <2019/02/14 21:34:29>

import requests

urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')

for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), '->', resp.status_code, '->', resp.url)
