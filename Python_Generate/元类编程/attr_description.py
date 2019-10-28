#! -*- encoding=utf-8 -*-
from datetime import date, datetime
import numbers

class IntField:
    # 数据属性描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value")
        self.value = value

    def __delete__(self, instance):
        pass

class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        pass

class User:
    age = IntField()
    # age = NonDataIntField()

'''
如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
首先调用__getattribute__。如果类定义了__getattr__方法，
那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，
而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。
user = User(), 那么user.age 顺序如下：

（1）如果“age”是出现在User或其基类的__dict__中， 且age是data descriptor(数据描述符)， 那么调用其__get__方法, 否则

（2）如果“age”出现在user的__dict__中， 那么直接返回 obj.__dict__[‘age’]， 否则
__dict__是实例的属性，设置之后影响不了数据描述符属性的value
（3）如果“age”出现在User或其基类的__dict__中

（3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则

（3.2）返回 __dict__[‘age’]

（4）如果User有__getattr__方法，调用__getattr__方法，否则

（5）抛出AttributeError

'''

# class User:
#     def __init__(self, name, birthday):
#         self.name = name
#         self.birthday = birthday
#         self._age = 0
    
#     # def get_age(self):
#     #     return datetime.now().year - self.birthday.year

#     @property
#     def age(self):
#         return datetime.now().year - self.birthday.year

#     @age.setter
#     def age(self, value):
#         self._age = value

if __name__ == "__main__":
    user = User()
    user.age = 30
    print(user.__dict__)        # 这时候__dict__还是空的
    print(user.age)
    #user.age = "abc"
    print(getattr(user, 'age'))
    '''
    Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/元类编程/attr_description.py", line 41, in <module>
    user.age = "abc"
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/元类编程/attr_description.py", line 11, in __set__
    raise ValueError("int value need")
ValueError: int value need
    '''
    #user.age = -1
    '''
    Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/元类编程/attr_description.py", line 52, in <module>
    user.age = -1
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/元类编程/attr_description.py", line 13, in __set__
    raise ValueError("positive value")
ValueError: positive value
    '''
    print(user.age)
    # user = User("fzk", date(year=1992, month=1, day=1))
    # # print(user.get_age())
    # print(user.age)
    # user.age = 40
    # print(user.age)
    # print(user._age)
