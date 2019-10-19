#! -*- encoding=utf-8 -*-
# array的效率和性能比list高的多，数据处理或者算法常用
# deque,看deque功能详解
# array,相当于c语言的数组
import array
'''
array 和 list的一个重要的区别，array只能存放指定的数据类型，也就是一个array一种数据
但是array效率非常高，所以根据这个来进行选择list和array
'''
my_array = array.array("i")   # int
my_array.append(1)
'''
my_array.append("abc")
会报错：
Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/Python自定义序列类/array_test.py", line 12, in <module>
    my_array.append("abc")
TypeError: an integer is required (got type str)
是说只能int类型，而你传进来一个str
'''
