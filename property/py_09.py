#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list comprehensions
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple', 21]
print([s.lower() for s in L if isinstance(s, str)])

# generator:
g = (x * x for x in range(10))  # creation method 1
print(g)
for item in g:
    print(item)


# generator function
def fib(n):  # creation method 2
    i, a, b = 0, 0, 1
    while i < n:
        yield b
        a, b = b, a + b
        i += 1
    return 'Done'


f = fib(3)
print(f)
for item in f:
    print(item)

# call generator manually:
g = fib(5)
while True:
    try:
        print('g:', next(g))
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
