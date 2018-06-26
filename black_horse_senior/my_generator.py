# list
L = [i*2 for i in range(5)]
print(L)


# generator
G = (i*2 for i in range(5))
print(G)

# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))

for x in G:
    print(x)


# 只要在def中有yield关键字的 就称为 生成器
# so fib() 是一个生成器，而非一个函数
def fib(n):
    num1 = 0
    num2 = 1
    current = 0
    while current < n:
        num = num1
        num1, num2 = num2, num1 + num2
        # num1 = num2
        # num2 = num1 + num2
        current += 1
        yield num
    return 'done'


F = fib(10)
print(F)

for i in F:
    print(i)


f = list(fib(15))
print(f)


"""

    总结：
    使用了yield关键字的函数不再是函数，而是生成器。（使用了yield的函数就是生成器）
    yield关键字有两点作用：
        保存当前运行状态（断点），然后暂停执行，即将生成器（函数）挂起
        将yield关键字后面表达式的值作为返回值返回，此时可以理解为起到了return的作用
    可以使用next()函数让生成器从断点处继续执行，即唤醒生成器（函数）
    Python3中的生成器可以使用return返回最终运行的返回值，而Python2中的生成器不允许使用return返回一个返回值
    （即可以使用return从生成器中退出，但return后不能有任何表达式）。


"""