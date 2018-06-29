import re

def my_preg(str):
    if re.match(r'^itcast(.*)',str):
        print('Preg ',str)
    else:
        print('Not preg match')


str = 'itcast hello python'
my_preg(str)


s1 = re.match('.', 'M')
print(s1)
print(s1.group())

s2 = re.match('t.o', 'too')
print(s2)
print(s2.group())

s3 = re.match('t.o', 'two')
print(s3)
print(s3.group())

s4 = re.match('h', 'hello Python')
print(s4.group())

s5 = re.match('H', 'Hello Python')
print(s5.group())

s6 = re.match('[0123456789]Hello python', '7Hello python')
print(s6.group())

s7 = re.match('[0-9]Hello python', '8Hello python')
print(s7.group())

s8 = re.match('[0-35-9]Hello python', '4Hello Python')       #前面匹配的数字是0-3 5-8   匹配不到4
print(s8)

# 匹配手机号
s9 = re.match('1[358][0-9]{9}', '15721243265')
print(s9)
print(s9.group())
print(s9.group(0))


# 匹配邮箱
# mail = '592557247@qq.com'
mail = 'ting.wang@maimob.cn'
email = re.match('^[0-9a-zA-Z.]{3,16}@[0-9a-zA-Z]{2,6}\.[a-zA-Z]{2,3}$', mail)
print(email)
print(email.group())


emails = re.match('^([0-9A-Za-z.]{3,16})@([0-9a-zA-Z]{2,6})\.([a-zA-Z]{2,3})$', mail)
print(emails)
print(emails.group(0))
print(emails.group(1))
print(emails.group(2))
print(emails.group(3))
print()


# findall
s10 = re.findall(r"\d+", "python=9999, c=7890, c++=12345")
print(s10)


# search
s11 = re.search(r"\d+", "阅读次数为 9999")
print(s11)
print(s11.group())

# sub 将匹配到的数据进行替换
s12 = re.sub(r'\d+', '1088', 'python=997')
print(s12)


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


# s13 = re.sub(r'\d+', add, 'python=997')
# print(s13)


# split 根据匹配进行切割字符串，并返回一个列表
s14 = re.split(r":| ", "info:xiaozhang 33 shandong")
print(s14)


# 贪婪 和 非贪婪
# 贪婪：尝试匹配尽可能多的字符
# 非贪婪：尝试匹配尽可能少的字符
# 在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪

# 第一种 贪婪模式
str = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'
s15 = re.search(r'https://.*\.jpg', str)
print(s15)
print(s15.group())
#匹配结果：https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg



# 第二种  非贪婪模式
s16 = re.search(r'https://.*?\.jpg', str)
print(s16)
print(s16.group())
# 匹配结果：https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg

# 说明： Python中字符串签名加上 r 表示原生字符串

m = re.match(r'^(\d{3,4})\-(\d{3,8})$', '0934-6616088')
# m = re.match(r'(\d{3,4})\-(\d{3,8})', '0934-6616088')
print(m)