#! -*- encoding=utf-8 -*-
from collections import OrderedDict

user_dict = OrderedDict()
user_dict["b"] = "fzk2"
user_dict["a"] = "fzk1"
user_dict["c"] = "fzk3"
print(user_dict) 
'''
输出：
OrderedDict([('b', 'fzk2'), ('a', 'fzk1'), ('c', 'fzk3')])
说明这个有序性不是指怎样排序，而是指添加的顺序
python3里用dict生成实例添加的话默认也是有顺序的
python2里用dict是无序的，orderedDict是有序的
'''
print(user_dict.popitem())
print(user_dict)
print(user_dict.move_to_end("b"))  # 输出None 说明这个方法没有返回值
print(user_dict)