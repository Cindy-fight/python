'''
str
1  split  以分割符拆分字符串，返回列表
2  partition  返回元组，把字符串分成一个3元素的元组（分隔符前面，分隔符，分隔符后面）
3  join    以字符串来连接字符串列表中每个元素，合并为一个新的字符串
4  replace  返回一个替换了原内容的新字符串，第三个值可以指定替换次数
5  find   在指定范围内，查询目标字符串的索引，不存在返回-1
6  rfind  在指定范围内，查找目标字符串的索引，不存在返回-1，从结尾处开始查找
7  index  在指定范围内，查找目标字符串的索引，不存在会报错
8  isalpha()    如果 str 的所有字符 都为字符， 则返回True，否则返回False
9  isdecimal()  如果 str 都是数字，则返回 True， 否则返回 False
10 islower()      都是小写 True， 否则 False
11 isupper()      都是大写 True， 否则 False
12 startswith   检查字符串是否以 目标字符串 开头，是则返回 True
13 endswith     检查字符串是否以 目标字符串 结尾，是则返回 True
14 lower    转小写
15 upper    转大写
16 center    按照指定宽度返回新字符串，并基于原字符串  居中  ，可设置两端空白位置的填充字符
17 ljust     按照指定宽度返回新字符串，并基于原字符串 左对齐 ，可设置两端空白位置的填充字符
18 rjust     按照指定宽度返回新字符串，并基于原字符串 右对齐 ，可设置两端空白位置的填充字符
19 strip   返回新字符串，去除 字符串 左右两边的 目标字符串，不设置目标字符串则去除空格
20 lstrip  返回新字符串，去除 字符串 左边的    目标字符串，不设置目标字符串则去除空格
21 rstrip  返回新字符串，去除 字符串 右边的    目标字符串，不设置目标字符串则去除空格

'''

my_str = "hello python hello world"
print(my_str)

str_split = my_str.split(' ')
print(str_split)

str_partition = my_str.partition(' ')
print(str_partition)
my_str1 = 'ting.wang@maiob.cn'
print(my_str1.partition('@'))

print(my_str +' ' + my_str1)

name_list = ['beijing', 'shanghai', 'guangzhou']
str1 = '&&'
str_join = str1.join(name_list)
print(str_join)

str_replace = my_str.replace('l', 'L', 3)
print(str_replace)

str_find = my_str.find('py')
print(str_find)

print(my_str)
str_rfind = my_str.rfind('o')
print(str_rfind)

str_index = my_str.index('py')
print(str_index)

str_isalpha = my_str.isalpha()
print(str_isalpha)

str2 = 'python'
print(str2.isalpha())

str3 = '1234567890'
str_isdecimal = str3.isdecimal()
print(str_isdecimal)

print(my_str.isdecimal())

str_islower = my_str.islower()
print(str_islower)

str_isupper = my_str.isupper()
print(str_isupper)
str4 = 'HELLO'
print(str4.isupper())

str_startswith = my_str.startswith('hello')
print(str_startswith)

str_endswith = my_str.endswith('ld')
print(str_endswith)

str_lower = str4.lower()
print(str_lower)

str_upper = my_str.upper()
print(str_upper)

str_center = str4.center(11, '-')
print(str_center)

str_ljust = str4.ljust(11, '-')
print(str_ljust)

str_rjust = str4.rjust(11, '-')
print(str_rjust)

str_strip = str_center.strip('-')
print(str_strip)

str_lstrip = str_rjust.lstrip('-')
print(str_lstrip)

str_rstrip = str_ljust.rstrip('-')
print(str_rstrip)

