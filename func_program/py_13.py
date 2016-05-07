#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# return function(Closure):
def lazy_sum(*args):
    def _sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return _sum


f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())


# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def count():
    fs = []

    def f(n):
        return lambda: n ** 2

    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())
