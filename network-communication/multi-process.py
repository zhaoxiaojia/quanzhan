#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/6 18:55
# @Author  :Coco
# @FileName: multi-process.py

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

import multiprocessing
import time


def test1():
    while True:
        print('1-----')
        time.sleep(1)


def test2():
    while True:
        print('2-----')
        time.sleep(1)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()
