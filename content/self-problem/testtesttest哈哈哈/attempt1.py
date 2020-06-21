'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-19 22:19:24
@LastEditTime: 2020-03-20 00:02:35
@FilePath: /Coding-Daily/self-problem/testtesttest哈哈哈/attempt1.py
@description: type some description
'''
import selffunc
import importlib
import os, sys
l = os.listdir('/Users/fzk27/fzk27/Coding-Daily/DesignPattern/Python设计模式/相关代码/第一章')
print(l)
filename = "self_test"
sys.path.append('/Users/fzk27/fzk27/Coding-Daily/DesignPattern/Python设计模式/相关代码/第一章')
print(sys.path)
a = importlib.import_module('.',filename)

print(dir(a))
print("asdf.py".endswith(".py"), "asdf.py"[:-3])
