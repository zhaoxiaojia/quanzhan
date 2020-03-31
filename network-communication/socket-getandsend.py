#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 9:11
# @Author  : Coco
# @Site    : SH #5-389
# @File    : socket-getandsend.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

import socket

if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 获取对方的ip/prot
    dest_ip = input('请输入对方的ip：')
    dest_port = int(input('清输入对方的端口：'))
    # while True:
    # 从键盘获取数据
    send_data = input('请输入你的数据：')
    # if send_data == 'exit':
    #     break
    udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))
    # 接受回来的数据
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('GBK'))
    udp_socket.close()
