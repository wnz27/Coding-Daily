# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/2 19:05
__author__ = '27'

def f1(a):
    print(a)
    print(b)

# f1(3)

# def f1(a):
#     print(a)
#     print(b)
# b = 6
# f1(3)

# b = 6
def f2(a):
    print(a)
    print(b)
    b = 9
# f2(3)

# b = 6
# def f3(a):
#     global b
#     print(a)
#     print(b)
#     b = 9
# f3(3)
# print(b)
# f3(3)
# b = 30
# print(b)

from dis import dis
print(dis(f1))
print("*"*80)
print(dis(f2))
