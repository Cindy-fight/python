from multiprocessing import Pool
import time,random,os


'''

进程池  Pool

'''


def worker(msg):
    t_start = time.time()

    print("%s 开始执行，进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)

    t_end = time.time()

    print(msg,"执行完毕，总耗时%.2f" % (t_end-t_start))



"""
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；
但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，直到池中有进程结束，才会用之前的进程来执行新的任务
"""

p = Pool(3)    # 定义一个进程池，最大进程数 3
for i in range(0, 10):
    # Pool().apply_async(要调用的目标,(传递给目标的参数元组,))
    # 每次循环将会用空闲出来的子进程去调用目标
    p.apply_async(worker, (i,))


print('-----start-----')
p.close()   # 关闭进程池，关闭后p不再接受新的请求
p.join()    # 等待p中所有子进程执行完成，必须放在close语句之后
print('-----end-----')


"""

multiprocessing.Pool常用函数解析：

    apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出
    才能执行下一个进程），args为传递给func的参数列表，kwds为传递给func的关键字参数列表；
    close()：关闭Pool，使其不再接受新的任务；
    terminate()：不管任务是否完成，立即终止；
    join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；


"""