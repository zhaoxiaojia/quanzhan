#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/8 6:18
# @Author  :Coco
# @FileName: multi-process-pool.py

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

from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print('%s 开始执行，进程号为%d' % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print('%s 执行完毕，耗时%0.2f' % (msg, t_stop - t_start))


if __name__ == '__main__':
    po = Pool(3)
    for i in range(0, 10):
        po.apply_async(worker, (i,))
    print('-----start-----')
    po.close()
    # 等待所有子进程结束
    po.join()
    print('-----end-----')
