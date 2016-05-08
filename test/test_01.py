# -*- coding: utf-8 -*-
import math


# 解二元一次方程
def quadratic_equation(a, b, c):
    if b * b - 4 * a * c >= 0:
        d = math.sqrt(b * b - 4 * a * c)
        return (-1 * b + d) / (2 * a), (-1 * b - d) / (2 * a)

# print(quadratic_equation(2, 3, 0))


# 函数的递归调用（汉诺塔问题）
def move(n, a, b, c):
    if n == 1:
        print(a + "-->" + c)
        return
    move(n - 1, a, c, b)
    print(a + "-->" + c)
    move(n - 1, b, a, c)

# move(4, 'A', 'B', 'C')
