# coding:utf-8
import hashlib

str = 'hello'

h1 = hashlib.md5()

h1.update(str.encode(encoding='utf-8'))

print(h1.hexdigest())





