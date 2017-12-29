# method1
def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# method2
def normalize_2(name):
    first = name[0].upper()
    next = name.lower()[1:]
    return first + next

L3 = list(map(normalize_2, L1))
print(L3)

from functools import reduce
def prod(x, y):
    return x * y
r1 = reduce(prod, [3, 5, 7, 9])
print('3 * 5 * 7 * 9 = ',r1)


def str2float(s):
    def fn(x, y):
        return x * 10 + y
    def fx(x, y):
        return x / 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}[s]
    L = s.split('.', 1)
    return reduce(fn, map(char2num, L[0])) + reduce(fx, map(char2num, L[1][-1::-1]))/10

print(str2float(input('请输入你要转化的字符串：')))    
