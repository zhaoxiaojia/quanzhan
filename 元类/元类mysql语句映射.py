#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 18:17
# @Author  : Coco
# @Site    : SH #5-389
# @File    : 元类mysql语句映射.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mappings = dict()
        for key, value in attrs.items():
            # 判断是否是元祖类型 是则保存
            if isinstance(value, tuple):
                print('Found mapping ：%s ==> %s' % (key, value))
                mappings[key] = value
        # 删除字典里的属性
        for key in mappings.keys():
            attrs.pop(key)
        # 重新添加属性
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(object, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        fields = list()
        args = list()
        for key, value in self.__mappings__.items():
            fields.append(value[0])
            args.append(getattr(self, key, None))

        # sql = 'insert into %s (%s) value (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        # print('SQL：' + sql)
        args_temp = list()
        for temp in args:
            if isinstance(temp, int):
                args_temp.append(temp)
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)
        sql = 'insert into %s (%s) value (%s)' % (
            self.__table__, ','.join(fields), ','.join([str(i) for i in args_temp]))
        print('SQL：' + sql)


class User(Model):
    uid = ('uid', 'int unsigned')
    name = ('username', 'varchar(30)')
    email = ('email', 'varchar(30)')
    password = ('password', 'varchar(30)')


u = User(uid=12345, name='coco', email='xxx@xx.com', password='123')
u.save()
