#! -*- encoding=utf-8 -*-
# Python集合（set）详解 - 高性能的无序不重复元素集

'''
Python集合的核心特性：
1. 无序：元素没有固定顺序
2. 不重复：自动去重，非常适合去重操作
3. 高性能：基于哈希表实现，查找时间复杂度O(1)
4. 可变性：set可变，frozenset不可变

主要用途：
- 去重
- 成员检测（in操作）
- 集合运算（交集、并集、差集等）
'''

print("=" * 50)
print("1. 创建集合")
print("=" * 50)

# set接受任何可迭代对象，自动去重
s1 = set('abcdeed')  # 从字符串创建
s2 = set(["a", "b", "c", "d", "e"])  # 从列表创建
print(f"s1 = {s1}")  # 注意：'e'和'd'只保留一个
print(f"s2 = {s2}")

# 使用字面量语法创建集合
s5 = {'a', 'b', 'p', 'n'}
print(f"s5的类型: {type(s5)}")  # <class 'set'>

# frozenset - 不可变集合
print("\n" + "=" * 50)
print("2. frozenset（不可变集合）")
print("=" * 50)

s4 = frozenset("123456")
print(f"frozenset: {s4}")

# frozenset不支持add、remove等修改操作
# s4.add("t")  # 会报错：AttributeError: 'frozenset' object has no attribute 'add'

print("""
frozenset的特点和用途：

1. 不可变性：
   - 创建后不能添加、删除元素
   - 没有add、remove、clear等方法

2. 重要用途：
   - 可以作为字典的键（dict key必须是不可变类型）
   - 可以作为其他集合的元素
   - 适合作为常量集合使用

3. 性能：
   - 查找速度同样是O(1)
   - 由于不可变，可以被哈希

示例：
   frozen_set = frozenset([1, 2, 3])
   my_dict = {frozen_set: 'value'}  # ✓ 可以作为key
   normal_set = {1, 2, 3}
   my_dict = {normal_set: 'value'}  # ✗ 会报错
""")

# 添加元素到集合
print("\n" + "=" * 50)
print("3. 集合的添加和更新操作")
print("=" * 50)

another_set = set("defab")
# update() - 批量添加元素，接受可迭代对象
s5.update(another_set)
print(f"update后的s5: {s5}")

print("""
集合的添加方法：
- add(elem)：添加单个元素
- update(iterable)：批量添加多个元素
- |= 运算符：等同update()
""")

# 集合运算
print("\n" + "=" * 50)
print("4. 集合运算（交集、并集、差集）")
print("=" * 50)

s3 = {'a', 'b', 'p', 'n'}

# difference() - 差集：属于s3但不属于another_set的元素
result_set = s3.difference(another_set)
print(f"s3 - another_set = {result_set}")

# 使用 - 运算符实现差集（与difference()等价）
result_set1 = s3 - another_set
print(f"s3 - another_set = {result_set1}")

# 交集 - 使用 & 运算符
result_set2 = s3 & another_set
print(f"s3 & another_set (交集) = {result_set2}")

# 并集 - 使用 | 运算符
result_set3 = s3 | another_set
print(f"s3 | another_set (并集) = {result_set3}")

print("""
集合运算总结：

1. 交集（Intersection）：
   - s1 & s2 或 s1.intersection(s2)
   - 返回两个集合共有的元素

2. 并集（Union）：
   - s1 | s2 或 s1.union(s2)
   - 返回两个集合的所有元素（去重）

3. 差集（Difference）：
   - s1 - s2 或 s1.difference(s2)
   - 返回s1有但s2没有的元素

4. 对称差集（Symmetric Difference）：
   - s1 ^ s2 或 s1.symmetric_difference(s2)
   - 返回只在其中一个集合中的元素

5. 就地修改运算：
   - |=, &=, -=, ^=
   - 直接修改原集合
""")

# 集合性能特点
print("\n" + "=" * 50)
print("5. 集合的高性能特性")
print("=" * 50)

print("""
set的性能优势：
- 基于哈希表实现，与dict原理一致
- 查找元素时间复杂度为O(1)
- 成员检测（in操作）非常快
- 对比list的O(n)查找，set在大数据集上有巨大优势
""")

# 成员检测 - in 运算符
print("\n" + "=" * 50)
print("6. 成员检测和子集判断")
print("=" * 50)

# 集合实现了__contain__魔法函数，支持in语句
if 'b' in result_set3:
    print("'b' 在集合中")

# issubset() - 判断是否是子集
lalala = s3.issubset(result_set3)
print(f"s3 是 result_set3 的子集: {lalala}")

print("""
子集和超集判断：
- issubset(other)：判断是否为子集
- issuperset(other)：判断是否为超集
- isdisjoint(other)：判断两集合是否没有交集
- 也可以使用 <=, <, >=, > 运算符
""")