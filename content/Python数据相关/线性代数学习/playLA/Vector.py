# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/3/29 23:01
__author__ = '27'

class Vector:
    def __init__(self, lst):
        self._values = lst

    def __len__(self):
        """返回向量长度（有多少个元素），即向量维度"""
        return len(self._values)

    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]

    # 系统调用
    def __repr__(self):
        return "Vector({})".format(self._values)

    # 使用者调用
    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
