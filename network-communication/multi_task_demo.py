#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/6 9:45
# @Author  :Coco
# @FileName: multi_task_demo.py

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

import time
import threading


def sing():
    for i in range(5):
        print('singing ...')
        time.sleep(1)


def dance():
    for i in range(5):
        print('dancing ...')
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    print(threading.enumerate())
