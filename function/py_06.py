#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# function: variable parameter
def hello(greeting, *args):
    if len(args) == 0:
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))


hello('Hi')  # => greeting='Hi', args=()
hello('Hello', 'Michael', 'Bob', 'Adam')  # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names)  # => greeting='Hello', args=('Bart', 'Lisa')


# function: keyword arguments
def print_scores(**kwargs):
    for name, score in kwargs.items():
        print('%10s %d' % (name, score))


data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}
print_scores(Adam=99, Lisa=88, Bart=77)
print_scores(**data)


# function: Named keyword arguments
def print_info(name, *, gender, city='Beijing', age):
    print(' Name: %s' % name)
    print(' Gender: %s' % gender)
    print(' City: %s' % city)
    print(' Age: %s' % age)


print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)


# Tail recursion
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
