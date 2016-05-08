# -*- coding: utf-8 -*-


# 构建菲波那切类
class Fib(object):
    def __init__(self, num):
        self.num = num
        a, b, L = 0, 1, []
        for i in range(1, num+1):
            a, b = b, a+b
            L.append(a)
        Fib.nums = L

    def __str__(self):
        return str(Fib.nums)

    def __len__(self):
        return len(Fib.nums)


f = Fib(10)
print(f, len(f))
