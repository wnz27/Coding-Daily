# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/1 18:23
__author__ = '27'


def simple_coroutine():  # 协程使用生成器函数定义:定义体中有 yield 关键字。
    print('-> coroutine started')
    x = yield  # 如果协程只从客户那里接收数据，那么产出的值是None，这个值是隐式指定的，因为yield关键字右边没有表达式
    print('-> coroutine received:', x)


# my_coro = simple_coroutine()  # 调用函数得到生成器对象
# print(my_coro)  # <generator object simple_coroutine at 0x1012956d0>
# next(my_coro)  # 因为生成器还没启动，没在yield处暂停，所以一开始无法发送数据。
# my_coro.send(42)  # 调用这个方法后，协程定义体中的yield会计算出42，现在，协程会恢复，一直运行到下一个yield表达式，或者终止。
# 然后控制权流动到协程定义体的末尾，导致协程生成器向往常一样抛出StopIteration异常。


def simple_coro2(a):
    print("-> Started: a =", a)
    b = yield a
    print("-> Received: b =", b)
    c = yield a + b
    print("-> Received: c =", c)


my_coro2 = simple_coro2(14)
from inspect import getgeneratorstate
print(getgeneratorstate(my_coro2))      # 处于GEN_CREATED状态，协程未启动
print(next(my_coro2))     # 预激协程，执行到第一个yield表达式，打印 -> Started: a = 14，然后产出a值，并且暂停等待为b赋值
print(getgeneratorstate(my_coro2))  # 处于GEN_SUSPENDED状态，即协程在yield表达式处暂停
print(my_coro2.send(28))        # 把数字28发给协程，计算yield表达式，得到28，然后赋值给b，打印 -> Received: b = 28消息，产出a+b的值42，然后协程暂停，等待为c赋值
try:
    print(my_coro2.send(99))    # 把数字99发给协程，计算yield表达式，得到99，然后赋值给c，打印 -> Received: c = 99消息，然后协程终止，产生StopIteration异常被texcept捕捉
except StopIteration as e:
    print("StopIteration!!!")   # 捕捉到StopIteration异常。
finally:
    print(getgeneratorstate(my_coro2))  # 可以清晰的看到抛出StopIteration后协程处于GEN_CLOSED状态（即协程执行结束）


