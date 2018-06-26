
'''

斐波那契数列

'''


class FibIterator(object):

    def __init__(self, n):
        self.n = n
        self.current = 0
        self.num1 = 0
        self.num2 = 1


    def __next__(self):
        if self.current < self.n:
            num = self.num1
            self.num1,self.num2 = self.num2,self.num1+self.num2
            self.current += 1
            return num
        else:
            raise StopIteration


    def __iter__(self):
        return self



if __name__ == '__main__':
    fib = FibIterator(20)
    for i in fib:
        print(i)



li = list(FibIterator(10))
print(li)

tp = tuple(FibIterator(15))
print(tp)



# 总结：for循环 、  list  、  tuple  都可以接收可迭代对象
