#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/29 21:54
# @Author  :Coco
# @FileName: web_server_WSGI.py

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
# import dynamic.mini_frame
import os
import sys


class WSGIServer:
    def __init__(self, port, app):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.tcp_server_socket.bind(('', port))
        self.tcp_server_socket.listen(128)
        self.application = app

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
        if not file_name.endswith('.html'):
            # 然后请求的资源不是以.py结尾 那么就认为是静态资源(css/js/png,jpg)等
            try:
                with open('./static' + file_name, 'rb') as f:
                    html_content = f.read()
            except:
                response = 'HTTP/1.1 404 NOT FOUND \r\n'
                response += '\r\n'
                response += '----- file not found -----'
                new_socket.send(response.encode('utf-8'))
            else:
                responce_body = html_content
                responce_header = 'HTTP/1.1 200 ok\r\n'
                responce_header += '\r\n'
                response = responce_header.encode('utf-8') + responce_body
                new_socket.send(response)
        else:
            # 如果是以.py结尾，那么就认为是动态资源的请求

            # if file_name == '/login.py':
            #     body = mini_frame.login()
            # elif file_name == 'register.py':
            #     body = mini_frame.register()
            env = dict()
            env['PATH_INFO'] = file_name
            body = self \
                .application(env, self.set_response_header)
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
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])  # 7890
            frame_app_name = sys.argv[2]  # xxxx_frame:application
        except Exception as e:
            print('端口输入错误')
    else:
        print('请按照以下方式运行:')
        print('python3 xxx.py 7890 xxxx_frame:application')
    ret = re.match(r'([^:]+):(.*)', frame_app_name)
    if ret:
        frame_name = ret.group(1)  # xxxx_frame
        app_name = ret.group(2)  # application
    else:
        print('请按照以下方式运行:')
        print('python3 xxx.py 7890 xxxx_frame:application')
    # import frame_name 寻找 frame_name
    # sys.path.append('xxx/xxx')
    sys.path.append('./dynamic')
    frame = __import__(frame_name)  # 返回值标记 导入的模块
    app = getattr(frame, app_name)  # 此时app指向了dynamic/mini_frame模块中的application
    wsgi_server = WSGIServer(port, app)
    wsgi_server.run_forever()
