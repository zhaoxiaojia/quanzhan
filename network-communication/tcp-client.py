#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/1 6:23
# @Author  :Coco
# @FileName: tcp-client.py

# @Software: PyCharm
"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓ ┏┓
            ┏┛┻━┛┻━┓
            ┃      ☃  ┃
            ┃ ┳┛ ┗┳ ┃
            ┃     ┻   ┃
            ┗━┓   ┏━┛
               ┃      ┗━━┓
               ┃           ┣┓
               ┃　       ┏┛
               ┗┓┓━━┳┓━┛
                 ┃┫  ┃┫
                 ┗┛  ┗┛
"""

import socket


def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.连接服务器
    server_ip = input('请输入服务器ip：')
    server_port = int(input('请输入服务器port：'))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)
    while True:
        # 3.发送数据/接收数据
        send_data = input('请输入要发送的数据：')
        tcp_socket.send(send_data.encode('utf-8'))
    # 4.关闭套接字
    tcp_socket.close()



if __name__ == '__main__':
    main()
