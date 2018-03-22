#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType

# 给实例绑定一个属性
s.set_age = MethodType(set_age, s)
s.set_age = 23
print(s.set_age)

s2 = Student()
# s2.set_age(18)
# print(s2.set_age)


# 给类绑定一个属性
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score = 100
print(s.set_score)

s2.set_score = 98
print(s2.set_score)

# 限制实例的属性

class Teacher(object):
    __slots__ = ('name', 'age')

t = Teacher()
t.name = 'Lucy'
t.age = 18
print(t.name)
print(t.age)
# t.sex = 'F'
# print(t.sex)

class YoungTeacher(Teacher):
    pass

yt = YoungTeacher()
yt.sex = 'F'
print(yt.sex)



