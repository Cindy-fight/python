#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member)

print(Month.May)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
day2 = Weekday['Tue']
print(day2)
day3 = Weekday(3)
print(day3)
day4_val = Weekday.Thu.value
print(day4_val)

for name, member in Weekday.__members__.items():
    print(name, '=>', member)