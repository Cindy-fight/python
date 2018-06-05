#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

import socket

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_server.bind(('127.0.0.1', 8080))

print('Bind udp on 8080...')

while True:
    data, addr = udp_server.recvfrom(1024)
    print('Received from %s:%s' % addr)
    print(data.decode('utf-8'))