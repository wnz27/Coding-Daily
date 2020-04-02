# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/2 20:56
__author__ = '27'


# def make_averager():
#     count = 0
#     total = 0
#     def averager(new_value):
#         count += 1
#         total += new_value
#         return total / count
#     return averager
#
# avg = make_averager()
# avg(10)

def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager

avg = make_averager()
print(avg(10))