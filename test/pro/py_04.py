# -*- coding: utf-8 -*-
import os
import random

# 错误和异常处理
# try-except 的使用

try:
    1 / 0
except ZeroDivisionError as error:  # 捕获并处理异常
    print(error)

num = random.randint(0, 100)
# print(num)
# 猜数字游戏
# while True:
#     try:
#         n = int(input('Enter 1~100: '))
#     except:
#         print('Enter Error!')
#         continue
#     else:
#         if n == num:
#             print('Success!!!')
#             break
#         elif n > num:
#             print('guess Big...')
#         else:
#             print('guess Small...')

# try-except 处理多个异常
try:
    file = open('py_00.py')
    1 / 0
except IOError as error:
    print(error)
except ZeroDivisionError as error:  # 捕获并处理异常
    print(error)
else:
    print('No Error...')

# try_finally使用. finally 代码段总是会被执行，为异常处理事件提供清理机制
try:
    f1 = open('py_03.py')
    line = f1.read(2)
    print(line)
except IOError as error:
    print(error)
except ValueError as error:
    print(error)
finally:
    try:
        f1.close()
    except:
        print('file not open...')
    else:
        print('file close ...')

# with context [as var] 语句与上下文管理
# with语句用于替代try-except-finally语句，context表达式返回一个对象，使用var来保存
try:
    with open('D:/demo/123.txt') as file:
        context = file.read()
        print(context)
        file.seek(-10, os.SEEK_SET)
except:
    print('error...')
print(file.closed)  # 判断文件是否关闭


# 自定义上下文管理器
class MyContext(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('enter...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit...')
        print('Error:', exc_type, 'Info:', exc_val)


def get_context():
    return MyContext('my_context')


try:
    with get_context() as context:
        # print(context)
        # 1/0
        print(MyContext('my_context').name)
except:
    pass


# raise 和 assert语句
# raise IOError('IOError')
# assert 2 == 3, 'AssertError'


# 自定义异常
class MyException(Exception):
    def __init__(self, info):
        print(id(self))
        self.info = info

    def __str__(self):
        return 'MyException:%s' % (self.info)


try:
    raise MyException('My Exception')
except MyException as error:
    print(error, id(error))
