import multiprocessing
import os
import time

"""

给子进程指定的函数传递参数

"""

def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name=%s, age=%d, pid=%d' % (name, age, os.getpid()))
        print(kwargs)
        time.sleep(0.2)


if __name__ == '__main__':
    p = multiprocessing.Process(target=run_proc, args=('test', 18), kwargs={"m":20})
    p.start()
    time.sleep(1)
    p.terminate()  # 不管任务是否完成，立即终止子进程
    p.join()   # 是否等待子进程执行结束，或等待多少秒
