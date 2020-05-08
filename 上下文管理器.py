#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 8:19
# @Author  : Coco
# @Site    : SH #5-389
# @File    : 上下文管理器.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

from contextlib import contextmanager

'''
Python 还提供了一个contextmanager的装饰器，更进一步简化了上下文管理器的实现方法，用过yield将函数分割两部分，yield之前的语句在__enter__ 方法中执行，yield之后的语句在__exit__方法中执行。紧跟在yield 后面的值是函数的返回值
什么是上下文管理器？上下文管理器就是允许你可以自动地开始和结束一些事情
'''
@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()


class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('entering ...')
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('will exit')
        self.f.close()


if __name__ == '__main__':
    with File('out.txt', 'w') as f:
        print('writing ...')
        f.write('hello python')

    with my_open('out1.txt', 'w') as f:
        f.write('hello again')
