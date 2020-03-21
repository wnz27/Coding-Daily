'''
字典的创建方法
'''
# 1、手动
empty_dict = {}
d1 = {'a': 1, 'b': 2, 'c': 3}
print(empty_dict, d1)

# 2、使用 dict() 构造函数，全用关键字参数
d2 = dict(a=1, b=2, c=3)
print(d2)

# 3、第一个位置传入键值对 + 关键字参数，第一个参数为字典，后面是一系列关键字参数，如 c=3：
d3 = dict({'a': 10}, b=4, c=6)
print(d3)

# 4、第一个传入可迭代对象
d4 = dict((('a', 1),), b=5)
d44 = dict([('a', 10)], b=99)
print(d4,d44)

# 5、fromkeys() 方法，已知键集合（keys），values 为初始值：
d5 = {}.fromkeys(['k1','k2','k3'],[1,2,3])
print(d5)

# 6、列表推导生成dict，以下a是key，b是每个key对应的value
b = [10,7,5,9,2,12,3]
a = range(1,len(b))
d6 = {k:v for k,v in zip(a, b)}
print(d6, d6[1])
# 用以上方法可以构造出一个类似下标从1开始的数组哈哈哈真是无聊啊！！！！

'''
遍历字典
比如遍历d6
'''
for k,v in d6.items():
    print(k, v)

# 获取所有键集合
# 方法一
print(set(d6))
# 方法二
print(set(d6.keys()))

# 获取所有值集合
print(set(d6.values()))

# 判断键是否在字典中：
if 1 in d6:
    print("键{}在字典d6中！".format(1))

if 100 not in d6:
    print("键{}不在字典d6中！".format(100))

# 获取某键对应的值，可以加第二个参数在没有值时回复一个给定的占位值
print(d6.get(2))
print(d6.get(100, '没有此键'))

# 添加或修改一个键值对：
d6[1] = 111111
print(d6)

# 删除一个键值对：
del d6[1]
print(d6)
d6.pop(2)
print(d6)

# 字典视图
print(d6.keys())
print(d6.values())
print(d6.items())
'''
它们都是原字典的视图，修改原字典对象，视图对象的值也会发生改变。
'''

# 字典的键
'''
字典的键
所有对象都能作为字典的键吗？
如果一个列表对象 lst 试图作为字典的键，会出现什么问题。
实验一下：
'''
# lst = [1,2]
# d = {lst:'ok?'}
'''
TypeError: unhashable type: 'list'
会抛出如上 TypeError 异常：不可哈希的类型 list。
因为列表是可变对象，而可变对象是不可哈希的，所以会抛出如上异常。

结论：可哈希的对象才能作为字典的键，不可哈希的对象不能作为字典的键。
'''

'''
集合
集合是一种不允许元素出现重复的容器。
案例：判断一个列表中是否含有重复元素，便可借助集合这种数据类型。
'''
def duplicated(lst):
    return len(lst)!=len(set(lst)) # 不相等就意味着含重复元素
# 列表去重也可以用集合

# 集合创建
'''
与字典（dict）类似，集合（set）也是由一对花括号（{}）创建。但是，容器内的元素不是键值对。
'''
set1 = {1,2,3}
'''
同字典类似，集合内的元素必须是可哈希类型（hashable）。
这就意味着 list、dict 等不可哈希的对象不能作为集合的元素。

另一种创建集合的方法，是通过 Python 的内置的 set 函数，参数类型为可迭代对象 Iterable。
'''
set2 = set([1,2,3,4])
print(set2)

# 求并集
a = {1,3,5,7}
b, c = {3,4,5,6}, {6,7,8,9}
d = a.union(b,c) # {1, 3, 4, 5, 6, 7, 8, 9}

# 求差集
a = {1,3,5,7}
b, c = {3,4,5,6}, {6,7,8,9}
d = a.difference(b,c) # {1} 在a中不在b和c中的元素构成的集合

# 求交集
a = {1,3,5,7}
b, c = {3,4,5,6}, {6,7,8,9}
d = a.intersection(b,c) # {} 同时在abc集合中的元素构成的集合

# 查看一个集合是否是另一个元素的子集
a = {1,3,5,7}
b = {3,4,5,6}
print(a.issubset(b))
print(a.issubset(a))
print(a.issubset({1,2,3,5,7,8}))