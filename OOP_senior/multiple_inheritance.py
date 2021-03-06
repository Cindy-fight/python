#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

class Animal(object):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

#大类
class Mammal(Animal):
    pass

class Birds(Animal):
    pass

#各种动物
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Birds, Flyable):
    pass

class Ostrich(Birds, Runnable):
    pass
