#! -*- encoding=utf-8 -*-
# Python 3.3+ yield from 语法详解 - 委托生成器的强大工具

'''
yield from 语法详解：

1. 基本作用：
   - Python 3.3新增的语法
   - 用于委托另一个生成器执行
   - 简化生成器的嵌套调用

2. 三个核心角色：
   - 调用方（caller）：调用委托生成器的代码
   - 委托生成器（delegating generator）：包含yield from的生成器
   - 子生成器（subgenerator）：yield from后面的生成器

3. yield from 的核心功能：
   - 在调用方与子生成器之间建立双向通道
   - 自动处理异常和返回值
   - 简化代码，提高可读性
'''

from itertools import chain
from collections.abc import Iterable

print("=" * 50)
print("yield from 基础示例")
print("=" * 50)

# 准备测试数据
my_list = [1, 2, 3]
my_dict = {
    "fzk1": "http://projectsedu.com",
    "fzk2": "http://www.baidu.com",
}

print("""
itertools.chain 功能：
- 可以把多个可迭代对象连接起来
- 做一个for循环就能遍历所有元素
- 适合处理多个数据源
""")

print("\n使用chain连接多个可迭代对象：")
for value in chain(my_list, my_dict, range(5, 10)):
    print(f"  {value}")

print("\n" + "=" * 50)
print("手动实现chain - 不使用yield from")
print("=" * 50)

def my_chain(*args, **kwargs):
    """手动实现chain功能 - 传统方式
    
    Args:
        *args: 多个可迭代对象
        
    Yields:
        每个可迭代对象中的元素
        
    Note:
        - 使用嵌套循环实现
        - 需要手动遍历每个元素
        - 代码相对繁琐
    """
    for my_iterable in args:
        if isinstance(my_iterable, Iterable):
            # 手动遍历每个可迭代对象的元素
            for value in my_iterable:
                yield value
        else:
            raise ValueError("need a Iterable Object")

print("\n使用my_chain（传统方式）：")
for value in my_chain(my_list, my_dict, range(5, 10)):
    print(f"  {value}")


print("\n" + "=" * 50)
print("使用yield from改写 - Python 3.3+")
print("=" * 50)

def my_chain2(*args, **kwargs):
    """使用yield from实现chain功能 - 现代方式
    
    Args:
        *args: 多个可迭代对象
        
    Yields:
        每个可迭代对象中的元素
        
    Note:
        - 使用yield from代替嵌套循环
        - 代码更简洁、更Pythonic
        - 性能也更好
    """
    for my_iterable in args:
        if isinstance(my_iterable, Iterable):
            # 使用yield from直接委托给可迭代对象
            yield from my_iterable
        else:
            raise ValueError("need a Iterable Object")

print("\n使用my_chain2（yield from方式）：")
for value in my_chain2(my_list, my_dict, range(5, 10)):
    print(f"  {value}")

print("\n" + "=" * 50)
print("yield from 的核心原理")
print("=" * 50)

print("""
yield from 的三个角色：

1. 调用方（main）：
   - 调用委托生成器的代码
   - 例：main()函数

2. 委托生成器（g1）：
   - 包含yield from语句的生成器
   - 负责委托给子生成器
   - 例：g1(gen)函数

3. 子生成器（gen）：
   - yield from后面的生成器
   - 真正执行工作的生成器
   - 例：gen对象

yield from 的关键特性：
- 在调用方与子生成器之间建立双向通道
- 自动转发send()、throw()、close()方法
- 自动处理StopIteration异常
- 自动获取子生成器的返回值

对比：
# 不使用yield from
    for value in my_iterable:
        yield value

# 使用yield from
    yield from my_iterable

优势：
- 代码更简洁
- 性能更好（避免了中间层的处理）
- 功能更强大（支持双向通信）
""")