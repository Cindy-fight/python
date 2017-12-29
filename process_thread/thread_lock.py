import time, threading

# 银行存款
balance  = 0
# 防止内容混乱 加 锁
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    # 先存后取，结果应该为0 range的数越大  才能越体现多线程的混乱   才能越体现锁的作用
    for i in range(10000000):
        # 先要获取锁
        lock.acquire()
        try:
            # 放心的改吧
            change_it(n)
        finally:
            # 改完了一定要释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)