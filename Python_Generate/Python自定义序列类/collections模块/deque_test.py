#! -*- encoding=utf-8 -*-
from collections import deque

user_list =["fzk", "fzk2"]
username = user_list.pop()
print(username)
print(user_list)

user_list2 = deque(["fzk", "fzk2"])
print(user_list2)

user_list3 = deque({
    "fzk": 27,
    "fzk2": 29
})
print(user_list3)

user_list5 = deque(["fzk", 30, 190])
name_tuple = ("fzk2", 33, 200)
user_list5.append(name_tuple)
print(user_list5)
# 这样不是很好，我们的list和deque尽量保证保存相同类型的数据，这是一个好习惯

user_list2.appendleft("fzk90")
print(user_list2)

