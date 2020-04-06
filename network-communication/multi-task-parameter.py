#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/6 11:15
# @Author  :Coco
# @FileName: multi-task-parameter.py

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

import threading
import time

g_num = 0
g_nums = [11, 22]

# 创建一个互斥锁
mutex = threading.Lock()


def test1(temp):
    global g_num
    mutex.acquire()
    for i in range(temp):
        # 上锁，如果之前没有被上锁，那么此时，上锁成功
        # 如果上锁之前 已经被上锁了，那么此时会堵塞在这里，直到 这个锁被解开位置
        g_num += 1
        # 解锁
    mutex.release()
    print('----- in test 1 g_nums= %d -----' % g_num)


def test2(temp):
    global g_num
    mutex.acquire()
    for i in range(temp):
        g_num += 1
    mutex.release()
    print('----- in test 2 g_num= %s -----' % g_num)


if __name__ == '__main__':
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()
    print('----- in main thread g_gum = %d -----' % g_num)
