#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 9:27
# @Author  : Coco
# @Site    : SH #5-389
# @File    : 多继承.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm


class Parent:
    def __init__(self, name):
        print('parent.__init__ start')
        self.name = name
        print('parent.__init__ end')


class Son(Parent):
    def __init__(self, name, age):
        print('son.__init__ start')
        self.age = age
        super(Son, self).__init__(name)
        print('son.__init__ end')


class Grandson(Son):
    def __init__(self, name, age, gender):
        print('grandson.__init__ start')
        self.gender = gender
        super(Grandson, self).__init__(name,age)
        print('grandson.__init__ end')


grandson = Grandson('coco',23,'男')
print(Grandson.__mro__)
