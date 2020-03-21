#! -*- encoding=utf-8 -*-
from collections import Counter

users = ["fzk1", "fzk2", "fzk3", "fzk4", "fzk5", "fzk6"]
user_counter = Counter(users)   # 这里可以传递任何可迭代对象
print(user_counter)

# 统计字符串
str_counter = Counter("aaffdddddggggeeeeeeeettt")
print(str_counter)

print("*" * 80)

# 合并更新统计
str_cot = Counter("qwerty")
print(str_cot)
str_cot.update("oooooooo")
print(str_cot)

print("*" * 80)
# 还可以这样更新
str_cot1 = Counter("qwerty")
print(str_cot1)
str_cot2 = Counter("oooooooo")
str_cot1.update(str_cot2)
print(str_cot1)

# most_common方法：传入一个x，计算counter对象中出现次数最多的x个值及其频数
# top n的问题~ 堆
str_cot3 = Counter("yyyyyqyyyiiqqqqqqqqqiiiiiiiiiiiiii")
print(str_cot3.most_common(2))
