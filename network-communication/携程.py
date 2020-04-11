#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/11 9:58
# @Author  :Coco
# @FileName: 携程.py

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

import time


def task_1():
    while True:
        print('---1---')
        time.sleep(0.1)
        yield


def task_2():
    while True:
        print('---2---')
        time.sleep(0.1)
        yield


if __name__ == '__main__':
    t1 = task_1()
    t2 = task_2()
    while True:
        next(t1)
        next(t2)
