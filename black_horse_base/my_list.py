'''
list
1 append  在末尾追加值
2 insert  在指定位置插入值，超过索引会增加值
3 extend  将 可迭代对象中的元素 追加到列表
4 remove  删除指定值的 第一个匹配项
5 del     删除指定位置的值
6 pop     删除指定索引的值，并返回被删除的值
7 clear   清空列表
8 len     列表长度
9 if in   判断列表中是否包含某个值
10 index  根据值查询索引，返回第一个匹配项的索引，没有查到会报错
11 count  值在列表中出现的次数
11 sort   排序
12 reverse 逆序、反转
'''
my_list = [13, 5, 8]
print(my_list)

my_list.append(12)
print(my_list)

my_list.insert(1, 16)
print(my_list)

my_list.insert(10, 88)
print(my_list)

list2 = [20, 21]
my_list.extend(list2)
print(my_list)

my_list.remove(5)
print(my_list)

del my_list[3]
print(my_list)

pop_str = my_list.pop(4)
print(pop_str)
print(my_list)

my_list.clear()
print(my_list)


my_list = [13, 5, 8, 5]

my_list[1] = 18
print(my_list)

print(my_list[2])
print(my_list)

list_index = my_list.index(5)
print(list_index)

list_len = len(my_list)
print(list_len)

if 8 in my_list:
    print('OK')

list_count = my_list.count(13)
print(list_count)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.reverse()
print(my_list)

print(my_list[0])
