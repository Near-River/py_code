#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# input     output
print('Hello World!')
print('1+2= ', 1+2)

name = input('Please input your name: ')
print('Your name:', name)


print('\\\t\\')
print(r'\\\t\\')
print('growth rate: %d %%' % 7)     # using %% to escape the character '%'


# String encoding
print(ord('A'))
print(chr(97))

print('ABC'.encode('ascii'))    # bytes type --> str type
print('中国'.encode('utf-8'))
print(b'ABC'.decode('ascii'))   # str type --> bytes type
print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf-8'))
