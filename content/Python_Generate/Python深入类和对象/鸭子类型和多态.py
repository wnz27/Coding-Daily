#! -*- encoding=utf-8 -*-
# Python的鸭子类型（Duck Typing）和多态详解

'''
鸭子类型（Duck Typing）：

“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，
 那么这只鸟就可以被称为鸭子。”

核心概念：
1. Python不关心对象的类型，只关心对象的行为（方法）
2. 如果对象实现了所需的方法，就认为是该类型
3. 不需要显式的继承关系

Python vs Java：
- Java：需要显式声明类型和继承关系
- Python：只需要实现相同的接口（方法）

优势：
- 灵活性高
- 代码复用性好
- 更容易扩展
'''

print("=" * 50)
print("鸭子类型示例")
print("=" * 50)

class Cat(object):
    """猫类"""
    def say(self):
        print("i am a cat")

class Dog(object):
    """狗类"""
    def say(self):
        print("i am a dog")

class Duck(object):
    """鸭子类"""
    def say(self):
        print("i am duck")

# 测试单个类
animal = Cat
animal().say()

print("\n" + "=" * 50)
print("Python的鸭子类型特性")
print("=" * 50)

# Java的做法（需要显式继承）
print("""
Java的传统做法：

class Animal {
    void say() {
        System.out.println("i am a animal");
    }
}

class Cat extends Animal {
    void say() {
        System.out.println("i am a cat");
    }
}

特点：
- 必须显式继承自Animal类
- 需要声明类型
- 类型检查发生在编译时
""")

# Python的做法（鸭子类型）
animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()  # 它们都有say方法，所以都被认为是“动物类型”

print("""
鸭子类型的核心思想：
- Cat、Dog、Duck都有say()方法
- 它们可以被认为是同一种类型（都是动物）
- 不需要显式继承关系
- 只要有相同的接口即可
""")

print("\n" + "#" * 100)
print("鸭子类型的实际应用")
print("#" * 100)

# 实际例子：list的extend方法
a = ["abc1", "abc2"]
b = ["abc2", "abc"]
name_tuple = ("abc3", "abc4")
name_set = set()
name_set.add("abc5")
name_set.add("abc6")
# 测试extend方法的鸭子类型特性
print("\n示例1：extend接受list")
a_copy = a.copy()
a_copy.extend(b)
print(f"a.extend(b) = {a_copy}")  # ['abc1', 'abc2', 'abc2', 'abc']

print("\n示例2：extend接受tuple")
a_copy2 = a.copy()
a_copy2.extend(name_tuple)
print(f"a.extend(name_tuple) = {a_copy2}")  # ['abc1', 'abc2', 'abc3', 'abc4']

print("\n示例3：extend接受set")
a_copy3 = a.copy()
a_copy3.extend(name_set)
print(f"a.extend(name_set) = {a_copy3}")  # ['abc1', 'abc2', 'abc5', 'abc6']

print("""
鸭子类型的实际应用：

1. list.extend()方法：
   - extend接收一个可迭代对象（Iterable）
   - 不限于list、tuple、set等特定类型
   - 只要实现了__iter__方法即可
   - 我们自己写的类实现了可迭代方法，也可以传给这个函数

2. 鸭子类型与魔法函数的结合：
   - 如果实现了某些魔法函数，类就可以被认为是某种类型
   - 例如：实现__iter__和__next__，就是迭代器
   - 例如：实现__len__和__getitem__，就是序列
   - 例如：实现__enter__和__exit__，就是上下文管理器

3. 常见的鸭子类型示例：
   - 可迭代对象：实现__iter__方法
   - 可调用对象：实现__call__方法
   - 上下文管理器：实现__enter__和__exit__方法
   - 序列类型：实现__len__和__getitem__方法

4. 鸭子类型的优势：
   - 更加灵活和动态
   - 降低代码耦合度
   - 提高代码复用性
   - 符合Python的设计哲学

5. 鸭子类型的应用场景：
   - 多态的实现
   - 接口的替代方案
   - 插件系统
   - 测试中的Mock对象
""")
比如你实现了迭代相关的魔法函数:
__iter__
__next__
那么你自己的类就可以被称为一个可迭代对象，以此类推
'''