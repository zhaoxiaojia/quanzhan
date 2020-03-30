#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 12:14
# @Author  : Coco
# @Site    : SH #5-389
# @File    : socket-example.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm


import socket

if __name__ == '__main__':
    # 创建一个UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 可以使用套接字收发数据
    udp_socket.sendto('Fuck the world',('127.0.0.1',8080))
    # 关闭套接字
    udp_socket.close()
