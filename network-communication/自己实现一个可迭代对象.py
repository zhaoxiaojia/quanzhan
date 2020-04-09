#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 9:37
# @Author  : Coco
# @Site    : SH #5-389
# @File    : 自己实现一个可迭代对象.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm
from collections import Iterator
from collections import Iterable

class Classmate:
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return ClassIterator()


class ClassIterator:
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        return 11


if __name__ == '__main__':
    classmate = Classmate()
    classmate.add('coco')
    classmate.add('zeus')
    classmate.add('sven')
    classmate_iterator = iter(classmate)
    print(isinstance(classmate_iterator, Iterator))
    print(classmate_iterator)
    # for name in classmate:
    #     print(name)
