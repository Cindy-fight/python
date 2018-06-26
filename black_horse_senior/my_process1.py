import multiprocessing,time,os

def run_proc():
    # os.getpid()  获取当前进程的进程号
    print('子进程运行中，pid=%d' % os.getpid())
    print('子进程将要结束...')


if __name__ == "__main__":
    print('父进程pid:%d' % os.getpid())
    p = multiprocessing.Process(target=run_proc)
    p.start()
