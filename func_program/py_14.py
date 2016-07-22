#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
import datetime


# decorator
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2016-4-25')

now()


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@logger('DEBUG')
def today(d):
    print(d)

today(datetime.date(2016, 5, 7))
print(today.__name__)
