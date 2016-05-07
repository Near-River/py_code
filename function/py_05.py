#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


# call function
x = abs(100)
y = abs(-20)
print(x, y)
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))


# define function
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type: ' + str(type(x))[8:-2])
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

print(my_abs(-20))


# TypeError: bad operand type: str
# my_abs('123')
