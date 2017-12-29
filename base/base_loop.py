print('Hello, world!')
print('The quick brown fox', 'jumps over', 'the lazy dog')
print(300)
print(100+200)
print('100 + 200 =', 100+200)

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum += x
print(sum)

sums = 0
for xs in range(101):
    sums += xs
print(sums)

# 奇数
sum_1 = 0
n = 99
while n > 0:
    sum_1 += n
    n -= 2
print('1-100奇数之和是：',sum_1)

# 偶数
sum_2 = 0
n2 = 100
while n2 > 0:
    sum_2 += n2
    n2 -= 2
print('1-100偶数之和是：',sum_2)

L = ['Bart', 'Lisa', 'Adam']
for l in L:
    print('Hello,',l, '!')

# test break
n3 = 1
while n3 <= 20:
    print(n3)
    n3 += 1
print('END')

n4 = 1
while n4 < 20:
    if n4 > 10:
        break
    print(n4)
    n4 += 1
print('END')

# test continue
n5 = 0
while n5 < 10:
    n5 += 1
    if(n5 % 2 == 0):
        continue
    print(n5)

# dict
d = {'Michael':95, 'Bob':86, 'Adam':92}
name1 = input('请输入你的姓名：')
if name1 in d:
    print('你想要查找的姓名为:',name1, '成绩为:',d[name1])
else:
    print('数据库中不存在你要查找的姓名:',name1)




