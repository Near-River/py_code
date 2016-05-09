#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# customize class
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
