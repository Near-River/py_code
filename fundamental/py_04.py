#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# dict
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))


# list: union   intersection    difference
s1 = {1, 1, 2, 2, 3, 3}
s2 = {2, 3, 4}
print(s1, s2)
print(s1 & s2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))