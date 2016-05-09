#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# customize class 2:
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    def __call__(self):     # let object be callable
        print('My name is %s.' % self.name)


s = Student()
print(s.name, s.score, s.age())
# AttributeError: 'Student' object has no attribute 'grade'
# print(s.grade)

s()
print(callable(s))
