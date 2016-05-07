# -*- coding: utf-8 -*-
import functools
import time
from functools import reduce


# 函数调用时间的性能测试


def performance(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = f(*args, **kwargs)
        t2 = time.time()
        print('call %s() in %f s' % (f.__name__, t2 - t1))
        return res

    return wrapper


@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


factorial(10000)
