
'''
class A:
    name = "A"
    # def __init__(self):
    #     self.name = "obj"
# c3算法
a = A()
print(a.name)
'''
'''
# 新式类
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B,C):
    pass

print(A.__mro__)
'''
# 输出： (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
'''
我们可以发现最后还是object，所以就是D不写（object）也会自动继承object
'''

class D:
    pass

class E:
    pass

class B(D):
    pass

class C(E):
    pass

class A(B,C):
    pass

print(A.__mro__)
# 输出：(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)