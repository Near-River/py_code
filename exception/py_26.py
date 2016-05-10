#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# exception 1:
try:
    print('try...')
    r = 10 / 0
    # r = 10 / 1
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
except ArithmeticError as e:
    print('except:', e)
else:
    print('no exception')
finally:
    print('finally...')
print('END')
