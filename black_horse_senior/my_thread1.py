import time
import threading


def saySorry():
    print('I was wrong. Honey,Can i eat dinner ?')
    time.sleep(1)


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()