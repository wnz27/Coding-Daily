#! -*- encoding=utf-8 -*-
from collections import abc

# +号
a = [1,2]
c = a + [3,4]
print(c)

# += 符号， 属于就地加
a += [4,3]
print(a)

a += (5,6)
print(a)
'''
用加法就无法+（5，6）
是因为+=本质上调用的是extend方法，而extend接受可迭代对象
extend方法没有返回值，他是直接修改本身
而append是增加，比如append（[4,5]）,那么他会原来的加上一个数组而不是两个值
'''