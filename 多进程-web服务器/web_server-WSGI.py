#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/29 21:54
# @Author  :Coco
# @FileName: web_server-WSGI.py

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
import multiprocessing
import time
import mini_frame
import os


class WSGIServer:
    def __init__(self):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.tcp_server_socket.bind(('', 7890))
        self.tcp_server_socket.listen(128)

    def server_client(self, new_socket):
        request = new_socket.recv(1024).decode('utf-8')
        if not request:
            return
        request_lines = request.splitlines()
        file_name = ''
        ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
        if ret:
            file_name = ret.group(1)
            if file_name == '/':
                file_name = '/index.html'
        if not file_name.endswith('.py'):
            # 然后请求的资源不是以.py结尾 那么就认为是静态资源(html/css/js/png,jpg)等
            try:
                with open('../HTTP协议/html' + file_name, 'rb') as f:
                    html_content = f.read()
            except:
                responce = 'HTTP/1.1 404 NOT FOUND \r\n'
                responce += '\r\n'
                responce += '----- file not found -----'
                new_socket.send(responce.encode('utf-8'))
            else:
                responce_body = html_content
                responce_header = 'HTTP/1.1 200 ok\r\n'
                responce_header += '\r\n'
                responce = responce_header.encode('utf-8') + responce_body
                new_socket.send(responce)
        else:
            # 如果是以.py结尾，那么就认为是动态资源的请求

            # if file_name == '/login.py':
            #     body = mini_frame.login()
            # elif file_name == 'register.py':
            #     body = mini_frame.register()
            env = dict()
            env['PATH_INFO'] = file_name
            body = mini_frame.application(env, self.set_response_header)
            header = 'HTTP/1.1 %s\r\n' % self.status
            for temp in self.headers:
                header += '%s:%s\r\n' % (temp[0], temp[1])
            header += '\r\n'
            response = header + body
            new_socket.send(response.encode('utf-8'))
        new_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [('server', 'mini_web v8.8')]
        self.headers += headers

    def run_forever(self):
        while True:
            new_socket, client_addr = self.tcp_server_socket.accept()
            p = multiprocessing.Process(target=self.server_client, args=(new_socket,))
            p.start()
            new_socket.close()
        self.tcp_server_socket.close()


if __name__ == '__main__':
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()
