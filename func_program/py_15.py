#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools


# partial function
def int2(x, base=2):
    return int(x, base)


print(int2('1001'))
print(int2('10101'))


int2 = functools.partial(int, base=2)
print(int2('1001'))
print(int2('10101'))
