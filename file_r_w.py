f = open('/Users/admin/Sites/python/hello.py', 'r')
# str = f.read()
# print(str)

for line in f.readlines():
    print(line.strip())

f.close()

try:
    f1 = open('/Users/admin/Sites/python/str2int.py', 'r')
    print(f1.read())
finally:
    if f:
        f.close()


with open('/Users/admin/Sites/python/hello.py') as f2:
    print(f2.read())


# image use rb export:二进制
f_image = open('/Users/admin/Desktop/wtt.jpg', 'rb')
# print(f_image.read())
f_image.close()

# 字符编码
f_code = open('/Users/admin/Sites/python/gbk.txt', 'r', encoding='utf-8', errors = 'ignore')
print(f_code.read())

# write file
f_write = open('/Users/admin/Sites/python/gbk.txt', 'w')
f_write.write('Hello, World!, Hello, Honey！')
f_write.close()


from io import StringIO
fs = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = fs.readline()
    if s == '':
        break
    print(s.strip())


from io import BytesIO
fb = BytesIO(b'101001010')
print(fb.read())
fb.close()


