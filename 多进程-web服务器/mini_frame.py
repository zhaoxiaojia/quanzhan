#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/30 6:22
# @Author  :Coco
# @FileName: mini_frame.py

# @Software: PyCharm
"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓ ┏┓
            ┏┛┻━┛┻━┓
            ┃   ☃  ┃
            ┃ ┳┛ ┗┳ ┃
            ┃   ┻   ┃
            ┗━┓   ┏━┛
               ┃     ┗━━┓
               ┃        ┣┓
               ┃　      ┏┛
               ┗┓┓━━┳┓━┛
                 ┃┫  ┃┫
                 ┗┛  ┗┛
"""


def index():
    # Todo
    return '这是主页'


def login():
    # Todo
    return '这是登陆页'


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']
    if file_name == '/index.py':
        return index()
    elif file_name == '/login.py':
        return login()
    return 'Hello World 我爱你中国'
