#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: generator.py
#    Created:       <2019/02/14 21:37:25>
#    Last Modified: <2019/02/17 15:40:21>

from url_utils import gen_from_urls

urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')

for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)

urls_res = {url: size for size, _, url in gen_from_urls(urls)}

import pprint

pprint.pprint(urls_res)
