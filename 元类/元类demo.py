#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/5/5 21:21
# @Author  :Coco
# @FileName: 元类demo.py

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


def upper_attr(class_name, class_parents, class_attr):
    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith('_'):
            new_attr[name.upper()] = value

    # 调用type来创建一个类
    return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=upper_attr):
    bar = 'bip'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
f = Foo()
print(f.BAR)
