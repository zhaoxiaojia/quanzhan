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

from multiprocessing import Pool
import os


def copy_file(origin, old_path, new_path):
    a = open(old_path + '/' + origin, 'r', encoding='utf-8')
    str = a.read()
    a.close()
    b = open(new_path + '/' + origin, 'w', encoding='utf-8')
    print('线程%s 正在拷贝文件%s' % (os.getpgid(), origin))
    b.write('coco')
    print(str)
    b.write(str)
    b.close()


if __name__ == '__main__':
    new_folder_name = 'target'  # input('请输入目的文件夹名字：')
    if not os.path.exists(new_folder_name):
        print('该文件夹已存在，无需创建')
        os.mkdir(new_folder_name)
    source_folder_name = 'origin'  # input('请输入目标文件夹名字：')
    print(source_folder_name)
    # 获取目标文件下所有文件
    file_names = os.listdir(source_folder_name)
    # 创建线程池
    po = Pool(5)
    for file_name in file_names:
        print(file_name)
        po.apply_async(copy_file, args=(file_name, source_folder_name, new_folder_name))
    po.close()
    po.join()
