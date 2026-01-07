#! -*- encoding=utf-8 -*-
# Python中的type、class和object关系详解

# 创建基本数据类型的实例
a = 1
b = "abc"

# 查看实例和类的类型
print("=" * 50)
print("1. 基本类型的type关系")
print(f"type(1) = {type(1)}")        # <class 'int'>
print(f"type(int) = {type(int)}")    # <class 'type'>
print(f"type('abc') = {type(b)}")    # <class 'str'>
print(f"type(str) = {type(str)}")    # <class 'type'>

'''
Python类型系统的层次关系：

type -> int -> 1
type -> str -> "abc"
type -> class -> obj

重要概念：
1. 在Python中，一切皆为对象，包括类本身
2. 类（如int、str、list）是type类的实例
3. 实例（如具体的数字、字符串）是对应类的实例
4. type本身也是一个类，用于创建其他类
'''

# 自定义类的例子
print("\n" + "=" * 50)
print("2. 自定义类的type关系")

class Student:
    """Student类 - 用于演示type关系"""
    pass

stu = Student()
print(f"type(stu) = {type(stu)}")        # <class '__main__.Student'>
print(f"type(Student) = {type(Student)}")  # <class 'type'>
'''
输出：
<class '__main__.Student'>
<class 'type'>
'''

c = [1,2]
print(type(c))
print(type(list))
'''
结论1：
- 我们定义的类（如list、int、str、Student）都是type类生成的对象
- 我们平常所熟悉的对象（如[1,2]、12、"abc"、stu）是由对应类创建的实例
'''

# 类的继承关系 - __bases__属性
print("\n" + "=" * 50)
print("3. 类的继承关系(__bases__)")

print(f"Student.__bases__ = {Student.__bases__}")  # (<class 'object'>,)

class MyStudent(Student):
    """MyStudent类 - 继承自Student"""
    pass

print(f"MyStudent.__bases__ = {MyStudent.__bases__}")  # (<class '__main__.Student'>,)
print(f"type.__bases__ = {type.__bases__}")          # (<class 'object'>,)
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
==================================================================================
Python类型系统的核心总结：
==================================================================================

1. 类型关系（type）：
   - 所有类都是type的实例（包括object和type自身）
   - type(any_class) 返回 <class 'type'>
   - type是元类（metaclass），用于创建类

2. 继承关系（__bases__）：
   - type继承自object
   - 所有类默认继承自object（如果没有显式指定父类）
   - object没有父类（object.__bases__ == ()）

3. 循环关系：
   - type是object的实例：type(object) == type
   - type继承自object：type.__bases__ == (object,)
   - 这形成了Python类型系统的循环关系

4. 实际应用：
   - 自定义类默认继承自object
   - 自定义类由type创建
   - 可以通过自定义元类来控制类的创建过程

5. 图示关系：
   ```
   object <----继承---- type
     ^实例              |
     |                   |实例
     |继承               |
   自定义类 <---------+
     |
     |实例
     v
   自定义实例
   ```

这就是Python中“一切皆对象”的核心原理！
'''