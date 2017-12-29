d = {'a':1, 'b':2, 'c':3}

for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

for ch in 'ABC':
    print(ch)


from collections import Iterable
i1 = isinstance('abc', Iterable)       # str
i2 = isinstance([1, 2, 3], Iterable)   # list
i3 = isinstance((1, 2, 3), Iterable)   # tuple
i4 = isinstance(123, Iterable)         # int
print('str是否是可迭代对象：', i1)
print('list是否是可迭代对象：', i2)
print('tuple是否是可迭代对象：', i3)
print('int是否是可迭代对象：', i4)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x,y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


