#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

import socket

# 1 创建UDP套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# 2 准备接收方的地址
# '127.0.0.1' 表示目的IP地址
# 8080表示目的端口
dest_addr = ('127.0.0.1', 8080)    # 注意是元组，ip是字符串，端口是数字


# 3 从键盘获取数据
send_data = input('请输入要发送的数据：')


# 4 发送数据到指定的电脑上的指定程序中
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)


# 5 等待接收对方发送数据
# recv_data = udp_socket.recvfrom(1024)    # 1024表示本次接收的最大字节数


# 6 显示对方发送的数据
# 接收的数据recv_data 是一个元组
# 第一个元素是 对方发送的数据
# 第二个元素是 对方的IP和端口
# print(recv_data[0].decode('utf-8'))
# print(recv_data[1])

# print(udp_socket.recv(1024).decode('utf-8'))


# 7 关闭套接字
udp_socket.close()