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
'''
一个请求对应一个函数
'''
import re
from pymysql import connect
import urllib.parse
import logging

URL_FUNC_DICT = {}


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


# 实现伪静态url
@route(r'/index.html')
def index(ret):
    with open('./templates/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    conn = connect(host='localhost', port=3306, user='root', password='123', database='stock_db', charset='utf8')
    cs = conn.cursor()
    cs.execute("select * from info;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    tr_template = '''
        <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type='button' value='添加' id='toAdd' name='toAdd' systemidvaule="%s">
        </td>
        </tr>
    '''
    html = ''
    for info in stock_infos:
        html += tr_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[1])
    content = re.sub(r'\{%content%\}', html, content)
    return content


# 实现伪静态url
@route(r'/center.html')
def center(ret):
    with open('./templates/center.html', 'r', encoding='utf-8') as f:
        content = f.read()
    conn = connect(host='localhost', port=3306, user='root', password='123', database='stock_db', charset='utf8')
    cs = conn.cursor()
    cs.execute(
        "select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    tr_template = '''
            <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type='button' class='btn btn-default btn-xs' href='/update/%s.html'> 
                <span class='glyphicon glyphicon-star' aria-hidden='true'></span>修改</a>
            </td>
            <td>
                <input type='button' value='删除' id='toDel' name='toDel' systemidvaule='%s'>
            </td>
            </tr>
        '''
    html = ''
    for info in stock_infos:
        html += tr_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[0], info[0])
    content = re.sub(r'\{%content%\}', html, content)
    return content


@route(r"/add/(\d+)\.html")
def add_focus(ret):
    '''添加业务逻辑'''
    # 1. 获取股票代码
    stock_code = ret.group(1)
    # 2. 判断是否有这个股票代码
    conn = connect(host='localhost', port=3306, user='root', password='123', database='stock_db', charset='utf8')
    cs = conn.cursor()
    sql = '''select * from info where code=%s;'''
    cs.execute(sql, [stock_code, ])

    if not cs.fetchall():
        cs.close()
        conn.close()
        return '没有鱼丸，没有粉丝'
    # 3. 判断一下是否已经关注过
    sql = '''select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;'''
    cs.execute(sql, [stock_code, ])
    if cs.fetchone():
        cs.close()
        conn.close()
        return '已经关注过请勿重复关注'
    # 4. 添加关注
    sql = '''insert into focus (info_id) select id from info where code=%s'''
    cs.execute(sql, [stock_code, ])
    conn.commit()
    cs.close()
    conn.close()
    return "关注成功"


@route(r"/del/(\d+)\.html")
def del_focus(ret):
    '''删除业务逻辑'''
    # 1. 获取股票代码
    stock_code = ret.group(1)
    # 2. 判断是否有这个股票代码
    conn = connect(host='localhost', port=3306, user='root', password='123', database='stock_db', charset='utf8')
    cs = conn.cursor()
    sql = '''select * from info where code=%s;'''
    cs.execute(sql, [stock_code, ])

    if not cs.fetchall():
        cs.close()
        conn.close()
        return '没有鱼丸，没有粉丝'
    # 3. 判断一下是否已经关注过
    sql = '''select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;'''
    cs.execute(sql, [stock_code, ])
    if not cs.fetchone():
        cs.close()
        conn.close()
        return '未关注，无法取消'
    # 4. 添加关注
    sql = '''delete from focus where info_id = (select id from info where code=%s);'''
    cs.execute(sql, [stock_code, ])
    conn.commit()
    cs.close()
    conn.close()
    return "取消关注成功"


@route(r'/update/(\d+)\.html')
def show_update_page(ret):
    '''显示修改页面'''
    # 1. 获取股票代码
    stock_code = ret.group(1)
    # 2. 打开模板
    with open('./templates/update.html', 'r', encoding='utf-8') as f:
        content = f.read()
    # 3. 根据股票代码查询相关备注信息
    conn = connect(host='localhost', port=3306, user='root', password='123', database='stock_db', charset='utf8')
    cs = conn.cursor()
    sql = "select f.note_info from focus as f inner join info as i on i.id=f.info_id where i.code=%s"
    cs.execute(sql, [stock_code, ])
    stock_info = cs.fetchone()
    note_info = stock_info[0]  # 获取股票id
    cs.close()
    conn.close()
    content = re.sub(r'\{%note_info%\}', note_info, content)
    content = re.sub(r'\{%code%\}', stock_code, content)
    return content


@route(r'/update/(\d+)/(.*)\.html')
def save_update_page(ret):
    '''保存修改的信息'''
    stock_code = ret.group(1)
    comment = ret.group(2)
    # 转义url编码
    comment = urllib.parse.unquote(comment)
    conn = connect(host='localhost', port=3306, user='root', password='123', database='stock_db', charset='utf8')
    cs = conn.cursor()
    sql = '''update focus set note_info = %s where info_id = (select id from info where code = %s);'''
    cs.execute(sql, [comment, stock_code])
    conn.commit()
    cs.close()
    conn.close()
    return '修改成功'


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']
    # if file_name == '/index.py':
    #     return index()
    # elif file_name == '/center.py':
    #     return login()
    # else:
    #     return 'Hello World 我爱你中国'
    logging.basicConfig(level=logging.INFO,
                        filename='./log.txt',
                        filemode='a',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    logging.info("访问的是，%s" % file_name)
    try:
        for url, func in URL_FUNC_DICT.items():
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else:
            logging.warning('没有对应的函数....')
            return "请求的url(%s)没有对应的函数...." % file_name
    except Exception as e:
        return '产生了异常：\n %s' % str(e)
