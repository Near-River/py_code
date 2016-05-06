# -*- coding: utf-8 -*-


# 对 list 进行切片处理
list = ['Adam', 'Lisa', 'Bart', 'Paul', 'Near']
list2 = []
for i in range(3):
    list2.append(list[i])
# print(list2)
# print(list[:3])
# print(list[1:3])
# 第三个参数表示每N个取一个
# print(list[::2])

# 对 str 进行切片处理
str2 = 'AbCdEfGh'
# print(str2[::2])
# print(str2.upper())
# print(str2.lower())


# 索引迭代 enumerate()：将迭代的每一个元素变成一个 (index, element) 这样的tuple
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print(index, '-', name)
# 迭代dict的value. values()方法：把dict转换成一个包含所有value的list
# items()方法：把dict对象转换成包含tuple的list
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
for v in d.values():
    print(v)
for k, v in d.items():
    print('%s -> %d' % (k, v))

# 列表生成式
list3 = [x * x for x in range(1, 11)]
list4 = [x * x for x in range(1, 11, 2)]
list5 = [x * x for x in range(1, 11) if x % 2 == 0]


# print(list3)
# print(list4)
# print(list5)


def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]


print(toUppers(['Hello', 'world', 101, None]))

print(str.join(" ", ['a', 'b', 'c']))

m = 'good' if 2 > 3 else 'bad'
print(m)

print(10 / 3, 10 // 3)

print('ssssssssssssssssssss'\
      'ssssssssssssssssssss')