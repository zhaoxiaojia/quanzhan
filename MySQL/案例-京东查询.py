#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 9:08
# @Author  : Coco
# @Site    : SH #5-389
# @File    : 案例-京东查询.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

from pymysql import connect


class JD:
    def __init__(self):
        # 创建Connection连接
        self.conn = connect(host='localhost', port=3306, user='root', password='123', database='jing_dong', charset='utf8')
        # 获得Cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭Cursor对象
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        '''
        显示所有的商品
        :return:
        '''
        sql = 'select * from goods'
        self.execute_sql(sql)

    def show_cates(self):
        '''
        显示所有的商品类型
        :return:
        '''
        sql = 'select name from goods_cates'
        self.execute_sql(sql)

    def show_brands(self):
        '''
        显示所有的品牌对象
        :return:
        '''
        sql = 'select name from goods_brands'
        self.execute_sql(sql)

    @staticmethod
    def print_name():
        print()
        print('-----京东-----')
        print('1:所有的商品')
        print('1:所有的商品分类')
        print('1:所有的商品品牌分类')
        return input('>: 请输入功能对应的序号 \n')

    def run(self):
        while True:
            num = self.print_name()
            if num == '1':
                # 查询所有商品
                self.show_all_items()
            elif num == '2':
                # 查询分类
                self.show_cates()
            elif num == '3':
                # 查询品牌分类
                self.show_brands()
            elif num == 'q' or num == 'quit':
                print('退出查询')
                break
            else:
                print('输入有误，请重新输入')


if __name__ == '__main__':
    # 1. 创建一个京东商城对象
    jd = JD()
    # 2. 调用这个对象的run方法，让其运行
    jd.run()
