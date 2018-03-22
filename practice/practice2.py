#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

b1 = hex(255)
b2 = hex(1000)
print("255转换为十六进制表示的字符串为：'",b1, "'")
print("1000转换为十六进制表示的字符串为：'", b2, "'")


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
number = int(input('请输入一个整数：'))
b3 = my_abs(number)
print(number , '的绝对值是' , b3)


def nop():
    pass

def power(x):
    return x * x
print(power(15))

def power_n(x, n = 2):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
print(power_n(5, 2))
print(power_n(5, 3))
print(power_n(2, 10))


def enroll(name = 'Cindy', gender = 'F', age = 7, city = 'Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll()
enroll('Sarah', 'F')
enroll('Adam', 'M')
enroll('Jack', city = 'Lanzhou')
enroll('Michael', 'M', 8, 'Shanghai')


def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())
print(add_end())

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

print(calc(1, 2, 3))
print(calc(1, 3, 5, 7))

nums = [1,2,3,4,5,6,7,8,9,10]
print(calc(*nums))

print(calc(1,2,3,4,5,6,7,8,9,10))
    
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city = 'Beijing')
person('Adam', 45, gender = 'F', job = 'Engineer')
extra = {'city': 'Shanghai', 'job':'Programmer'}
person('Cindy', 23, **extra)

# def worker(name, age, *, city, job):
#     print(name, age, city, job)
# worker('Lisa', 23, city = 'Lanzhou', job = 'Teacher')

def f1(a, b, c = 0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=',args, 'kw=', kw)

# def f2(a, b, c = 0, *, d, **kw):
#     print('a=', a, 'b=', b, 'c=', c, 'd=',d, 'kw=', kw)

f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'ABC')
f1(1, 2, 3, 'a', 'ABC', x=99)
# f2(6, 6, 8, d=8)
# f2(6, 6, 8, d=8, ext = None)

args = (1, 2, 3, 4)
kw = {'d':99, 'x':'Hello,World'}
f1(*args, **kw)

# arg = (1, 2, 3)
# f2(*arg, **kw)

def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)

print(fact(5))
print(fact(10))
#print(fact(100))


# 尾递归优化
def fact_1(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact_1(8))


def move(n, a, b, c):
    if  n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(int(input('请输入层数：')), 'A', 'B', 'C')













