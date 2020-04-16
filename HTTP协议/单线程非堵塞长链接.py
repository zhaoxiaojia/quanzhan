#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/16 21:35
# @Author  :Coco
# @FileName: 单线程非堵塞长链接.py

# @Software: PyCharm
"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓ ┏┓
            ┏┛┻━┛┻━┓
            ┃   ☃  ┃
            ┃ ┳┛ ┗┳ ┃
            ┃   ┻   ┃
            ┗━┓   ┏━┛
               ┃     ┗━━┓
               ┃        ┣┓
               ┃　      ┏┛
               ┗┓┓━━┳┓━┛
                 ┃┫  ┃┫
                 ┗┛  ┗┛
"""

import socket
import re


def server_client(new_socket, request):
    request_lines = request.splitlines()
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    file_name = ''
    if ret:
        file_name = ret.group(1)
        if file_name == '/':
            file_name = '/index.html'

    try:
        print(file_name)
        with open('./html' + file_name, 'rb') as f:
            html_content = f.read()
    except Exception:
        print('---File not found---')

        response = 'HTTP/1.1 404 NOT FOUND\r\n'
        response += '\r\n'
        # 请求头中添加 body长度信息，长链接中使用 发送字节长度到达改长度时 会发送数据无需close

        new_socket.send(response.encode('utf-8'))
    else:
        response_body = html_content
        response_header = 'HTTP/1.1 200 OK\r\n'
        response_header += 'Content-Length:%d\r\n' % len(response_body)
        response_header += '\r\n'
        response = response_header.encode('utf-8') + response_body
        new_socket.send(response)


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    tcp_server_socket.bind(('', 7890))
    tcp_server_socket.listen(128)
    # 将套接字变为非堵塞
    tcp_server_socket.setblocking(False)
    client_socket_list = list()
    while True:
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception:
            ...
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode('utf-8')
            except Exception:
                ...
            else:
                if recv_data:
                    server_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)
    tcp_server_socket.close()
