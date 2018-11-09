import schedule
import time

'''

创建定时任务

'''

def job():
    print('Hello world!')


schedule.every(10).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
