#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 11:17
# @Author  : Coco
# @Site    : SH #5-389
# @File    : 匹配163邮箱.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm


import re
if __name__ == '__main__':

    str = 'ocmo@163.com'
    result = re.match(r'[a-zA-Z0-9_]{4,20}@163\.com$', str)
    if result:
        print(result.group())
    else:
        print('匹配失败')
