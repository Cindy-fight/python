import base64

e = base64.b64encode(b'binary\x00string')
print(e)

d = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(d)

es = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(es)    #b'abcd++//'

dss = base64.urlsafe_b64decode('abcd++//')
print(dss)

ds = base64.urlsafe_b64decode('abcd--__')
print(ds)

en = base64.b64encode(b'abcd')
print(en)

de = base64.b64decode('YWJjZA==')
print(de)

#practice
def safe_base64_decode(s):
    num = len(s) % 4
    if num != 0:
        s = s + '=' * (4 - num)
    return base64.b64decode(s)

test1 = safe_base64_decode('YWJjZA==')
print(test1)

test2 = safe_base64_decode('YWJjZA')
print(test2)

