#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: tmpl_decorator.py
#    Created:       <2019/01/03 15:07:11>
#    Last Modified: <2019/01/03 15:30:31>

from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Code to execute BEFORE calling the decorated function.

        # 2. Call the decorated function as required, returning its
        #    results if needed.
        return func(*args, **kwargs)

        # 3. Code to execute INSTEAD of calling the decorated function.
    return wrapper
