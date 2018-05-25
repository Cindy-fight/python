"""

列表推导式
概念：快速生成列表元素的表达形式
格式：[计算公式 for循环 if判断]
特点：
    1、每循环一次，将计算公式的结果添加到列表中
    2、计算公式可以使用遍历出的数据
    3、for遍历出的数据，必须满足if判断，才会使用计算公式生成元素

"""

list1 = [i for i in range(1, 101)]
list2 = [i+1 for i in range(0, 100)]

print(list1)
print(list2)


# 正常模式
list3 = []
for i in range(1, 11):
    if i % 2 == 0:
        list3.append(i**2)

print(list3)


# 列表推导式
new_list3 = [i**2 for i in range(1, 11) if i%2 ==0]
print(new_list3)
