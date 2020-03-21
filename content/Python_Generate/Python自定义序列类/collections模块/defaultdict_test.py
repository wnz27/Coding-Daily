#! -*- encoding=utf-8 -*-
from collections import defaultdict
'''
这个类是C语言写的一个类，所以性能是非常高的，这与namedtuple是不一样的
'''
# 数组数据计数
user_dict = {}
users = ["fzk1","fzk2","fzk3","fzk1","fzk2","fzk2"]
for user in users:
    user_dict.setdefault(user,0)
    user_dict[user] += 1
print(user_dict)
# 也就是说setdefault会自判断键是否存在

default_dict = defaultdict(int)
users1 = ["fzk1","fzk2","fzk3","fzk1","fzk2","fzk2"]
for user in users1:
    default_dict[user] +=1
print(default_dict)
print("*" * 80)

def gen_default():
    return {
        "name":"",
        "nums":0
    }
default_dict1 = defaultdict(gen_default)
default_dict1["group1"]
print(default_dict1)
