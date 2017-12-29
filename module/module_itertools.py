import itertools

# count()会创建一个无限的迭代器
natural = itertools.count(1)
# for n in natural:
#     print(n)  # 进入死循环

# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)   # 进入死循环

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('YRC', 8)
for r in ns:
    print(r)

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
nl = itertools.takewhile(lambda x : x<= 10, natural)
print(list(nl))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

print('*' * 30)

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):  # or c.lower()
    print(key, list(group))

