from multiprocessing import Pool,Manager
import os,time,random


'''

进程池中的Queue

'''


def read(q):
    print("read 启动(%s),父进程(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("read 从 Queue 中获取到消息：%s" % q.get(True))


def write(q):
    print("write 启动(%s),父进程(%s)" % (os.getpid(), os.getppid()))
    for i in 'itcast':
        q.put(i)



if __name__ == '__main__':
    print("(%s) start" % os.getpid())
    q = Manager().Queue()
    po = Pool()
    po.apply_async(write, (q,))

    time.sleep(random.random()*10)

    po.apply_async(read, (q,))
    po.close()
    po.join()
    print("(%s) End" % os.getpid())
