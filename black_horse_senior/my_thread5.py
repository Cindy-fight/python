import time
import threading

"""
在一个进程内，所有线程共享全局变量，很方便在多个线程间数据共享
缺点就是：线程是对全局变量 随意遂改 可能造成 多线程之间对全局变量的混乱（即 线程非安全）


如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确
num 的赋值越大，最终结果混乱的可能性越大，  循环次数越大 混乱的可能性越大
经测试：10万 数据正常   100万数据混乱

"""

g_num = 0

def work1(num):
    global g_num
    for i in range(num):
        g_num += 1

    print('---in work1, g_num is %d---' % g_num)


def work2(num):
    global g_num
    for i in range(num):
        g_num += 1

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
