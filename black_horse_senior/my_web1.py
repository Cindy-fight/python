import socket

"""

Web静态服务器-1-显示固定的页面

"""


def handle_client(client_socket):
    recv_data = client_socket.recv(1024).decode('utf-8')
    request_headers_lines = recv_data.splitlines()
    for line in request_headers_lines:
        print(line)

    # response_headers = "HTTP/1.1 200 OK\r\n"
    # response_headers += "\r\n"

    response_body = "hello world"

    # response = response_headers + response_body
    client_socket.send(response_body.encode('utf-8'))
    client_socket.close()



def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 7788))
    server_socket.listen(128)
    while True:
        client_socket, client_addr = server_socket.accept()
        handle_client(client_socket)


if __name__ == '__main__':
    main()


