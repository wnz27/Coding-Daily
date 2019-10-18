#! -*- encoding=utf-8 -*-
from collections import Counter

users = ["fzk1", "fzk2", "fzk3", "fzk4", "fzk5", "fzk6"]
user_counter = Counter(users)   # 这里可以传递任何可迭代对象
print(user_counter)

# 统计字符串
str_counter = Counter("aaffdddddggggeeeeeeeettt")
print(str_counter)
