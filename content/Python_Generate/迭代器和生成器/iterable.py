#! -*- encoding=utf-8 -*-

'''
什么是迭代协议?

迭代器是什么？
迭代器是访问集合内元素的一种方式， 一般用来遍历数据
迭代器和以下表的访问方式不一样，迭代器是不能返回的，
迭代器提供了一种惰性访问数据的方式(访问数据的时候才去计算或者获取数据)
list下标访问方式背后的原理是__getitem__
凡是可迭代类型，背后都是实现了迭代协议的，我们可以对它for循环

Iterable，可迭代对象。
Iterator，迭代器。 
'''
from collections.abc import Iterable, Iterator
a = [1,2]
iter_rator = iter(a)
iter_rator2 = iter(a)
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(isinstance(iter_rator, Iterator))
print(id(iter_rator), id(iter_rator2))