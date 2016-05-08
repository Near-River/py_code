#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types


# obtain the object info:
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))
print('getattr(obj, \'y\') =', getattr(obj, 'y'))
print('obj.y =', obj.y)

print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))

f = getattr(obj, 'power')
print(f)
print(f())
