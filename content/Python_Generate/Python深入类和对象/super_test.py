#! -*- encoding=utf-8 -*-
# Python中super()函数的深入理解和使用

'''
super()函数详解：

1. super()的作用：
   - 调用父类（超类）的方法
   - 按照MRO（Method Resolution Order）顺序查找
   - 常用于__init__方法中初始化父类

2. 为什么使用super()：
   - 代码复用：避免重复编写父类的初始化代码
   - 维护方便：修改继承关系时不需要修改子类代码
   - 支持多继承：正确处理复杂的多继承情况

3. Python 2 vs Python 3：
   - Python 2: super(ClassName, self).__init__()
   - Python 3: super().__init__()  # 更简洁
'''

from threading import Thread

class MyThread(Thread):
    """自定义线程类 - 演示super()的使用"""
    
    def __init__(self, name, user):
        """初始化自定义线程
        
        Args:
            name: 线程名称
            user: 自定义的用户属性
        """
        self.user = user
        # 不需要 self.name = name
        # 因为Thread类已经有name属性，直接用super()初始化即可
        super().__init__(name=name)
        # 这就是为什么要用super()的原因：方便且代码复用

# ==================== 深入理解super()的执行顺序 ====================
print("=" * 50)
print("super()执行顺序演示")
print("=" * 50)

class A:
    """顶层父类"""
    def __init__(self):
        print("A.__init__()")

class B(A):
    """继承自A"""
    def __init__(self):
        print("B.__init__()")
        # Python 2的写法：super(B, self).__init__()
        # Python 3的写法（更简洁）
        super().__init__()

class C(A):
    """也继承自A"""
    def __init__(self):
        print("C.__init__()")
        super().__init__()

class D(B, C):
    """多继承：同时继承自B和C"""
    def __init__(self):
        print("D.__init__()")
        super().__init__()

if __name__ == "__main__":
    print("\n示例1：单继承")
    print("-" * 30)
    b = B()
    # 输出：B.__init__()  A.__init__()
    
    print("\n" + "#" * 100)
    print("示例2：多继承的MRO顺序")
    print("-" * 30)
    print(f"D的MRO顺序: {D.__mro__}")
    # 输出：(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    
    print("\n示例3：多继承的初始化顺序")
    print("-" * 30)
    d = D()
    # 输出：
    # D.__init__()
    # B.__init__()
    # C.__init__()
    # A.__init__()
    print("\n" + "=" * 50)
    print("super()的核心原理总结")
    print("=" * 50)
    print("""
    重要结论：
    
    1. super()不是直接调用父类：
       - super()是按照该类的__mro__属性的顺序往上查找
       - MRO (Method Resolution Order) 是方法解析顺序
    
    2. MRO的特点：
       - 使用C3线性化算法计算
       - 保证子类在父类之前
       - 保证多继承时的顺序一致性
       - 父类只会被调用一次
    
    3. 多继承中的super()：
       - D(B, C)的MRO：D -> B -> C -> A -> object
       - D中调用super()会找到B
       - B中调用super()会找到C（不是A！）
       - C中调用super()才会找到A
       - 这确保了A只被初始化一次
    
    4. 最佳实践：
       - 在多继承中总是使用super()
       - 不要直接调用父类名
       - 确保所有类都调用super()
       - 这样才能正确处理复杂的继承关系
    
    5. 常见误区：
       - 误：super()总是调用直接父类
       - 正：super()按MRO顺序调用下一个类
       - 在多继承中这个区别非常重要！
    """)