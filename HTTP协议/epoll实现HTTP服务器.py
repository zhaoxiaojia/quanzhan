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
import select


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

    # 创建一个epoll对象
    epl = select.epoll()

    # 将对应的套接字fd注册到epoll
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)
    fd_event_dict = dict()
    while True:
        # 默认会堵塞，直到os 监测到数据到来，通过事件通知方式 告诉这个程序，此时才会解堵塞
        fd_event_list = epl.poll()
        # [(fd,event),(套接字对应的文件描述符，这个文件描述符到死是个什么事件， 例如 可以调用recv接收等
        for fd, event in fd_event_list:
            # 等待新客户端的连接
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 判断已经链接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode('utf-8')
                if recv_data:
                    server_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]
