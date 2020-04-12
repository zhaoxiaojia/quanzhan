#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/11 10:12
# @Author  :Coco
# @FileName: greenlet_demo.py

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

from greenlet import greenlet
import time


def test1():
    while True:
        print('---A---')
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print('---B---')
        gr1.switch()
        time.sleep(0.5)


if __name__ == '__main__':
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()