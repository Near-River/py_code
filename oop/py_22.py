#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# customize class 1:
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name

    __repr__ = __str__


print(Student('Nate River'))


class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):  # let the object support the indexing
            a, b = 1, 1
            for i in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # let the object support the slice
            start, stop = item.start, item.stop
            if start is None:
                start = 0
            a, b, L = 1, 1, []
            count = 0
            while count < stop:
                if count >= start:
                    L.append(a)
                a, b = b, a + b
                count += 1
            return L


for i in range(10):
    print(Fib()[i])
print(Fib()[:10])
print(Fib()[1:5])
