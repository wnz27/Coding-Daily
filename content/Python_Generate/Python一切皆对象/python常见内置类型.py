#! -*- encoding=utf-8 -*-
# Python常见内置类型完整概览

'''
Python对象的三个基本特征：

1. 身份（Identity）：
   - 对象在内存中的地址
   - 可以用id()函数来查看
   - 对象一旦创建，身份就不会改变

2. 类型（Type）：
   - 决定对象支持哪些操作
   - 可以用type()函数来查看
   - 对象的类型也是不可改变的

3. 值（Value）：
   - 对象所代表的数据
   - 有些对象的值可变（如列表），有些不可变（如元组）
'''

# None类型 - Python的空值
print("=" * 50)
print("1. None类型")
a = None
b = None
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(a) == id(b): {id(a) == id(b)}")  # True
'''
重要特性：
None在Python中是单例模式，全局只有一个None对象。
所有指向None的变量实际上都指向同一个内存地址。
'''

# 数值类型
print("\n" + "=" * 50)
print("2. 数值类型")
print("""
Python的数值类型包括：
- int：整数类型，支持任意大小的整数
- float：浮点数类型，用于表示小数
- complex：复数类型，如 3+4j
- bool：布尔类型，True/False，昬int的子类
""")

# 迭代类型
print("\n" + "=" * 50)
print("3. 迭代类型")
print("""
迭代类型是实现了__iter__或__getitem__方法的对象。
包括列表、元组、字符串、字典、集合等。
""")

# 序列类型
print("\n" + "=" * 50)
print("4. 序列类型")
print("""
序列类型是有序的容器类型，支持索引访问、切片等操作：

1. list：可变序列，用[]表示，如[1, 2, 3]
2. tuple：不可变序列，用()表示，如(1, 2, 3)
3. str：字符串，不可变序列，用''or""表示
4. bytes：不可变字节序列，用b''表示
5. bytearray：可变字节序列
6. memoryview：内存视图，用于高效访问大型数据
7. range：范围对象，如range(10)
8. array：数组模块的数组类型
""")

# 映射类型（dict）
print("\n" + "=" * 50)
print("5. 映射类型")
print("""
dict：字典类型，键值对映射，用{}表示。
特点：
- 键必须是不可变类型（可哈希）
- 无序集合（Python 3.7+保持插入顺序）
- 查找效率高，时间复杂度O(1)
""")

# 集合类型
print("\n" + "=" * 50)
print("6. 集合类型")
print("""
1. set：可变集合，无序且元素唯一
2. frozenset：不可变集合，可以作为dict的key

特点：
- set和dict在Python中的实现原理几乎一致
- 都使用哈希表实现，效率非常高
- 支持快速的成员检测和集合运算
""")

# 上下文管理器类型
print("\n" + "=" * 50)
print("7. 上下文管理器类型")
print("""
实现了__enter__和__exit__方法的对象。
用于with语句，确保资源的正确获取和释放。

例如：
- 文件对象：with open('file.txt') as f:
- 锁对象：with lock:
- 数据库连接：with conn:
""")

# 其他特殊类型
print("\n" + "=" * 50)
print("8. 其他特殊类型")
print("""
Python还有很多内部类型：

1. 模块类型：import导入的模块对象
2. 类和实例：自定义的class和实例对象
3. 函数类型：def定义的函数、lambda函数
4. 方法类型：类中定义的方法
5. 代码类型：编译后的字节码对象
6. object对象：所有类的基类
7. type类型：所有类的元类
8. ellipsis类型：省略号类型，在切片中使用，如...
9. NotImplemented类型：在面向对象高级设计时用到

这些类型共同构成了Python丰富的类型系统！
""")