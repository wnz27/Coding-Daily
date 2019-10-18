#! -*- encoding=utf-8 -*-
from class_method import Date
class User:
    def __init__(self, birthday):
        self.__birthday = birthday
    
    def get_age(self):
        # 返回年龄
        return 2019 - self.__birthday.year
    
if __name__ == '__main__':
    user = User(Date(1990,2,1))
    print(user.get_age())
    # print(user.__birthday)
    # 事实上还是可以访问的，比如这样_classname__attr:
    print(user._User__birthday)
    # 所以python底层只是做了个结构化的操作，变形而已，不是绝对安全的

