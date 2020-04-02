# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/2 03:32
__author__ = '27'


def deco(func):
    def inner():
        print("running inner()")

    return inner  # 返回inner函数对象


@deco  # 使用deco装饰target函数
def target():
    print("running target()")


target()        # 调用被装饰的target其实会运行inner
print(target)   # 查看对象，target现在是inner的引用
