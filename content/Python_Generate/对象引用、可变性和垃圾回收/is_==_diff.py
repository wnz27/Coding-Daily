#! -*- encoding=utf-8 -*-
# Python中 is 和 == 的区别详解

'''
Python中的两种比较方式：

1. is 操作符：
   - 比较两个对象的身份（内存地址）
   - 相当于比较 id(a) == id(b)
   - 判断是否是同一个对象

2. == 操作符：
   - 比较两个对象的值是否相等
   - 调用对象的 __eq__ 魔法函数
   - 只判断值是否相同，不关心是否是同一个对象
'''

print("=" * 50)
print("示例1：引用同一个对象")
print("=" * 50)

c = [1, 2, 3]
d = c  # d 引用同一个列表对象
print(f"c = {c}, d = {d}")
print(f"id(c) = {id(c)}, id(d) = {id(d)}")
print(f"c is d: {c is d}")  # True，因为它们指向同一个对象

print("\n" + "=" * 50)
print("示例2：创建两个值相同但是不同的对象")
print("=" * 50)

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]  # 创建一个新的列表对象
print(f"a = {a}, b = {b}")
print(f"id(a) = {id(a)}, id(b) = {id(b)}")
print(f"a is b: {a is b}")  # False，因为它们是两个不同的对象
'''
重要原理：
只要有赋值符号 = 时，对于可变对象（如列表），Python会：
1. 创建一个新的对象 [1,2,3,4]
2. 然后将变量b“贴”到这个新对象上
这就是Python的“名字绑定”机制。
'''

print("\n" + "=" * 50)
print("示例3：Python的intern机制（小整数和小字符串缓存）")
print("=" * 50)

# Python内部有个优化机制：intern
# 对于小整数（通常是-5到256）和小段字符串，
# Python会只生成一个全局对象，再次遇见同一个值时不会再创建新对象。

e = 1
f = 1
print(f"e = {e}, f = {f}")
print(f"id(e) = {id(e)}, id(f) = {id(f)}")
print(f"e is f: {e is f}")  # True，小整数被缓存

g = "abc"
h = "abc"
print(f"\ng = {g}, h = {h}")
print(f"id(g) = {id(g)}, id(h) = {id(h)}")
print(f"g is h: {g is h}")  # True，小字符串被缓存

# ==================== == 操作符的使用 ====================
print("\n" + "=" * 50)
print("示例4：== 比较值是否相等")
print("=" * 50)

print(f"a == b: {a == b}")  # True，因为它们的值相同

'''
== 操作符的工作原理：
- == 会调用对象的 __eq__ 魔法函数
- 它只判断值是否相等，不关心是否是同一个对象
- 可以自定义 __eq__ 方法来定义相等的逻辑
'''

# ==================== type 判断的特殊情况 ====================
print("\n" + "=" * 50)
print("示例5：使用is判断类型")
print("=" * 50)

class People:
    """人类 - 用于演示类型判断"""
    pass

person = People()

# 最常用的类型判断方式（推荐）
if isinstance(person, People):
    print("person 是 People 类的实例")

# 使用type()和is的特殊用法
if type(person) is People:
    print("\ntype(person) is People: yes!yeah!")
    
'''
为什么 type(person) is People 可行？

1. 类本身就是一个对象
2. 在Python中，每个类在全局范围内只有一个对象
3. type(person) 返回的是 People 类对象
4. People 本身也是这个类对象
5. 所以它们的 id 是一样的，is 判断返回True

但是注意：
- isinstance() 更推荐，因为它支持继承关系的检查
- type() is 只能判断精确类型，不考虑继承
'''

print(f"\nid(type(person)) = {id(type(person))}")
print(f"id(People) = {id(People)}")
print(f"type(person) is People: {type(person) is People}")

print("\n" + "=" * 50)
print("总结")
print("=" * 50)
print("""
1. is: 判断是否是同一个对象（内存地址相同）
2. ==: 判断值是否相等（调用__eq__方法）
3. isinstance(): 类型判断的最佳实践，支持继承
4. type() is: 只用于精确类型匹配，不考虑继承
""")
