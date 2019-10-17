#! -*- encoding=utf-8 -*-

a = 1
b = "abc"
print(type(1))
print(type(int))
print(type(b))
print(type(str))

'''
输出：
<class 'int'>
<class 'type'>
<class 'str'>
<class 'type'>
type -> int -> 1
type -> str -> abc
type -> class -> obj
'''

class Student:
    pass

stu = Student()
print(type(stu))
print(type(Student))
'''
输出：
<class '__main__.Student'>
<class 'type'>
'''

c = [1,2]
print(type(c))
print(type(list))
'''
输出：
<class 'list'>
<class 'type'>
'''
'''
结论：
我们的类，比如list，int，str，是由type这个类生成的对象
而我们的平常所熟悉的对象，比如具体的[1,2]、12、abc是由我们的list、int、str类创建的对象
'''

print(Student.__bases__)
class MyStudent(Student):
    pass

print(MyStudent.__bases__)
print(type.__bases__)
'''
输出：
(<class 'object'>,)
(<class '__main__.Student'>,)
(<class 'object'>,)
'''
'''
object是最顶层基类
type也是一个类，同时也是一个对象。
'''
print(type(object))  
print(object.__bases__)
'''
输出：
<class 'type'>  #object成环了。。。。。。。
()
'''
'''
所有类都是type的实例
type继承自object
'''