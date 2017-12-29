def now():
    print('2017-09-11')

f = now
f()
print(f.__name__)
print(now.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2017-09-11')
now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-09-11 17:31:36')

now()

print(now.__name__)

import functools

def log(func):
    @functols.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator




