#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 19:05
# @Author  : Coco
# @Site    : SH #5-389
# @File    : property-demo.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm


class Foo1:
    def func(self):
        print('coco')

    @property
    def prop(self):
        print('zeus')
        return 'a'


class Foo2:
    def get_bar(self):
        return 'coco'

    BAR = property(get_bar)


class Foo3:
    '''
    property 方法中有四个参数
    调用 对象.属性 时自动触发执行方法
    调用 对象.属性 = xxx 时自动触发执行方法
    调用 del 对象.属性 是自动触发执行方法
    调用 对象.属性.__doc__ 此参数是该属性的描述信息
    '''

    def get_bar(self):
        print('getter...')
        return 'coco'

    def set_bar(self, value):
        '''必须两个参数'''
        print('setter...')
        return 'set value' + value

    def del_bar(self):
        print('deleter...')
        return 'coco'

    BAR = property(get_bar, set_bar, del_bar, 'description...')


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
        val = self.current_page * self.per_items
        return val


class Goods:
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    @property
    def price(self):
        new_price = self.original_price * self.discount
        print(new_price)
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


if __name__ == '__main__':
    # foo_obj = Foo1()
    # foo_obj.func()
    # a = foo_obj.prop
    # print(a)

    # p = Pager(1)
    # print(p.start)
    # print(p.end)

    # obj = Goods()
    # obj.price
    # obj.price = 200
    # del obj.price

    # obj = Foo2()
    # result = obj.BAR
    # print(result)

    obj = Foo3()
    obj.BAR
    obj.BAR = 'alex'
    desc = Foo3.BAR.__doc__
    print(desc)
    del obj.BAR
