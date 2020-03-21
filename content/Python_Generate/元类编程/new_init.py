#! -*- encoding=utf-8 -*-
class User:
    def __new__(cls, *args, **kwargs):  # new的过程时还没有生成对象，是对类的操作，可以自定义类的生成的逻辑
        print(" in  new  ")
        return super().__new__(cls)
    def __init__(self,name):                 # 这时候已经生成对象，对对象的操作
        print("  in init  ")
        self.name = name


# new 是用来控制对象的生成过程，在对象生成之前
# init 是用来完善对象的
# 如果new方法不返回对象，则不会调用init函数
if __name__ == "__main__":
    user = User(name="fzk")     # 属性会以dict进入**kwargs
    # user1 = User("fzk1")        # 属性会以tuple进入*args
