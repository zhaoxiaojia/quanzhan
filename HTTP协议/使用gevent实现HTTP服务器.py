#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 9:17
# @Author  : Coco
# @Site    : SH #5-389
# @File    : 使用gevent实现HTTP服务器.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm


import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()


def server_client(new_socket, AC):
    AC = AC
    # 1. 接受客户端发送过来的请求
    request = new_socket.recv(1024).decode('utf-8')

    # 2. 获取请求中的文件地址
    file_name = ''
    request_lines = request.splitlines()
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == '/':
            file_name = '/index.html'

    # 3. 响应客户端请求，反馈数据
    html_content = ''
    try:
        with open('./html' + file_name, 'rb') as f:
            html_content = f.read()
    except:
        response = 'HTTP/1.1 404 NOT FOUND \r\n'
        response += '\r\n'
        response += 'NOT FOUND'
        new_socket.send(response.encode('utf-8'))
    else:
        response = 'HTTP/1.1 200 OK \r\n'
        response += '\r\n'
        new_socket.send(response.encode('utf-8'))
        new_socket.send(html_content)
    new_socket.close()


if __name__ == '__main__':
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(('', 7890))

    # 3. 监听
    tcp_server_socket.listen(128)

    AC = True

    while True and AC:
        # 4. 等待客户端进行连接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        gevent.spawn(server_client, (new_socket, AC))

    tcp_server_socket.close()
