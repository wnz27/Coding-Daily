#! -*- encoding=utf-8 -*-
from collections import ChainMap

user_dict1 = {"a": "fzk1", "b": "fzk2"}
user_dict2 = {"c": "fzk2", "d": "fzk3"}
new_dict = ChainMap(user_dict1, user_dict2)
for key, value in new_dict.items():
    print(key, value)

user_dict3 = {"a": "fzk1", "b": "fzk2"}
user_dict4 = {"b": "fzk7", "d": "fzk3"}
new_dict2 = ChainMap(user_dict3, user_dict4)
print(new_dict2)
for key, value in new_dict2.items():
    print(key, value) 
'''
输出：
d fzk3
a fzk1
b fzk2
可以看到，如果有重复的key，当我们for遍历的时候遇见第一个输出之后，就不会找第二个了
'''

print("*" * 80)

user_dict5 = {"a": "fzk1", "b": "fzk2"}
user_dict6 = {"c": "fzk7", "d": "fzk3"}
new_dict3 = ChainMap(user_dict5, user_dict6)
print(new_dict3)
print("*" * 80)
print(new_dict3.maps)
print("*" * 80)
print(new_dict3.new_child())
print("*" * 80)
new_chain = new_dict3.new_child({"aa":"aa", "bb":"bb"})
print(new_chain)
print("*" * 80)
for key, value in new_dict3.items():
    print(key, value)
print("*" * 80) 
for key, value in new_chain.items():
    print(key, value)

'''
由输出可以看出
maps这个方法可以以列表的形式把数据展示出来
new_child()这个方法并不改变调用它的chain_map，而是返回一个新的ChainMap
''' 