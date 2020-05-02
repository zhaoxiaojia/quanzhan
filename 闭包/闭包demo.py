#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/5/1 21:56
# @Author  :Coco
# @FileName: 闭包demo.py

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
'''
函数：将代码封装成一个小整体 传递的是这个函数的引用 只有功能
匿名函数：传递的是这个函数的引用 只有功能
对象：传递很多数据+功能
闭包：能定义一个空间只传递一部分数据+功能
'''


def line(k, b):
    def create_y(x):
        print(k * x + b)

    return create_y

x=300
def test1():
    x = 200

    def test2():
        nonlocal x
        print('----1----%d' % x)
        x = 100
        print('----1----%d' % x)

    return test2


if __name__ == '__main__':
    line = line(1, 2)
    line(0)
    line(1)
    line(2)
    t1 = test1()
    t1()