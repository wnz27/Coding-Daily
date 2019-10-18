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

user_list4 = user_list2.copy()
print(id(user_list2), id(user_list4))
user_list2[1] = "fzk1000000"
print(user_list2, user_list4)

user_list6 = deque(["fzk",["fzk100", "fzk900"] , "fzk2"])
user_list7 = user_list6.copy()
user_list7[1].append("abcdefg")
print(user_list6, user_list7) 
# 以上说明只拷贝了元素，属于浅拷贝，第二个例子就是只拷贝了list这个元素

# python本身有深拷贝
import copy as cp
user_list8 = deque(["fzk",["fzk100", "fzk900"] , "fzk2"])
user_list9 = cp.deepcopy(user_list8)
user_list9[1].append("abcdefg")
print(user_list8, user_list9) 
# 看输出可以看到一个增加另一个没有增加


user_list99 = deque(["fzk", "fzk2"])
user_list98 = deque(["fzk111", "fzk555"])
user_list99.extend(user_list98)
# print(user_list99.extend(user_list98))   
# # 这是错误的，这个方法不返回值，他是在调用者上扩容，也就是返回user_list99就行了
print(user_list99)

# 在指定位置上插入元素
user_list98.insert(0,"nimahai")
print(user_list98)

# reverse 反转,也是在deque本身上操作
user_list98.reverse()
print(user_list98)

# deque的应用场景
'''
双端队列
deque：GIL是线程安全的， list不是线程安全的
'''
