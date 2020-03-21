#! -*- encoding=utf-8 -*-
# python对象的自省机制
# 自省是通过一定的机制查询到对象的内部结构
from class_method import Date

class Person:
    '''
    人头哥
    '''
    name = "user"
    
class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__ == '__main__':
   user = Student("慕课网")

   # 通过__dict__查询属性
   print(user.__dict__)
   print(Person.__dict__)
   print(user.name)
   # __dict__可以直接赋值
   user.__dict__["school_addr"] = "冥王星"
   print(user.school_addr)

   print('#'*80)
   # dir 这个函数可以列出对象的所有属性
   print(dir(user))

   a = [1,2]
   # print(a.__dict__)   # 会报错的
   # 但我们用dir就可以
   print(dir(a))