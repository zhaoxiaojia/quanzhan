#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/8 6:40
# @Author  :Coco
# @FileName: multi-pool-copefile.py

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
import os
import time
import sys

def copy_file(q, origin, old_path, new_path):
    # print('进程%d 正在拷贝文件%s' % (os.getpid(), origin))
    # print('b' if '' else 'a ')
    # print(os.getpgid() if os.getpgid() else 'c')

    # time.sleep(1)
    a = open(old_path + '/' + origin, 'r', encoding='utf-8')
    str = a.read()
    a.close()

    b = open(new_path + '/' + origin, 'w', encoding='utf-8')
    b.write(str)
    b.close()

    # 如果拷贝完文件，那么向队列中写入一个消息，表示已经完成
    q.put(origin)

if __name__ == '__main__':
    new_folder_name = 'target'  # input('请输入目的文件夹名字：')
    if not os.path.exists(new_folder_name):
        print('该文件夹已存在，无需创建')
        os.mkdir(new_folder_name)
    source_folder_name = 'origin'  # input('请输入目标文件夹名字：')
    # 获取目标文件下所有文件
    file_names = os.listdir(source_folder_name)
    # 创建线程池
    po = multiprocessing.Pool(5)

    # 创建一个队列
    que = multiprocessing.Manager().Queue()
    for file_name in file_names:
        res = po.apply_async(copy_file, args=(que, file_name, source_folder_name, new_folder_name))

    po.close()
    # po.join()

    all_file_name = len(file_names)
    copy_ok_num = 0
    while True:

        file_name = que.get()
        # 每次从queue中get一个数据之后，当处理好相关问题，最后调用该方法，以提示q.join()是否停止阻塞，让线程向前执行或者退出
        que.task_done()
        copy_ok_num += 1
        # print('已经完成copy%s' % file_name)
        os.system('cls')
        print('\r拷贝的进度为 %.2f %%' % (copy_ok_num * 100 / all_file_name),end='')
        if copy_ok_num >= all_file_name:
            break
        print()