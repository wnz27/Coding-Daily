# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/2 21:43
__author__ = '27'

import time


def clock(func):
    def clocked(*args):  # 定义内部函数clocked，它接收任意个定位参数。
        t0 = time.perf_counter()
        result = func(*args)  # 这行代码可用，是因为 clocked 的闭包中包含自由变量 func。
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked  # 返回内部函数，取代被装饰的函数。下面演示了 clock 装饰器 的用法。

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__=='__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))

print(factorial.__name__)



