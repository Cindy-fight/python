#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8002))

print(s.recv(1024).decode('utf-8'))

for data in [b'Sarah', b'Michael', b'Tracy']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()