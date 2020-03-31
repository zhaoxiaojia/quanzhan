#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 8:17
# @Author  : Coco
# @Site    : SH #5-389
# @File    : socket-bind.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm


import socket

if __name__ == '__main__':
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定一个本地信息
    local_addr = ('', 7788)
    udp_socket.bind(local_addr)
    while True:
        # 3.接受数据
        recv_data = udp_socket.recvfrom(1024)
        # recv_data 接收到的数据为元祖（接受到的数据，（发送方的ip，port)
        recv_msg = recv_data[0]  # 存储接受到的数据
        send_addr = recv_data[1]  # 存储发送放的地址信息
        # 4.打印接收到的数据
        # print(recv_data)
        print("%s:%s" % (str(send_addr), recv_msg.decode('GBK')))
    # 5.关闭套接字
    udp_socket.close()
