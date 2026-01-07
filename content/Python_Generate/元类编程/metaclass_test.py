#! -*- encoding=utf-8 -*-
# Python元类（Metaclass）详解 - 类的类，创建类的机制

'''
元类是什么？

1. 基本概念：
   - 类也是一个对象
   - type是创建类的类
   - 元类就是创建类的类！

2. 关系链：
   对象 <-- class(对象) <-- type(元类)
   例如：
   user_obj <-- User类 <-- type

3. 三种创建类的方式：
   - 普通的class定义
   - 使用type()动态创建
   - 自定义metaclass创建
'''

print("=" * 50)
print("方式1：普通方法 - 在函数中定义类")
print("=" * 50)

# 普通方法 - 在函数中根据条件返回不同的类
def create_class(name):
    """根据名称动态创建不同的类
    
    Args:
        name: 类名称
        
    Returns:
        返回对应的类对象
    """
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

print("\n" + "=" * 50)
print("方式2：使用type()动态创建类")
print("=" * 50)

class BaseClass:
    """基类"""
    def answer(self):
        return "i am baseclass"

def say(self):
    """实例方法 - 将被添加到动态创建的类中"""
    return "i am user"
    # return self.name  # 可以访问实例属性

# 使用type()动态创建类
# type(name, bases, dict)
# name: 类名
# bases: 父类元组
# dict: 类的属性和方法字典
User = type("User", (BaseClass,), {"name": "fzk", "say": say})
# 注意：千万不要写say()，只写函数名say
# 因为say()是调用函数，而say是函数对象本身

print("""
type()创建类的参数说明：
1. name：字符串，类的名称
2. bases：元组，父类列表（可以继承多个父类）
3. dict：字典，类的属性和方法
   - 属性：{"name": "value"}
   - 方法：{"method_name": function_object}

优势：
- 可以在运行时动态创建类
- 适合根据配置或数据生成类
- ORM框架常用此方法
""")

print("\n" + "=" * 50)
print("方式3：自定义元类")
print("=" * 50)

print("""
什么是元类？
元类就是创建类的类！！！

关系链：
- 平常所说的对象是由class创建的
- 而class本身也是对象，是由type（元类）创建的

关系图：
对象 <-- class(对象) <-- type(元类)
""")

class MetaClass(type):
    """自定义元类 - 继承臮type
    
    元类可以控制类的创建过程
    """
    
    def __new__(cls, *args, **kwargs):
        """创建类对象时调用
        
        Args:
            cls: 当前元类
            args: 位置参数 (name, bases, dict)
            kwargs: 关键字参数
            
        Returns:
            返回创建的类对象
            
        Note:
            - __new__在__init__之前调用
            - 可以在这里修改类的定义
            - 可以添加、修改、删除类的属性和方法
        """
        # 调用父类（type）的__new__方法创建类
        return super().__new__(cls, *args, **kwargs)

class Customer(metaclass=MetaClass):
    """使用自定义元类的类
    
    通过metaclass参数指定元类
    """
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "customer" + " " + self.name

print("""
Python中类的实例化过程：

1. 寻找metaclass的顺序：
   a) 首先查找当前类是否指定了metaclass参数
   b) 如果没有，到它的父类中查找是否设置了metaclass
   c) 如果都没有，使用type作为默认元类

2. 创建类的步骤：
   a) 调用元类的__new__方法创建类对象
   b) 调用元类的__init__方法初始化类对象
   c) 返回类对象

3. 实例化对象的步骤：
   a) 调用类的__new__方法创建实例
   b) 调用类的__init__方法初始化实例
   c) 返回实例对象

元类的应用场景：
- ORM框架（如Django ORM, SQLAlchemy）
- 单例模式的实现
- 类的注册机制
- API框架中的自动路由注册
- 类的校验和约束
""")

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("测试三种创建类的方式")
    print("=" * 50)
    # 普通方法
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(my_obj)
    # print(type(my_obj))

    # type方法
    my_obj2 = User()
    print(my_obj2)
    print(my_obj2.name)
    print(my_obj2.say())
    print(my_obj2.answer())

    # metaclass方法
    my_cus = Customer(name="yuner")
    print(my_cus)
