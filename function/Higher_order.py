def add(x, y, f):
    return f(x) + f(y)

a = add(-5, -12, abs)
print(a)

# map
def f(x):
	return x * x

L = list(map(f, [1, 3, 5, 7, 9]))
print(L)

st = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(st)

# reduce
from functools import reduce
def add(x, y):
	return x+y

print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
	return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6' : 6, '7': 7, '8': 8, '9': 9}[s]

number = reduce(fn, map(char2num, '13579'))
print(number)


def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))

print(L2)
print(list(map(normalize, L1)))
