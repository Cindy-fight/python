import re

test = '0934-6616088'
if re.match(r'^\d{3,4}\-\d{3,8}$', test):
    print('OK')
else:
    print('failed')


print(re.split(r'\s+', 'a b   c'))

print(re.split(r'[\s\,]+', 'a,b, c  d'))

print(re.split(r'[\s\,\;]+', 'a,b;; c,  d e'))

m = re.match(r'^(\d{3,4})-(\d{3,8})$', test)
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
