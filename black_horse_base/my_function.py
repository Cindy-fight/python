def func_sum():
    """ 求和 1+2+3...+100 """
    i = 1
    sum_num = 0
    while i <= 100:
        sum_num += i
        i += 1
    print(sum_num)

func_sum()



def func_sum2(num1=0, num2=0):
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))

func_sum2(20, 30)

func_sum2()



a = 10
def func():
    # global a    修改全局变量
    a = 5
    print(a)

func()
print(a)


# 字典型可变形参
def print_info(name, **kwargs):
    print(name)
    print(kwargs)

print_info(name='Cindy', age=20, height=1.75)



# 组包和拆包
# 组包  =右边有多个数据时，会自动包装为元组
result = 10, 20, 30
print(result)    # (10, 20, 30)


# 拆包  变量数量 = 容器长度 ，容器中的元素会一一对应赋值给变量   ？？？有待理解

# 注意1：拆包时需要拆的数据的个数要与变量的个数相同，否则程序会异常
# 注意2：除了对元组拆包之外，还可以对列表、字典等拆包

# 应用1：交换变量的值
a1 = 10
b1 = 20
a1, b1 = b1 , a1
print(a1)
print(b1)

# 应用2：多个返回值
def func1():
    high = 178
    weight = 100
    age = 18
    return high, weight, age

result_func = func1()
print(result_func)

a, b, c = func1()
print(a)
print(b)
print(c)

# 应用三：元组解包
dict1 = {'name':'Cindy', 'age': 18}
for key,value in dict1.items():
    print(key)
    print(value)

# python 中可以使用 id函数 查看变量的引用地址，引用地址相等，说明指向同一个内存空间

m = 10
n = m
print(id(m))
print(id(n))
# 总结：m n 的引用地址相同

c = [10, 20]
d = c
c.append(30)
print(c)
print(d)
print(id(c))
print(id(d))
# 总结：c d的引用地址相同


f = [10, 20, 30]
print(id(f))
# f虽然和c d 的内容相同， 但是他们的引用地址不同


"""

可变类型与不可变类型

可变类型：
    1. 列表 list
    2. 字典 dict
    
不可变类型：
    1. 数值类型 int long float bool
    2. 字符串 str
    3. 元组 tuple

"""



"""

匿名函数
定义匿名函数：lambda 形参列表：返回值
调用匿名函数：(lambda 形参列表：返回值)(实参列表)

"""

lambda_result = (lambda num1,num2:num1+num2)(1, 3)
print(lambda_result)



"""

递归函数

"""

def step_num(num):
    if num > 1:
        return num * step_num(num-1)
    else:
        return 1

number = step_num(4)
print(number)