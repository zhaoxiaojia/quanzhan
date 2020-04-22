#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 19:05
# @Author  : Coco
# @Site    : SH #5-389
# @File    : property-demo.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm


class Foo:
    def func(self):
        print('coco')

    @property
    def prop(self):
        print('zeus')
        return 'a'


class Pager:
    def __init__(self, current_page):
        self.current_page = current_page
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page  * self.per_items
        return val


if __name__ == '__main__':
    # foo_obj = Foo()
    # foo_obj.func()
    # a = foo_obj.prop
    # print(a)
    p = Pager(1)
    print(p.start)
    print(p.end)
