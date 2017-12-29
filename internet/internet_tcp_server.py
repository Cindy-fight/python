#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

'''
一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。
'''

import socket
import threading, time

# 首先，创建一个基于IPv4和TCP协议的Socket：
# 创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
# SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 然后，绑定监听的地址和端口
s.bind(('127.0.0.1', 8002))

# 紧接着，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection from %s : %s ...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)

# 接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接
while True:
    sock, addr = s.accept()   # 接受一个新连接
    t = threading.Thread(target=tcplink, args=(sock, addr))  # 创建新线程来处理TCP连接
    t.start()



