'''
用列表作函数的默认参数
'''

def func(a, b=None):
    if b is None:
        b = []
    b.append(a)
    print(f'a:{a}')
    print(f'b:{b}')

func(1)
func(2)




'''
 文件操作
'''

with open('/tmp/wtt.log') as file:
    for line in file:
        print(line)



'''
捕获所有异常
'''
try:
    pass
except Exception as e:
    print('Exception {e}')



'''
忽略 Python 的 for…else 语法
'''
numbers = [1,2,3,4,5]
for i in numbers:
    if i % 2 == 1:
        print('is odd')
        # break
    else:
        print('is not odd')



'''
使用键遍历字典
'''
member = {'name':'cindy','age':18,'mobile':123}
for key,val in member.items():
    print(f'{key}:{val}')

