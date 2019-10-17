#! -*- encoding=utf-8 -*-

class A:
    aa = 1                          # 类变量
    def __init__(self, x, y):
        self.x = x                  # 实例变量
        self.y = y                  # 实例变量

a = A(2,5)
print(a.x, a.y, a.aa)       # 输出： 2 5 1   ; a.aa可以向上查找到类里，在对象里查找不到的时候就会自动去类里查找。
print(A.aa)                 # 输出： 1
'''
print(A.x)                  
输出： Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/class_var.py", line 10, in <module>
    print(A.x)                  
AttributeError: type object 'A' has no attribute 'x'
'''
A.aa = 11
a.aa = 100
print(a.aa)
print(A.aa)
'''
输出：
100
11
解释：我更改完类的，再改了这个类的某个实例的aa，可以想象类是模板，
类的每个实例创建之后都会有所有与类相同的空间和模块，实例的aa也是根据类开辟出来的，
所以在我实例更改aa之后，也就是我这个实例已经有aa值了，它不会再向上去找类里aa的值。
'''
b = A(3,6)
print(b.aa)
'''
输出：11
解释：因为类A中的aa被改为11了，那么之后用类生成的实例的aa也会是11
'''
