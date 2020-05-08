#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/5/2 7:25
# @Author  :Coco
# @FileName: 装饰器demo.py

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


class Test:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('这里是装饰器添加的功能')
        return self.func(*args, **kwargs)


def add_func(func):
    print('----开始进行装饰权限1的功能----')

    def inner(*args, **kwargs):
        print('----正在验证权限1----')
        print('----权限验证ok----')
        return func(*args, **kwargs)

    return inner


def set_func(func):
    print('----开始进行装饰权限xxx的功能----')

    def inner(*args, **kwargs):
        print('----正在验证权限xxx----')
        print('----权限验证ok----')
        return func(*args, **kwargs)

    return inner


@Test
@add_func  # 后执行
@set_func  # 先执行
def test1(num, *args, **kwargs):
    print('----test1----%d' % num)
    print('----test1----', args)
    print('----test1----', kwargs)
    return 'ok'


if __name__ == '__main__':
    # test1(100)
    # test1(100, 200, 300)
    print(test1(100, 200, 300, mm=100))
'''
----开始进行装饰权限xxx的功能----
----开始进行装饰权限1的功能----
这里是装饰器添加的功能
----正在验证权限1----
----权限验证ok----
----正在验证权限xxx----
----权限验证ok----
----test1----100
----test1---- (200, 300)
----test1---- {'mm': 100}
ok
'''