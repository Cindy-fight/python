#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

import socket


def  main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input('please input server ip:')
    server_port = int(input('please input server port:'))
    tcp_socket.connect((server_ip, server_port))

    file_name = input('please input the filename you want to download:')
    tcp_socket.send(file_name.encode('utf-8'))
    recv_data = tcp_socket.recv(2048)

    if recv_data:
        with open("download_"+file_name, 'wb') as f:
            f.write(recv_data)

    tcp_socket.close()



if __name__ == '__main__':
    main()