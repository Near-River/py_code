# -*- coding: utf-8 -*-


# 打印杨辉三角
def triangles(n):
    i, L = 1, []
    while i <= n:
        if i == 1:
            L = [1]
        elif i == 2:
            L = [1, 1]
        else:
            temp = [1]
            for j in range(1, i - 1):
                temp.append(L[j - 1] + L[j])
            temp.append(1)
            L = temp
        yield L
        i += 1


t = triangles(10)
print(t)
for item in t:
    print(item)
