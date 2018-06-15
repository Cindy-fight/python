import time
import threading

"""

在多个线程中，同时对一个变量操作，数据量过大会造成数据混乱，这个时候可以加入 互斥锁 解决这个问题

某个线程要更改数据时，先将其锁定，此时资源的状态为'锁定'，其他线程不能更改； 直到该线程释放资源，将资源的状态变为'非锁定'，
其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。

具体步骤为：
mutex = threading.Lock()    # 创建锁

mutex.acquire() # 锁定

mutex.release()  # 释放

加锁的好处：确保了某段关键代码 只能由 一个线程 从头到尾 完整的执行
锁的坏处：1、阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大下降了
        2、由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁


"""

g_num = 0

mutex = threading.Lock()

def work1(num):
    global g_num
    for i in range(num):
        mutex.acquire() # 上锁
        g_num += 1
        mutex.release()  # 解锁

    print('---in work1, g_num is %d---' % g_num)


def work2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()

    print('---in work2, g_num is %d---' % g_num)



print('线程创建之前 g_num is %d' % g_num)

t1 = threading.Thread(target=work1, args=(1000000,))
t1.start()

t2 = threading.Thread(target=work2, args=(1000000,))
t2.start()

# time.sleep(1)

while len(threading.enumerate()) != 1:
    time.sleep(1)

print('两个线程同时对一个全局变量操作之后的最终结果是：%d' % g_num)
