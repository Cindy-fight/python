'''

阶乘 factorial

'''

# 新手程序员
def factorial1(x):
    if x == 0:
        return 1
    else:
        return x * factorial1(x - 1)

print(factorial1(6))



# 第一年刚学完Pascal的新手
def factorial2(x):
    result = 1
    i = 2
    while i <= x:
        result = result * i
        i += 1
    return result

print(factorial2(7))



# 第一年刚学完C语言的新手


# 第一年刚学完SICP的新手


# 第一年刚学完Python的新手
def factorial5(x):
    res = 1
    for i in range(2, x+1):
        res *= i
    return res

print(factorial5(8))



# 爱偷懒的程序员
def factorial6(x):
    return x > 1 and x * factorial6(x-1) or 1

print(factorial6(9))



# 更懒得python程序员
factorial7 = lambda x: x and x * factorial7(x-1) or 1
print(factorial7(10))



# python 专家
# 导入functional包
# import operator as op
# import functional as f
# factorial8 = lambda x: f.foldl(op.mul, 1, range(2, x+1))
#
# print(factorial8(6))



# python 黑客
# @tailcall
def factorial9(x, acc=1):
    if x:return factorial9(x.__sub__(1), acc.__mul__(x))
    return acc
import sys
sys.stdout.write(str(factorial9(6)) + '\n')



# 专家程序员
# 导入c_math包



# 英语系的专家级程序员


# UNIX 程序员
# import os
# def factorial12(x):
#     os.system('factorial(' + str(x) + ')')
#
# print(factorial12(6))

