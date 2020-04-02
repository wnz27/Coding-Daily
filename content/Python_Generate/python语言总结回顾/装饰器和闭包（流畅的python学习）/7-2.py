# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/2 10:58
__author__ = '27'

# registration.py

registry = []  # 保存被@register装饰的函数引用


def register(func):  # register的参数是一个函数
    print("running register(%s)" % func)  # 打印被装饰的函数
    registry.append(func)  # 把被装饰的函数装入registry
    return func  # 返回函数，必须返回函数，这里返回的函数与通过参数传入的一样。


@register  # f1、f2被@register装饰
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


def f3():  # f3没有被装饰
    print("running f3()")


def main():  # main显示registry，然后调用f1()、f2()、f3()
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()


print(registry)
if __name__ == '__main__':  # 只有把本py文件当做脚本运行时才调用main()
    main()
