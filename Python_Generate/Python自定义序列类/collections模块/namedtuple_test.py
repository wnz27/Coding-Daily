#! -*- encoding=utf-8 -*-
from collections import namedtuple

User = namedtuple("User", ["name", "age", "height", "edu"])
user = User(name="fzk", age=27, height=166, edu="lll")
print(user)
print(user.age, user.name, user.edu)
# 其实相当于以简洁的方式帮我们创建了user类
# nametuple是tuple的子类

user_tuple = ("fzk", 27, 199)
user1 = User(*user_tuple, "master")
print(user1)
print(user1.age, user1.name, user1.edu)
# 可以看到tuple不够的时候我们可以生成变量时候添加属性

# 函数参数
def ask(*args, **kwargs):
    pass
'''
不指定变量名称的话是存在args里，是元组存储，比如这样ask("27",27)
指定的话是存在kwargs里，是字典存储，比如这样ask(name="27", age=27)
'''
# 所以引申到可以用**kwargs来解包
user_dict = {
    "name": "27",
    "age": 27,
    "height": 170
}
user2 = User(**user_dict, edu="doctor")   
# 注意用**后那后面添加的参数也要加关键字
print(user2)
print(user2.age, user2.name, user2.edu)

# _make方法，把可迭代对象变成namedtuple
'''
# 使用namedtuple的_make方法传递进一个可迭代对象就可以不用区分*还是**
# 但是这个方法不好的地方时必须接受跟定义一样数量属性的可迭代对象
'''
user_tuple_new = ("fzk", 27, 199,"qwertpasncvan")
user10 = User._make(user_tuple_new)
print(user10)
user_list = ["fzk", 33, 3456,"1342dsf43rf234"]
user20 = User._make(user_list)
print(user20)
user_dict1 = {
    "name": "27",
    "age": 44,
    "height": 888,
    "edu": "2t3t5t7t"
}
user30 = User._make(user_dict1)
print(user30)
'''
返回的是：
User(name='name', age='age', height='height', edu='edu')
在dict对象迭代的时候返回的是key
所以想要拿到值要做如下的修改：
'''
user40 = User._make(user_dict1.values())
print(user40)
'''
这时候输出的是：
User(name='27', age=44, height=888, edu='2t3t5t7t')
'''

# _asdict方法： 可以把tuple变成dict
user40_dict = user40._asdict()
print(user40_dict)
#输出是：OrderedDict([('name', '27'), ('age', 44), ('height', 888), ('edu', '2t3t5t7t')])

# 拆包
name1, age1, *other1 = user40
print(name1, age1, other1)
