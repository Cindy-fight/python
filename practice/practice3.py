#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

L = []

for x in range(1, 11):
    L.append(x * x)

print(L)


c1 = [x * x for x in range(1, 11)]
print(c1)

c2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(c2)

c3 = [m + n for m in 'ABC' for n in 'XYZ']
print(c3)

import os
c4 = [d for d in os.listdir('.')]
print(c4)

# method1
d = {'x':'A', 'y':'B', 'z':'C'}
for k, v in d.items():
    print(k, '=', v)

# method2
c5 = [k + '=' + v for k, v in d.items()]
print(c5)

List = ['Hello', 'World', 'IBM', 'Apple']
c6 = [s.lower() for s in List]
print(c6)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(8))

# def fib_2(max):
#     n = 0
#     a = 0
#     b = 1
#     while n < max:
#         yield b
#         a, b = b , a + b
#     return 'done'
#
# print(fib_2(8))

# g = fib_2(6)
# while True:
#    try:
#        x = next(g)
#        print('g:', x)
#    except StopIteration as e:
#        print('Generator return value:', e.value)
#        break

#杨辉三角
def triangles(max):
    L = [1]
    n = 0
    while n <= max:
        yield L
        L.append(0)
        #print(L)
        L = [L[i-1] + L[i] for  i in range(len(L))]
        n = n + 1
for i in triangles(int(input('输入行数：'))):
    print(i)


from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for  x in range(10)), Iterable))
print(isinstance(100, Iterable))
print('\n')

from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print('\n')

print(isinstance(iter([]), Iterator))
print(isinstance(iter('123'), Iterator))
