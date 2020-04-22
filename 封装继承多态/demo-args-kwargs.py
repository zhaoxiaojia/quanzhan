#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 8:57
# @Author  : Coco
# @Site    : SH #5-389
# @File    : demo-args-kwargs.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

def test2(a, b, *args, **kwargs):
    print('-----------')
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test1(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    test2(a, b, *args, **kwargs)  # 相当于test2(11,22,33,44,55,66,name='coco',age=25)
    test2(a, b, args, kwargs)  # 相当于test2(11,22,(33,44,55,66),{name='coco',age=25})


if __name__ == '__main__':
    test1(11, 22, 33, 44, 55, 66, name='coco', age='25')
