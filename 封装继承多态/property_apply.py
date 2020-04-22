#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/22 21:39
# @Author  :Coco
# @FileName: property_apply.py

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


class Money1:
    '''
    定义私有变量
    定义共有方法操作该私有变量
    '''

    def __init__(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('error: Not int ')


class Money2:
    def __init__(self):
        self.__money = 0

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('error: not int ')

    def getMoney(self):
        return self.__money

    money = property(getMoney, setMoney)



if __name__ == '__main__':
    # m = Money1(100)
    # print(m.__money)

    a = Money2()
    a.money = 100
    print(a.money)


