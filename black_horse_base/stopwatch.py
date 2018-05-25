# 电子秒表
import time
h = 0
while h <= 23:
    m = 0
    while m <= 59:
        s = 0
        while s <= 59:
            print("%02d:%02d:%02d" % (h, m, s))
            time.sleep(1)
            s += 1
        m += 1
    h += 1
