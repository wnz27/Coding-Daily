# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/3 01:49
__author__ = '27'

import html


def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)
