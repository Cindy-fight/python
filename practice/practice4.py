#!/usr/bin/env python
# ！-*- coding:UTF-8 -*-

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    if callable(text):
        decorator = decorator(text)
    return decorator

@log
def f():
    print('Hello, I am call!')
f()

@log('execute')
def f():
    print('Hello, I am execute!')
f()
