import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def test():
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(8):
        print('thread %s >>> %s' % (threading.current_thread().name, i))
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
ts = threading.Thread(target=test, name='WttTest')
t.start()
t.join()
ts.start()
ts.join()
print('thread %s ended.' % threading.current_thread().name)