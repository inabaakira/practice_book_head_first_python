#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: url_utils.py
#    Created:       <2019/02/15 20:42:55>
#    Last Modified: <2019/02/17 15:31:58>

import requests

def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url
