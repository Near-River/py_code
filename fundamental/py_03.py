#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# if - elif - else
age = int(input('Input your age: '))
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

m = 'good' if 2 > 3 else 'bad'
print(m)

# for loop
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


# while loop: calculate the summation through 1 to 100
sum_, n = 0, 1
while n <= 100:
    sum_ += n
    n += 1
print(sum_)
