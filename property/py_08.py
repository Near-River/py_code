#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:  # for x in iter([1, 2, 3, 4, 5])
    print(x)

it = iter([1, 2, 3, 4, 5])  # iter() --> next()
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
for k in d.keys():
    print('key:', k)

# iter each value:
for v in d.values():
    print('value:', v)

# iter both key and value:
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
for x, y, z in [(1, 1, 1), (2, 4, 6), (3, 6, 9)]:
    print(x, y, z)
