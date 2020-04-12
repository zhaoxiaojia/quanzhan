#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 11:17
# @Author  : Coco
# @Site    : SH #5-389
# @File    : 匹配163邮箱.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

'''
re 中多种 方法的使用技巧
'''
import re


def match_email():
    str = 'ocmo@qq.com'
    result = re.match(r'[a-zA-Z0-9_]{4,20}@(163|126|qq)\.com$', str)
    if result:
        print(result.group())
    else:
        print('匹配失败')


def match_html_label():
    '''
    使用()获取匹配到的字符串 使用 \1 使用第一个()中匹配的字符串用在正则表达式中
    也可以使用(?P<xxx>) 获取匹配到字符串 使用(?P=xxx) 使用匹配到的字符串用于正则表达式中
    :return:
    '''
    html_str = '<body><h1>coco</body></h1>'
    # result = re.match(r'<(?P<body>\w*)><(?P<h1>\w*)>(.*)</(?P=body)></(?P=h1)>', html_str).group(3)
    result = re.match(r'<(\w*)><(\w*)>(.*)</\1></\2>', html_str).group(3)
    print(result)


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


def sub_function():
    # sub 中使用方法处理匹配到的字符串
    result = re.sub(r'\d+', add, 'python = 998')
    print(result)


def split_function():
    result = re.split(r"xiao", 'info:xiaozhang 33 shandong ')
    print(result)


if __name__ == '__main__':
    # match_html_label()
    split_function()