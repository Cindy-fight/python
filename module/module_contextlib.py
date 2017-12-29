try:
    f = open('/Users/admin/Sites/python/a_index.py', 'r')
    f.read()
finally:
    if f:
        f.close()

with open('/Users/admin/Sites/python/a_index.py', 'r') as f:
    f.read()

# 传统方法
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s ...' % self.name)

with Query('Cindy') as q:
    q.query()

# python方法
from contextlib import contextmanager

class Query2(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s ...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

# test
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print('Hello')
    print('World!')

# closing
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
