#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 8:55
# @Author  : Coco
# @Site    : SH #5-389
# @File    : tcp-server.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm


import socket

'''
监听套接字 负责等待有新的客户端进行连接
accept产生的新的套接字用来为客户端服务

'''


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.bind绑定ip和port
    tcp_server_socket.bind((('', 7890)))

    # 3.listen使套接字变为可以被动连接
    tcp_server_socket.listen((128))
    while True:
        # 该循环持续接受新的客户端
        print('等待新的客户端的到来。。。')
        # 4.accept等待客户端的链接
        new_client_socket, client_addr = tcp_server_socket.accept()
        print(client_addr)
        print('一个新的客户端已经到来。。。')
        while True:
            # 该循环持续从客户端发消息给服务端
            # 5.recv/send 接受发送数据
            recv_data = new_client_socket.recv(1024)
            print('客户端发送过来的请求是：%s' % recv_data.decode('utf-8'))
            if recv_data:
                # 回送一部分数据给客户端
                new_client_socket.send('coco'.encode('utf-8'))
            else:
                break
        new_client_socket.close()
        print('已经服务完毕')
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
