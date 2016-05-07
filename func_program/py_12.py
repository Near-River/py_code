#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from operator import itemgetter


# functional programming 3: sorted()
L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))


students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def _by_score(s):
    return s[1]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
print(sorted(students, key=_by_score, reverse=True))
