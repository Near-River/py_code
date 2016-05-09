# -*- coding: utf-8 -*-


# 构建菲波那切模板
# class Fib(object):
#     def __init__(self, num):
#         self.num = num
#         a, b, L = 0, 1, []
#         for i in range(1, num+1):
#             a, b = b, a+b
#             L.append(a)
#         Fib.nums = L
#
#     def __str__(self):
#         return str(Fib.nums)
#
#     def __len__(self):
#         return len(Fib.nums)
#
#
# f = Fib(10)
# print(f, len(f))

class Fib(object):  # 改进版
    __count__ = 0

    def __init__(self, num):
        self.num = num
        self._a, self._b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self._a, self._b = self._b, self._a+self._b
        if self.__count__ >= self.num:
            raise StopIteration
        self.__count__ += 1
        return self._a


for item in Fib(10):
    print(item)