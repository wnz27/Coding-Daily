#! -*- encoding=utf-8 -*-

from threading import Thread
class MyTread(Thread):
    def __init__(self, name, user):
        self.user = user
        # self.name = name #父类里有name的属性可以直接利用super函数来初始化这个name
        super().__init__(name=name)
        # 所以下面问题一的答案明显了，就是方便，和代码复用
    
# 1、既然我们重写了B的构造函数， 为什么还要去调用super？
# 2、super的执行顺序到底是什么样的？

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        # super(B,self).__init__() # python2中的做法
        # python3中
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D")
        super().__init__()

if __name__ == "__main__":
    b = B()  # 打印：B   A
    print("#" * 100)
    print(D.__mro__)
    print("#" * 100)
    d = D()
    

    '''
    问题二的解答：
    super不是完全调用父类，他是按照该类的__mro__顺序去往上调用父类
    '''