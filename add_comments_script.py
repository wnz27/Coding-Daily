#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为Python_preToPractice.md文件中的Python代码块添加详细中文注释的脚本
"""

import re

# 读取文件内容
with open('/Users/f27/self_repo/Coding-Daily/content/PythonPractice/Python_preToPractice.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义需要添加注释的代码模式和对应的注释版本
replacements = []

# 1. Car类的完整定义
replacements.append({
    'old': '''```
class Car():
    '''模拟汽车的尝试'''
    def __init__(self,make,model,year):
        '''初始化汽车实例的属性'''
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car("audi","a4",2018)   # 创建 my_new_car 这个实例
print my_new_car.get_descriptive_name() # 调用 描述方法
```''',
    'new': '''```python
# 定义Car类,用于模拟汽车
class Car():
    '''模拟汽车的尝试'''
    
    # 构造函数,初始化汽车的基本属性
    def __init__(self,make,model,year):
        '''初始化汽车实例的属性'''
        self.make = make      # 制造商
        self.model = model    # 型号
        self.year = year      # 年份

    # 返回格式化的汽车描述信息
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        # 拼接年份、制造商和型号
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        # 返回首字母大写的格式
        return long_name.title()

# 创建Car类的实例
my_new_car = Car("audi","a4",2018)
# 调用方法获取并打印汽车描述
print my_new_car.get_descriptive_name()
```'''
})

# 2. 文件读取with语句
replacements.append({
    'old': '''```
with open("pi_digits.txt") as file_object:  #读取文件pi_digit.txt的操作
    contents = file_object.read()
    print(contents)
```''',
    'new': '''```python
# 使用with语句打开文件,自动管理文件的关闭
with open("pi_digits.txt") as file_object:
    # 使用read()方法读取文件的全部内容
    contents = file_object.read()
    # 打印文件内容
    print(contents)
```'''
})

# 3. try-except异常处理
replacements.append({
    'old': '''```
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't division by zero!")
```''',
    'new': '''```python
# try代码块:尝试执行可能引发异常的代码
try:
    # 尝试执行除以0的操作,这会引发ZeroDivisionError异常
    print(5/0)
# except代码块:捕获特定类型的异常并处理
except ZeroDivisionError:
    # 当捕获到ZeroDivisionError异常时,打印友好的错误提示
    print("You can't division by zero!")
```'''
})

# 4. json模块使用
replacements.append({
    'old': '''```
import json #导入json模块

numbers = [2,3,5,7,11,13]

file_name = "numbers.json"
with open(file_name,"w") as f_obj:
    json.dump(numbers,f_obj) #把数字列表写入文件对象f_obj
```''',
    'new': '''```python
# 导入json模块,用于序列化和反序列化Python对象
import json

# 创建一个数字列表
numbers = [2,3,5,7,11,13]

# 指定要保存的文件名
file_name = "numbers.json"
# 以写入模式打开文件
with open(file_name,"w") as f_obj:
    # 使用json.dump()将Python对象序列化并写入文件
    # 第一个参数是要保存的数据,第二个参数是文件对象
    json.dump(numbers,f_obj)
```'''
})

# 5. unittest测试用例
replacements.append({
    'old': '''```
import unittest
from test_prctice import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''测试test_practice.py'''
    def test_first_last_name(self):
        '''能够正确处理Janis Joplin这样的姓名吗？'''
        formatted_name = get_formatted_name("janis","joplin")
        self.assertEqual(formatted_name,"Janis Joplin")

unittest.main()
```''',
    'new': '''```python
# 导入unittest模块,Python的单元测试框架
import unittest
# 导入要测试的函数
from test_prctice import get_formatted_name

# 定义测试用例类,必须继承unittest.TestCase
class NameTestCase(unittest.TestCase):
    '''测试test_practice.py'''
    
    # 测试方法必须以test_开头
    def test_first_last_name(self):
        '''能够正确处理Janis Joplin这样的姓名吗？'''
        # 调用被测试的函数
        formatted_name = get_formatted_name("janis","joplin")
        # 使用断言方法检查结果是否符合预期
        self.assertEqual(formatted_name,"Janis Joplin")

# 运行测试
unittest.main()
```'''
})

print(f"准备进行 {len(replacements)} 处替换...")

# 执行替换
count = 0
for r in replacements:
    if r['old'] in content:
        content = content.replace(r['old'], r['new'], 1)
        count += 1
        print(f"✓ 替换成功 {count}/{len(replacements)}")
    else:
        print(f"✗ 未找到匹配内容")

# 写回文件
with open('/Users/f27/self_repo/Coding-Daily/content/PythonPractice/Python_preToPractice.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n完成! 成功替换了 {count} 处代码块")
