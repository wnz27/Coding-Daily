# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/3 15:21
__author__ = '27'

from functools import wraps

def coroutine(func):
    """装饰器:向前执行到第一个`yield`表达式，预激`func`"""
    @wraps(func)
    def primer(*args, **kwargs):  # 把被装饰的生成器函数替换成这里的 primer 函数;调用 primer 函数时，返回预激后的生成器。
        gen = func(*args, **kwargs)  #  调用被装饰的函数，获取生成器对象。
        next(gen)  # 预激生成器。
        return gen  # 返回生成器。
    return primer

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:  # 这个无限循环表明，只要调用方不断把值发给这个协程，它就会一直接收值，然后生成结果。仅当调用方在协程上调用 .close() 方法，或者没有对协程的引用而被垃圾回收程序回收时，这个协程才会终止。
        term = yield average  # 这里的 yield 表达式用于暂停执行协程，把结果发给调用方;还用于接收调用方后面发给协程的值，恢复无限循环。
        total += term
        count += 1
        average = total / count
coro_avg = averager() # 调用 averager() 函数创建一个生成器对象，在 coroutine 装饰器的 primer 函数中已经预激了这个生成器。
print(coro_avg.send(40))
print(coro_avg.send(50))
try:
    print(coro_avg.send("spam"))    # 发送的值不是数字，导致协程内部有异常抛出。
except Exception as e:
    print(e)
finally:
    print(coro_avg.send(60))    # 由于在协程内没有处理异常，协程会终止。如果试图重新激活协程，会抛出 StopIteration 异常。