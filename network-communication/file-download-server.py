#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 9:35
# @Author  : Coco
# @Site    : SH #5-389
# @File    : file-download-server.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

import socket


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定信息
    tcp_server_socket.bind("", 7890)
    # 3. 将手机设置为正常的 响铃模式（让默认的套接字由主动变为被动）
    tcp_server_socket.listen(128)
    # 4. 等待客户端的链接accept（）
    new_client_socket, client_addr = tcp_server_socket.accept()
    # 5. 接受客户端发送过来的 要下载的文件名
    filename = new_client_socket.recv(1024)
    print('客户端（%s)需要下载的文件是：%s' % (str(client_addr), filename))
    # 6. 会送一部分数据给客户端
    new_client_socket.send('coco'.encode('utf-8'))
    # 7. 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
