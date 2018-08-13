def get_now_time():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

print(get_now_time())



