import copy

"""

深拷贝 和 浅拷贝

深拷贝 是对于一个对象 所有层次的拷贝（递归）

浅拷贝 是对于一个对象的顶层拷贝（即：拷贝了应用，并没有拷贝内容）


"""

# 浅拷贝部分

a = [11, 22]
b = a
print(id(a))
print(id(b))
# a b 的id相同


c = {'name':'cindy'}
d = c
print(id(c))
print(id(d))
# c d 的 id 相同

c['age'] = 18
print(c)
print(d)
# c d 的打印内容一样
print()


e = [11, 22]
f = [33, 44]
g = [e, f]
print(id(e))
print(id(f))
print(id(g))
print('='*20)


h = copy.copy(g)   # h g id不一致
print(id(h))
print(h)
print(id(h[0]))    # 和 e id一致
print(h[0])
print(id(h[1]))    # 和 f id一致
print(h[1])

e.append('888')
print(g)
print(h)
print("\n\n")



# 深拷贝部分

k1 = [66, 88]
k2 = copy.deepcopy(k1)
print(k1)
print(k2)
print(id(k1))
print(id(k2))
# k1 k2 指向不一致  内容一致

k1.append(999)
print(k1)
print(k2)
# k1 新增参数， k2 无变化
print()



m1 = [11, 22]
m2 = [33, 44]
m3 = [m1, m2]
m4 = copy.deepcopy(m3)

print(id(m1))
print(id(m2))
print(id(m3))
print(id(m4))

print(id(m3[0]))   # 指向与 m1 一致
print(id(m3[1]))   # 指向与 m2 一致

print(id(m4[0]))
print(id(m4[1]))
print("\n\n")


# 拷贝的其他方式

# 分片表达式可以赋值一个序列

n1 = [11, 22]
n2 = [33, 44]
n3 = [n1, n2]
n4 = n3[:]     # n4 = n3[:]  等价于  n4 = copy.copy(n3)   属于浅拷贝

print(id(n1))
print(id(n2))

print(id(n3))
print(id(n4))

print(id(n3[0]))
print(id(n3[1]))

print(id(n4[0]))
print(id(n4[1]))

# n3 n4 指向不同   n1 n3[0] n4[0] 指向相同    n2 n3[1] n4[1] 指向相同


n1.append(666)
print(n3)
print(n4)
# n3 n4 内容随 n1 的变化而变化


# 字典的 copy 方法可以拷贝一个字典

p1 = {'name':'baoDan', 'age':22, 'children_ages':[10, 8]}
co = p1.copy()

p1['children_ages'].append(6)

print(p1)
print(co)
print("\n\n")


"""

浅拷贝对 不可变类型  和  可变类型 的 copy 不同

copy.copy()   对于可变类型  会进行浅拷贝
copy.copy()   对于不可变类型  不会拷贝  仅仅是指向

"""

test_a = [11, 22, 33]
test_b = copy.copy(test_a)

print(id(test_a))
print(id(test_b))

test_a.append(44)

print(test_a)
print(test_b)

#  test_a test_b 的指向不同 ， test_b 不会随 test_a 的变化而变化
# 注意  b = a   和  b = copy.copy(a)  不等价


test_c = [55, 66]

test_d = (test_a, test_c)
print(test_d)
print(id(test_d))

test_e = copy.copy(test_d)
print(test_e)
print(id(test_e))
# test_d  test_e  指向相同 内容相同

test_c.append(888)
print(test_d)
print(test_e)

# test_c 新增值后， test_d  test_e  随之增加




