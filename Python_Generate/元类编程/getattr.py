#! -*- encoding=utf-8 -*-
from datetime import date

# __getattr__   \   __getattribute__

# __getattr__ 就是在查找不到属性的时候调用

class User:
    def __init__(self, info={}):
        self.info = info
    
    def __getattr__(self, item):
        # print("not find %s" % item)
        return self.info[item]
    
    # def __getattribute__(self, item):   # 最高优先级，访问谁都进入这个函数
    #    return "alallallal"             # 把持所有属性访问的入口，能不重写就不要重写

if __name__ == "__main__":
    user = User(info={"company_name": "yuner", "name":"fzk"})
    # print(user.age)
    print(user.company_name)
    print(user.name)