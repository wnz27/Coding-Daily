#! -*- encoding=utf-8 -*-
from collections import *

name_list = ["asb1", "asb2"]
for name in name_list:
    print(name)

# 元组也可以遍历
name_tuple = ("asb1", "asb2")
for name in name_tuple:
    print(name)

# 只要iterable都是可以遍历的，也就是实现了__iter__和__getitem__的魔法函数都是可以的

# 如果这样做：
# name_tuple[0] = "12345" 
'''
以上会报错：
Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/Python自定义序列类/collections模块/collections_tuple.py", line 17, in <module>
    name_tuple[0] = "12345"
TypeError: 'tuple' object does not support item assignment
'''
# tuple不可变不是绝对的
name_tuple2 = ("asb1", "asb2",[1, 2])
print(name_tuple2)          # ('asb1', 'asb2', [1, 2])
name_tuple2[2].append(333)
print(name_tuple2)          # ('asb1', 'asb2', [1, 2, 333])

# 拆包
user_tuple = ("bobby", 29, 175)
name, age, height = user_tuple
print(name, age, height)
# 输出：bobby 29 175
# 所以拆包有隐含的位置信息关系
user_tuple2 = ("bobby", 29, 175, "yunnan")
name1, *other = user_tuple2
print(name, other)
# 输出：bobby [29, 175, 'yunnan']
'''
- tuple比list好的地方
        - immutable的重要性
            - 性能优化
                - 指出元素全部为immutable的tuple会作为常量在编译时确定，因此产生了如此显著的速度差异
            - 线程安全 (不可修改当然是线程安全)
            - 可以作为dict的key （可哈希的对象才能作为dict的key，immutable对象是可哈希的）
            - 拆包特性
        - 如果要拿C语言来类比，Tuple对应的是struct，而List对应的是array

'''

user_info_dict = {}
user_info_dict[user_tuple] = "fzk27"
print(user_info_dict)
# 输出：{('bobby', 29, 175): 'fzk27'}

# 用list就不能作为key：
# user_info_dict[name_list] = "lxl"
'''
输出：
Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/Python自定义序列类/collections模块/collections_tuple.py", line 58, in <module>
    user_info_dict[name_list] = "lxl"
TypeError: unhashable type: 'list'
是说list是不可哈希的。
'''

# 类使用
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
user = User(name="fzk", age=27)
print(user.name, user.age)
# 输出：fzk 27