import time
import threading

"""
在一个进程内，所有线程共享全局变量，很方便在多个线程间数据共享
缺点就是：线程是对全局变量 随意遂改 可能造成 多线程之间对全局变量的混乱（即 线程非安全）

"""

g_num = 100

def work1(nums):
    global g_num
    for i in range(3):
        g_num += 1

    print('---in work1, g_num is %d---' % g_num)

    nums.append(44)
    print('---in work1---',nums)


def work2(nums):
    global g_num
    for i in range(3):
        g_num += 1

    print('---in work2, g_num is %d---' % g_num)
    print('---in work2---',nums)


g_nums = [11, 22, 33]


print('线程创建之前 g_num is %d' % g_num)
print('线程创建之前 g_nums ',g_nums)

t1 = threading.Thread(target=work1, args=(g_nums,))
t1.start()

# time.sleep(1)

t2 = threading.Thread(target=work2, args=(g_nums,))
t2.start()

print('线程执行完毕 g_num is %d' % g_num)
