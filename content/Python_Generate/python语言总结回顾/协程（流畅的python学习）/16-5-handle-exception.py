# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/3 15:36
__author__ = '27'


class DemoException(Exception):
    """为这次演示定义的异常类型。"""
    pass


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:   # ➊
            print('*** DemoException handled. Continuing...')
        else:  # ➋
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')  # ➌

"""
❶ 特别处理 DemoException 异常。
❷ 如果没有异常，那么显示接收到的值。
❸ 这一行永远不会执行。
"""

