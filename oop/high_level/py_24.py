#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique


# enum class
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(type(Month))      # <class 'enum.EnumMeta'>
print(type(Month.Jan))  # <enum 'Month'>
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique     # to make sure all the constant in the class be unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
# day1.value = 10       # AttributeError: can't set attribute

print('Weekday.Tue =', Weekday.Tue)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Tue.name =', Weekday.Tue.name)
print('Weekday.Tue.value =', Weekday.Tue.value)
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday(1) ?', day1 == Weekday(1))

for member in Weekday:
    print(member, member.value)
