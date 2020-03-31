#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 9:47
# @Author  : Coco
# @Site    : SH #5-389
# @File    : socket-demo.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

import socket


def send_msg(udp_socket):
    '''
    发送消息
    :return:
    '''
    # 发送
    # 获取要发送的内容
    dest_ip, dest_port = ' ', ' '
    if dest_ip:
        dest_ip = input('请输入对方的ip')
    if dest_port:
        dest_port = int(input('请输入对方的port'))
    send_data = input('请输入要发送的内容：')
    udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
    '''
    接受数据
    :return:
    '''
    # 接受并显示
    recv_data = udp_socket.recvfrom(1024)
    print("%s%s" % (str(recv_data[1]), recv_data[0].decode('GBK')))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定信息
    udp_socket.bind(('', 7788))
    # 循环来进行处理事情
    while True:
        print('-----自闭聊天室------')
        print('1:发送消息')
        print('2:接受消息')
        print('0:退出聊天')
        op = input('请输入功能：')
        if op == '1':
            # 发送
            send_msg(udp_socket)
        elif op == '2':
            # 接受
            print('c')
            recv_msg(udp_socket)
        elif op == '0':
            break
        else:
            print('输入有误，请重新输入')

if __name__ == '__main__':
    main()
