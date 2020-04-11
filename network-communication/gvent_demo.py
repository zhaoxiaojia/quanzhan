#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/11 10:16
# @Author  :Coco
# @FileName: gvent_demo.py

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

import gevent
import time
from gevent import monkey
# 可以先将代码中的time等延时操作替换为gevent延时操作 无需重构代码
monkey.patch_all()

'''
gevent 特点 遇到延时就会切换 否则不切换
延时通过 gevent 触发
'''
'''
进程，线程，携程
程序运行起来称之为进程，进程是资源分配的单位
线程执行代码，一个线程只能做一件事
单线程并发，利用携程
'''


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(1)
        # gevent.sleep(1)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(1)
        # gevent.sleep(1)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(1)
        # gevent.sleep(1)


if __name__ == '__main__':
    print('1')
    g1 = gevent.spawn(f1, 5)
    print('2')
    g2 = gevent.spawn(f2, 5)
    print('3')
    g3 = gevent.spawn(f3, 5)
    print('4')
    g1.join()
    g2.join()
    g3.join()
