import re

class Dict(dict):
    '''

    Simple dict but also support access as x,y style.

    >>> d1 = Dict()
    >>> d1['x'] = 200
    >>> d1.x
    200
    >>> d1['y'] = 500
    >>> d1.y
    500
    >>> d2 = Dict(a=1, b=2, c='3')
    >>>
    >>> d2.a
    1
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
      File "<stdin>", line 6, in __getattr__
    KeyError: 'empty'

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 8, in __getattr__
    AttributeError:  'Dict' object has no attribute 'empty'

    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r" 'Dict' object has no attribute '%s' " % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()

