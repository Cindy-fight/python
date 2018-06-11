#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

'''
udp 聊天器
1 获取键盘数据 并将其发送给对方
2 接收数据并显示

'''

import socket

def send_msg(udp_socket):
    msg = input("\n 请输入要发送的数据：")
    dest_ip = input("\n 请输入目的IP地址：")
    dest_port = input("\n 请输入目的端口号：")
    if dest_port.isdecimal():
        dest_port = int(dest_port)
        udp_socket.sendto(msg.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
    data, addr = udp_socket.recvfrom(1024)
    print(">>>%s:%s" % (addr, data.decode('utf-8')))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('127.0.0.1', 6666))
    print('=' * 30)
    print('1:发送消息')
    print('2:接收消息')
    print('=' * 30)
    op_num = input("请输入要操作的功能序号：")

    if op_num == '1':
        send_msg(udp_socket)
    elif op_num == '2':
        recv_msg(udp_socket)
    else:
        print('输入有误，请重新输入...')



if __name__ == '__main__':
    main()

