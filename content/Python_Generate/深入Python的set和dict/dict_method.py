#! -*- encoding=utf-8 -*-
# Python字典（dict）的常用方法详解

'''
本文件演示Python字典的常用方法和操作技巧，包括：
- copy()：浅拷贝
- deepcopy()：深拷贝
- fromkeys()：创建新字典
- setdefault()：带默认值的获取/设置
- update()：更新字典
'''

print("=" * 50)
print("1. 字典的浅拷贝和深拷贝")
print("=" * 50)

# 原始字典（包含嵌套字典）
a = {
    "fzk": {"company": "yuner"},
    "fzk2": {"company": "yuner2"}
}

# copy() - 返回浅拷贝
new_dict = a.copy()
new_dict["fzk"]["company"] = "lalalal"

print(f"修改后的new_dict: {new_dict}")
print("vs")
print(f"原始字典a: {a}")
print(f"a的地址: {id(a)}")
print(f"new_dict的地址: {id(new_dict)}")

print("""
浅拷贝的特点：
- 创建一个新的字典对象（地址不同）
- 但字典内的可变对象（如嵌套的字典）仍然是引用
- 修改嵌套对象会影响原字典
- 适用于字典值都是不可变类型的情况
""")

# 深拷贝 - 需要引入copy模块
print("\n" + "=" * 50)
print("2. 深拷贝")
print("=" * 50)

import copy as cp
new_dict1 = cp.deepcopy(a)  # 创建完全独立的副本
new_dict1["fzk"]["company"] = "12344556"

print(f"原始字典a: {a}")
print("vs")
print(f"深拷贝后的new_dict1: {new_dict1}")

print("""
深拷贝的特点：
- 递归复制所有层级的对象
- 创建完全独立的副本
- 修改任何层级都不会影响原字典
- 适用于包含嵌套可变对象的情况
- 性能开销较大，但更安全
""")

# fromkeys() - 快速创建字典
print("\n" + "=" * 50)
print("3. fromkeys() 方法")
print("=" * 50)

# fromkeys(keys, value) - 从可迭代对象创建字典
# 第一个参数：可迭代对象，用作字典的键
# 第二个参数：所有键共享的默认值
new_list = ["yuenr1", "yuner2"]
new_dict2 = dict.fromkeys(new_list, {"company": "nimahai"})
print(f"fromkeys创建的字典: {new_dict2}")

print("""
fromkeys注意事项：
- 所有键共享同一个值对象（如果值是可变对象要小心）
- 如果不提供第二个参数，默认值为None
- 常用于初始化默认值字典
""")

# setdefault() - 带默认值的获取/设置
print("\n" + "=" * 50)
print("4. setdefault() 方法")
print("=" * 50)

# setdefault(key, default) - 如果key存在返回其值，否则设置为default并返回
default_value = new_dict2.setdefault("fzk", "hahahahah")
print(f"setdefault返回值: {default_value}")
print(f"更新后的字典: {new_dict2}")

print("""
setdefault的特点：
- 如果键不存在，添加键值对并返回default
- 如果键存在，返回现有值，不修改字典
- 比先判断再添加更高效和简洁
""")

# update() - 批量更新字典
print("\n" + "=" * 50)
print("5. update() 方法的多种用法")
print("=" * 50)

# 方式1：使用字典更新
new_dict2.update({"1992": "0825"})
print(f"方式1 - 字典更新: {new_dict2}")

# 方式2：使用关键字参数更新
new_dict2.update(fzk="999", fzk2="888")
print(f"方式2 - 关键字参数: {new_dict2}")

# 方式3：使用可迭代对象（列表包含元组）
new_dict2.update([("000", "111"), ("222", "333"), ("444", "555")])
print(f"方式3 - 列表包含元组: {new_dict2}")

# 方式4：使用元组包含元组
new_dict2.update((("666", "777"), ("888", "999"), ("aaa", "bbb")))
print(f"方式4 - 元组包含元组: {new_dict2}")

print("""
update()方法的特点：
1. 可以接受多种类型的参数：
   - 字典对象
   - 关键字参数
   - 可迭代对象（每个元素是(key, value)对）

2. 更新规则：
   - 如果键已存在，更新其值
   - 如果键不存在，添加键值对
   - 就地修改原字典，不返回新字典

3. 使用场景：
   - 合并多个字典
   - 批量更新配置
   - 添加多个键值对
""")