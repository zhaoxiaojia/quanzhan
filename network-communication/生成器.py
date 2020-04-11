#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/11 7:41
# @Author  :Coco
# @FileName: 生成器.py

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


def create_num(all_num):
    # print('---1---')
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print('---2---')
        ret = yield a
        print('---ret---',ret)
        # print('---3---')
        a, b = b, a + b
        current_num += 1
        # print('---4---')
    return  'coco'

obj2 = create_num(50)

# while True:
#     try:
#         ret = next(obj2)
#         print(ret)
#     except Exception as ret:
#         print(ret.value)
#         break

print(next(obj2))

print(obj2.send('coco'))
print(next(obj2))