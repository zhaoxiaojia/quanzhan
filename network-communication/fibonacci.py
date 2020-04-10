#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 8:51
# @Author  : Coco
# @Site    : SH #5-389
# @File    : fibonacci.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm


class Fibonacci:
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            self.current_num += 1
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            return ret
        else:
            raise StopIteration

fibo = Fibonacci(10)
for num in fibo:
    print(num)