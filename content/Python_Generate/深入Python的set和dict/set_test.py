#! -*- encoding=utf-8 -*-

# set集合， fronzenset不可变集合
# 无序，  不重复    去重非常好用

# set接受一个可迭代的对象
s1 = set('abcdeed')
s2 = set(["a","b","c","d","e"])
print(s1)
print(s2)
s5 = {'a', 'b','p','n'}
print(type(s5))     # <class 'set'>

s4 = frozenset("123456")
'''
s4.add("t")
输出：
Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/深入Python的set和dict/set_test.py", line 15, in <module>
    s4.add("t")
AttributeError: 'frozenset' object has no attribute 'add'
'''
print(s4)

'''
所以frozenset一个重要的用途就是可以作为dict的key值
'''

# 向set添加数据， 常用的是add
another_set = set("defab")
s5.update(another_set)
print(s5)

s3 = {'a', 'b','p','n'}
# 集合运算 |= -= ^= 
result_set = s3.difference(another_set)
print(result_set)
# 返回的是属于s3里面的，且another_set里面没有的
result_set1 = s3 - another_set
print(result_set1)
result_set2 = s3 & another_set  #交集
print(result_set2)
result_set3 = s3 | another_set  # 并集
print(result_set3)

'''
set 性能很高，和dict原理一样，是哈希，查找某个元素的时候时间复杂度是1
'''

# 有__contain__魔法函数，所以可以使用in语句
if 'b' in result_set3:
    print("i am in set")

# issubset 判断一个集合是不是另一个集合的子集
lalala = s3.issubset(result_set3)
print(lalala)