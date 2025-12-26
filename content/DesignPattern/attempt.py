'''
@Author: 27
@LastEditors: 27
@Date: 2020-02-14 09:28:12
@LastEditTime: 2020-02-26 15:06:56
@FilePath: /Coding-Daily/DesignPattern/attempt.py
@description: Python基础语法练习 - 各种常用操作和技巧
'''

# ==================== 列表和字典操作 ====================
print("=" * 50)
print("列表和字典操作")
print("=" * 50)

b = [1, 7, 5, 9, 2, 12, 3]
a = range(len(b))
# 使用zip和字典推导式创建字典
c = {k: v for k, v in zip(a, b)}
print(f"字典c: {c}")

# 查找列表中相差为2的数对
result = []
for value in b:
    if (value + 2) in b:
        result.append((value, value+2))
print(f"相差为2的数对: {result}")

d = "asdfasdf asdfafads asdfasdf"
s = d.split(' ')
g = '%20'.join(s)
print(g)
print(max(1, 1))

print("fzk".join(" 13 13 21 ".split(" ")))

from numpy import random
lala = random.randint(1,5, 10)
print("*"*40,lala)

print(list(range(0, 10, 3)))

a = [2,2,2,2,2,2,2]
b = []
print(max(b, default=100))

name = "lucas"
judge = False
print(name.upper() == 'LUCAS' and judge)

# print([1,23,4].index(5))

a = str(["asdf", "adfadsfdfadsf"])
print(type(a), ":", a)
print(a[0])
print(str(["asdfadsfadsf"]),str(["asdfadsfadsf"])[:2])
print(str(tuple("1"))[:2])

b = {}
print(b.setdefault(4,"not"))
print(b.setdefault(4, "lallal"))
print(b)