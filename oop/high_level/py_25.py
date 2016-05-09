#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# type(): dynamically created class object
def fn(self, name):
    print('hello, %s!' % name)

Hello = type('Hello', (object,), dict(sayHello=fn))

print(type(Hello))
h = Hello()
print(type(h))
h.sayHello('tom')


# metaclass：
class ListMetaclass(type):  # metaclass is a class template, so it must be derived from type
    def __new__(cls, name, bases, attrs):
        """
        :param cls:     the current class object preparing to be created
        :param name:    the class name
        :param bases:   base classes
        :param attrs:   collections of method
        """
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):    # specify the custom metaclass
    pass

L = MyList()
L.add(1)
L.add('END')
print(L)