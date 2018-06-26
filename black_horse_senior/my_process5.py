from multiprocessing import Queue,Process
import time,random


'''

进程间通信-Queue

'''

def write(q):
    for value in ['A', 'B', 'C', 'D']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue...' % value)
            time.sleep(random.random())
        else:
            break



if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pw.join()

    pr.start()
    pr.join()

    print()
    print('所有数据都写入并且读完')
