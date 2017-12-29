from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)
print(p.y)

print(isinstance(p, Point))

print(isinstance(p, tuple))

Circle = namedtuple('Circle1', ['x', 'y', 'r'])
print(Circle(3, 4, 6))

q = deque(['a', 'b', 'c'])
q.append('C')
q.appendleft('T')
print(q)
q.pop()
q.popleft()
print(q)

dd = defaultdict(lambda :'N/A')
dd['key1'] = 'WTT'
print(dd['key1'])
dd['key2'] = 'YRC'
print(dd['key2'])
print(dd['key3'])

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# FIFO first in first out 类似于队列
# ? 没有看到效果  需温习
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

LastUpdatedOrderedDict(od)

c = Counter()

for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
print(c.most_common(3))


