#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

print(Student('Michael'))

class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1
        self.c = 1

    def __iter__(self):
        return self

    def __next__(self):
        #method1
        self.a = self.b
        self.b = self.c
        self.c = self.a + self.b
        if self.c > 1000:
            raise StopIteration()
        return self.c

        #method2
        # self.a, self.b = self.b, self.a + self.b
        # if self.a > 1000:
        #     raise StopIteration()
        # return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# for n in Fib():
#     print(n)

f = Fib()
print(f[10])

print(f[5:18])


class Fib_2(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        #method1
        self.a = self.b
        self.b = self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

# for n in Fib_2():
#     print(n)


class Fib_3(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        #method1

        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

# for n in Fib_3():
#     print(n)


class Student_1(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda : 25
        # raise AttributeError('Student object has no attribute %s' % attr)

s1 = Student_1()
print(s1.name)
print(s1.age())
print(s1.score)

class China(object):

    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return China('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

china = China()
print(china.status.user.timeline.list)

class Student_2(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s2 = Student_2('Cindy')
s2()

# print(callable(Student()))
print(callable(Student_1()))
# print(callable(Student_2()))
print(callable(max))