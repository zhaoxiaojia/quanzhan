#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/5/2 11:00
# @Author  :Coco
# @FileName: 带有参数的装饰器.py

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


def set_level(level_num): # 改成嵌套用于传递参数
    def set_func(func): # 改成嵌套用于传递函数引用
        def call_func(*args, **kwargs):
            print('权限等级为:%d' % level_num)
            return func()

        return call_func

    return set_func


@set_level(1)
def test1():
    print('-----test1-----')
    return 'ok'


@set_level(2)
def test2():
    print('-----test2-----')
    return 'ok'


if __name__ == '__main__':
    test1()
    test2()
