#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/7 6:56
# @Author  :Coco
# @FileName: multi-process-queue.py

# @Software: PyCharm
"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓ ┏┓
            ┏┛┻━┛┻━┓
            ┃   ☃  ┃
            ┃ ┳┛ ┗┳ ┃
            ┃    ┻ ┃
            ┗━┓  ┏━┛
               ┃    ┗━━┓
               ┃        ┣┓
               ┃　      ┏┛
               ┗┓┓━━┳┓━┛
                 ┃┫  ┃┫
                 ┗┛  ┗┛
"""

import multiprocessing
import time

def download_from_web(q):
    '''下载数据'''
    # 模拟从网上下载的数据
    data = [11, 22, 33, 44]
    # 向队列中写入数据
    for temp in data:
        q.put(temp)
        time.sleep(1)
    print('---下载完成----')


def analysis_data(q):
    '''数据处理'''
    waitting_analysis_data = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        print(data)
        time.sleep(1)
        waitting_analysis_data.append(data)
        if q.empty():
            break
if __name__ == '__main__':
    # 1. 创建一个队列
    q = multiprocessing.Queue()
    # 2. 创建多个进程，将队列的引用当做实参传递到里面
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()
