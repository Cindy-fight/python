import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5.update('You are my sunshine!'.encode('utf-8'))
md5.update('You are my sunshine, YRC'.encode('utf-8'))
print(md5.hexdigest())