#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 12:14
# @Author  : Coco
# @Site    : SH #5-389
# @File    : socket-example.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm


import socket

'''
socket.SOCK_DGRAM  UDP连接
socket.SOCK_STREAM TCP连接
'''
if __name__ == '__main__':
    # 创建一个UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_socket.bind(("",7890))

    while True:
        # 从键盘获取数据
        send_data = input(' 请输入数据：')

        if send_data == 'exit':
            break

        # 可以使用套接字收发数据
        udp_socket.sendto(send_data.encode('utf-8'), ('10.18.19.100', 8080))
    # 关闭套接字
    udp_socket.close()
