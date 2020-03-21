#! -*- encoding=utf-8 -*-

# pyhton3.3新加了yield from语法
from itertools import chain
from collections import Iterable
'''
可以把多个可迭代对象连接起来做一个for循环
'''
my_list = [1, 2, 3]
my_dict = {
    "fzk1": "http://projectsedu.com",
    "fzk2": "http://www.baidu.com",
}
for value in chain(my_list,my_dict,range(5,10)):
    print(value)

print("*" * 80)
# 自己模拟实现chain
def my_chain(*args, **kwargs):
    for my_iterable in args:
        if isinstance(my_iterable, Iterable):
            for value in my_iterable:
                yield value
        else:
            raise ValueError("need a Iterable Object")
# 测试
for value in my_chain(my_list,my_dict,range(5,10)):
    print(value)


print("*" * 80)

# # 小例子
# def g3(iterable):
#     yield iterable

# def g4(iterable):
#     yield from iterable

# for value in g3(range(10)):
#     print(value)
# for value in g4(range(10)):
#     print(value)

# yield from iterable来改写
def my_chain2(*args, **kwargs):
    for my_iterable in args:
        if isinstance(my_iterable, Iterable):
            yield from my_iterable
        else:
            raise ValueError("need a Iterable Object")
# 测试
for value in my_chain2(my_list,my_dict,range(5,10)):
    print(value)

print("*" * 80)

def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)
'''
1、main ：调用方
g1 ：(委托生成器)
gen ：子生成器
2、yield from会在调用方与子生成器之间建立一个双向通道
'''