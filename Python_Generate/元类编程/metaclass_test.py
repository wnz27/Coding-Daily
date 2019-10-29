#! -*- encoding=utf-8 -*-
# 类也是一个对象， type是创建类的类

# 普通方法
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

class BaseClass:
    def answer(self):
        return "i am baseclass"

def say(self):
    return "i am user"
    # return self.name

# 通过type动态创建类
User = type("User", (BaseClass,), {"name":"fzk","say":say})       # 千万不要写say()，只写函数名称say

'''
什么是元类：
元类是创建类的类！！！！！！！
平常所说的对象是由我们的class创建的
对象<--class(对象)<--type(元类)
'''

class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

class Customer(metaclass=MetaClass):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "customer" + " " + self.name

'''
Python 中类的实例化过程，会首先寻找metaclass,
通过metaclass去创建User类，如果自己没有metaclass，
那会去它的基类里看有没有设置metaclass，有的话还是会使用metaclass去创建User类，
都没有的话，会用type去创建类对象，实例
'''

if __name__ == "__main__":
    # 普通方法
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(my_obj)
    # print(type(my_obj))

    # type方法
    my_obj2 = User()
    print(my_obj2)
    print(my_obj2.name)
    print(my_obj2.say())
    print(my_obj2.answer())

    # metaclass方法
    my_cus = Customer(name="yuner")
    print(my_cus)
