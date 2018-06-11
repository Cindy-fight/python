#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

# 文件下载器
'''
下载器的实质：文件的读取与写入

中途遇到困难及解决方案：
遇到困难：文件复制不完全
分析、猜测：误以为是不识别中文符号等
最终原因：发送内容超出了发送接收设置的字节数
解决方案：将发送接收的字节数增大即可 client_socket.recv(2048)

'''

import socket

def get_file_content(file_name):
    try:
        with open(file_name, 'rb') as f:
            content = f.read()
        return content
    except:
        print("没有下载的文件：%s" % file_name)



def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('127.0.0.1', 8888)
    tcp_socket.bind(address)
    tcp_socket.listen(128)

    while True:
        client_socket, client_addr = tcp_socket.accept()
        recv_data = client_socket.recv(2048)
        file_name = recv_data.decode('utf-8')
        print('对方请求下载的文件名为:%s' % file_name)
        file_content = get_file_content(file_name)
        if file_content:
            client_socket.send(file_content)

    tcp_socket.close()



if __name__ == "__main__":
    main()