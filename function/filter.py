def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'c', None])))

# su shu
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 100:
        print(n)
    else:
        break

# hui shu
# method 1
def is_palindrome(n):
    m = int(str(n)[::-1])
    return n == m
print(list(filter(is_palindrome, range(1000))))

# method 2
is_palindrome = lambda n: str(n) == str(n)[::-1]
print(list(filter(is_palindrome, range(1000))))

