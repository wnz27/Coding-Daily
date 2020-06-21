# -*- coding: utf-8 -*-
# @UpdateTime    : 2020/6/21 17:13
# @File    : vector_test.py
import unittest
from content.Python数据相关.线性代数学习.playLA.Vector import Vector
import os


class TestVector(unittest.TestCase):
    def testVectorAssociativeLaw(self):
        """
        测试向量结合律
        """
        vec = Vector([2, 5])
        vec2 = Vector([8, 1])
        k = 2
        res1 = k * vec2 + k * vec
        res2 = k * (vec + vec2)
        self.assertEquals(res1[0], res2[0])
        self.assertEquals(res1[1], res2[1])

