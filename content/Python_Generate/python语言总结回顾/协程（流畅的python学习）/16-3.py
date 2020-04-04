# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/2 03:45
__author__ = '27'


def averager():
    total = 0.0
    count = 0
    average = None
    while True:  # 这个无限循环表明，只要调用方不断把值发给这个协程，它就会一直接收值，然后生成结果。仅当调用方在协程上调用 .close() 方法，或者没有对协程的引用而被垃圾回收程序回收时，这个协程才会终止。
        term = yield average  # 这里的 yield 表达式用于暂停执行协程，把结果发给调用方;还用于接收调用方后面发给协程的值，恢复无限循环。
        total += term
        count += 1
        average = total / count


coro_avg = averager()  # 创建协程对象
print(next(coro_avg))  # 调用 next 函数，预激协程。
print(coro_avg.send(10))  # 计算移动平均值:多次调用 .send(...) 方法，产出当前的平均值。
print(coro_avg.send(30))
print(coro_avg.send(5))
