#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 21:23
# @Author  : Coco
# @Site    : SH #5-389
# @File    : 实现简单的HTTP服务器.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

import socket
import re


def service_client(new_socket):
    '''为这个客户端'''
    # 1. 接受浏览器发送过来的请求，即http请求
    # GET / HTTP/1.1
    # ......
    request = new_socket.recv(1024).decode('utf-8')
    request_lines = request.splitlines()
    print(request_lines)
    # GET /index.html HTTP/1.1
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    file_name = ''
    if ret:
        file_name = ret.group(1)
        if file_name=='/':
            file_name = '/index.html'

    html_content = ''
    try:
        with open('./html' + file_name, 'rb') as f:
            html_content = f.read()
    except:
        response = 'HTTP/1.1 404 NOT FOUND\r\n'
        response += '\r\n'
        response += 'not found '
    else:
        # 2. 返回http格式的数据，给浏览器
        # 2.1 准备发送给浏览器的数据 --header
        response = 'HTTP/1.1 200 OK \r\n'
        response += '\r\n'
        # 2.2 准备发送给浏览器的数据 --body
        # 将response header 发送给浏览器
        new_socket.send(response.encode('utf-8'))
        # 将 response body 发送给浏览器
        new_socket.send(html_content)
    # 关闭套接字
    new_socket.close()


if __name__ == '__main__':
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务端4次挥手之后资源能够立即释放，这样就保证了，下次在运行程序时，可以立即使用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(('', 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        service_client(new_socket)
    # 关闭监听套接字
