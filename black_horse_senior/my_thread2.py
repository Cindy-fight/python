#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

import time
import threading

def sing():
    for i in range(3):
        print('singing ... %d' % i)
        time.sleep(1)


def dance():
    for i in range(3):
        print('dancing ... %d' % i)
        time.sleep(1)


if __name__ == '__main__':
    print('---start---:%s' % time.ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    # time.sleep(5)

    while True:
        length = len(threading.enumerate())
        print('当前运行的进程数为：%d' % length)
        if length <= 1:
            break

        time.sleep(0.5)

    print('---over---:%s' % time.ctime())

