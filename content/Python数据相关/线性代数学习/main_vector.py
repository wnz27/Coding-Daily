'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-29 23:12:42
@LastEditTime: 2020-06-21 11:39:17
@FilePath: /Coding-Daily/content/Python数据相关/线性代数学习/main_vector.py
@description: type some description
'''
# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/3/29 23:12
from .playLA.Vector import Vector

__author__ = '27'

if __name__ == "__main__":
    vec = Vector([5, 2])
    print(vec)
    print(len(vec))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))

    # 加减尝试
    vec2 = Vector([3,1])
    print(vec2)
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    # 乘法尝试
    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    # 正负尝试
    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))
