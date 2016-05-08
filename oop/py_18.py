#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# inheritance    polymorphism
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class RunObj(object):
    def run(self):
        print('run...')


def run(animal):
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))

run(d)
run(c)
run(RunObj())   # Ducks type
