#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json


# pickling: JSON Advanced
def Dict2Student(d):
    return Student(d['id'], d['name'], d['age'])


class Student(object):
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def Student2Dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

    def __str__(self):
        return '<%s>: id: %s    name: %s    age: %s' % (self.__class__.__name__, self.id, self.name, self.age)

    __repr__ = __str__


s = Student('001', 'Nate_River', 21)
s_json = json.dumps(s, default=Student.Student2Dict)
print(s_json)
print(json.loads(s_json, object_hook=Dict2Student))

"""==========================================================================="""

s_json2 = json.dumps(s, default=lambda s: dict(id=s.id, name=s.name, age=s.age))
print(s_json2)
print(json.loads(s_json2, object_hook=lambda d: Student(d['id'], d['name'], d['age'])))
