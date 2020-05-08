#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 9:37
# @Author  : Coco
# @Site    : SH #5-389
# @File    : 自己实现一个可迭代对象.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm
from collections.abc import Iterator
from collections.abc import Iterable


class Classmate:
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


# class ClassIterator:
#     def __init__(self, obj):
#         self.obj = obj
#         self.current_num = 0
#
#     def __iter__(self):
#         pass
#
#     def __next__(self):
#         if self.current_num < len(self.obj.names):
#             ret = self.obj.names[self.current_num]
#             self.current_num += 1
#             return ret
#         else:
#             raise StopIteration

if __name__ == '__main__':
    classmate = Classmate()
    classmate.add('coco')
    classmate.add('zeus')
    classmate.add('sven')
    classmate_iterator = iter(classmate)
    print('判断classmate_iterator是否是可迭代对象')
    print(isinstance(classmate_iterator, Iterator))
    print('判断classmate是否是迭代器')
    print(isinstance(classmate, Iterable))
    # print(next(classmate_iterator))
    for name in classmate:
        print(name)
