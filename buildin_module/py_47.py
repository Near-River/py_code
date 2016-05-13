#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter


# build-in: collections
# namedtuple:
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)


# deque: Bidirectional list
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


# defaultdict:
dd = defaultdict(lambda: 'Not Exist.')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])


# OrderDict: According to the order of insertion sort
od = OrderedDict()
od['z'] = 1
od['y'] = 1
od['x'] = 1
print(od.keys())


# Counter:
c = Counter()
for ch in 'programming':
    c[ch] += 1
print(c)
