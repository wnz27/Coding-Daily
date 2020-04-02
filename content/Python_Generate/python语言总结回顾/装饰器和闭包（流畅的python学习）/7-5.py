# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/2 20:06
__author__ = '27'


class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))


# 函数式实现，使用高阶函数 make_averager
def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager
avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)
