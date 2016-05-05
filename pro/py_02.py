# -*- coding: utf-8 -*-
import functools
import math
import time
from functools import reduce

# 高阶函数特点

fun = abs

print(fun)
print(fun(-10))


# 自定义高阶函数
def my_add(a, b, f):
    return f(a) + f(b)


# print(my_add(-1, 2, fun))


# map()函数接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
def format_name(s):
    return s[:1].upper() + s[1:].lower()


for value in map(format_name, ['adam', 'LISA', 'barT']):
    print(value)


# reduce()函数接收的参数和 map()类似，但对list的每个元素反复调用函数f，并返回最终结果值。
# reduce()还可以接收第3个可选参数，作为计算的初始值。
def prod(x, y):
    return x * y


# print(reduce(prod, [2, 4, 5, 7, 12], 1))


# filter()函数根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
def is_not_empty(s):
    return s and len(s.strip()) > 0  # 删除None或空字符串


def is_sqr(x):
    m = int(math.sqrt(x))  # 保留1-100中具有整数平方根的数
    return m * m == x


for value in map(format_name, filter(is_not_empty, ['test', None, '', 'str', '  ', 'END', 0])):
    print(value)

a = '\t\t123\r\n'
b = '    haha'

# print(a.strip())
# print(b.strip())


# 自定义排序函数 sorted()方法
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.upper))

sum_1 = sum([1, 2, 3])
print(sum_1)


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            def g():
                return i * i

            return g

        f_ = f(i)
        fs.append(f_)
    return fs


for f in count():  # count() --> fs
    print(f())

# 匿名函数
my_abs = lambda x: -x if x < 0 else x
print(my_abs(-10))


# for v in map(lambda x: x * x, [1, 2, 3]):
#     print(v)


# 装饰器 @decorator
def f1(x):
    return x * x


# 通过高阶函数返回新函数
def new_fn(f):  # 装饰器函数
    def fn(x):
        print('call', f.__name__ + '()')
        return f(x)

    return fn


g1 = new_fn(f1)
f1 = new_fn(f1)  # 彻底隐藏f1的原始定义函数
# print(g1(3))
print(f1(5))


@new_fn
def f2(x):
    return x * x * x


# print(f2(3))

def log(f):  # 自定义日志函数
    @functools.wraps(f)
    def fn(*args, **kwargs):
        print('call', f.__name__ + '()')
        return f(*args, **kwargs)

    return fn


@log
def f3(a, b):
    return a + b


print(f3(10, 20))


# 函数调用时间的性能测试
def performance(f):
    def fn(*args, **kwargs):
        t1 = time.time()
        res = f(*args, **kwargs)
        t2 = time.time()
        print('call %s() in %f s' % (f.__name__, t2 - t1))
        return res

    return fn


@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


factorial(10000)


# 编写带参数的装饰器
def log2(prefix):
    def log_decorator(f):
        @functools.wraps(f)  # 完善装饰器，把原函数的一些属性复制到新函数中。
        def wrapper(*args, **kw):
            print('[%s] %s()' % (prefix, f.__name__))
            return f(*args, **kw)

        return wrapper

    return log_decorator


@log2('DEBUG')
def test():
    pass


test()
# print(test.__name__)

# 偏函数
int2 = functools.partial(int, base=2)
print(int2('10101'))
