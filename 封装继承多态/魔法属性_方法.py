#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/23 6:12
# @Author  :Coco
# @FileName: 魔法属性_方法.py

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
    '''
    调用doc方法时 会显示这里的内容
    '''

    def __init__(self, name):
        self.__name = name

    def __call__(self, *args, **kwargs):
        print('__call__')

    def __str__(self):
        # 获取当前对象描述时会被调用
        return 'coco'

    # 用于索引操作，如字典。以上分别表示获取，设置，删除数据
    def __getitem__(self, item):
        print('__getitem___', item)

    # 设置
    def __setitem__(self, key, value):
        print('___setitem___', key, value)

    # 删除
    def __delitem__(self, key):
        print('___delitem___', key)

    # 该方法用于切片操作 如 列表
    def __getslice__(self, i, j):
        print('__getslice__', i, j)

    def __setslice__(self, i, j, sequence):
        print('__setslice__', i, j)

    def __delslice__(self, i, j):
        print('__delslice__', i, j)


if __name__ == '__main__':
    test = Test('coco')
    print(test.__dict__)
    print(Test.__dict__)
    print(Test.__doc__)
    print('打印当前操作对象是在哪个模块：', test.__module__)
    print('打印当前操作的对象的类是什么：', test.__class__)
    test.__call__()
    print(test)
    print('当前对象的描述是：%s' % test)
    # print(test.__name)

    result = test['k1']  # 自动触发执行 __getitem__
    test['k2'] = 'coco'  # 自动触发执行 __setitem__
    del test['k1']  # 自动触发执行 __delitem__

    test[-1:1]
    test[0:1] = [11, 22, 33, 44]
    del test[0:2]
