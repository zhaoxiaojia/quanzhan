#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2020/4/11 12:49
# @Author  :Coco
# @FileName: 图片下载器.py

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

import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(url):
    req = urllib.request.urlopen(url)
    img_content = req.read()
    with open('xxx', 'w') as f:
        f.write(img_content)


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(downloader, 'xxx'),
        gevent.spawn(downloader, 'xxx')
    ])
