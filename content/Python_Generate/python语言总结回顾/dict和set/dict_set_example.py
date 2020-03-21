'''
update
实际使用字典时，需要批量插入键值对到已有字典中，使用 update 方法实现批量插入。
已有字典中批量插入键值对：
'''
# 方法 1
d = {'a': 1, 'b': 2}
d.update({'c':3,'d':4,'e':5})
print(d)

# 方法 2
d = {'a': 1, 'b': 2}
print(d)
d.update([('c',3),('d',4),('e',5)])
print(d)

# 方法3
d = {'a': 1, 'b': 2}
print(d)
d.update(c=3,d=4,e=5)
print(d)

# 方法4
# 把方法2和3混合使用也可如：
d.update([('c',0),('d',0)],e=0)
print(d)
'''
方法4也说明，如果更新的键存在，那么依然会把键对应的值更新
'''

'''
setdefault
如果仅当字典中不存在某个键值对时，才插入到字典中；如果存在，不必插入（也就不会修改键值对）。
这种场景，使用字典自带方法 setdefault：
'''
d = {'a': 1, 'b': 2}
r = d.setdefault('c', 10)
print(r)
print(d)
r = d.setdefault('c', 99999999)
print(r)
print(d)

'''
字典并集

先来看这个函数，为了好理解，显示的给出参数类型、返回值类型，这不是必须的。
'''
def func(d:dict):
    return {**d}
print(func({'a': 1, 'b': 2}))

'''
{**d1,**d2} 实现合并 d1 和 d2，返回一个新字典, 键重复的不会和并，值不一样的话使用后一个
'''
def merge_dict(d1,d2):
    return {**d1, **d2}
print(merge_dict({'a': 1, 'b': 8}, {'c': 1, 'b': 7}))
print(merge_dict({'a': 1, 'b': 2}, {'c': 1, 'd': 2}))

def test_merge_dict():
    assert merge_dict({'a': 1, 'b': 8}, {'c': 1, 'b': 7}) == {'a': 1, 'b': 7, 'c': 1}
    assert merge_dict({'a': 1, 'b': 2}, {'c': 1, 'd': 2}) == {'a': 1, 'b': 2, 'c': 1, 'd': 2}


# 字典差
def diff_dict(d1, d2):
    return {k:v for k,v in d1.items() if k not in d2}
def test_diff_dict():
    assert diff_dict({'a':1,'b':2,'c':3},{'b':2}) == {'a':1, 'c':3}
    assert diff_dict({'a':1,'b':2,'c':3},{'b':7}) == {'a':1, 'c':3}

# 按键排序
def sort_by_key(d):
    return sorted(d.items(),key=lambda x: x[0])

def test_sort_by_key():
    assert sort_by_key({'a':10, 'z':1987, 'b':999}) == [('a',10), ('b',999), ('z',1987)]

'''
按值排序
与按照键排序原理相同，按照值排序时，key 函数定义为按值（x[1]）比较。解释为什么是 x[1]。
d.items() 返回元素为 (key, value) 的可迭代类型（Iterable），
即[(key1, value1),(key2, value2),........]
key函数的参数x便是元素 (key, value)，所以 x[1] 取到字典的值。
'''
def sort_by_value(d):
    return sorted(d.items(),key=lambda x: x[1])

def test_sort_by_value():
    assert sort_by_value({'a':10, 'z':1987, 'b':999}) == [('a',10), ('b',999), ('z',1987)]

'''
最大键
通过 keys 拿到所有键，获取最大键，返回 (最大键,值) 的元组
'''
def max_key(d):
    if len(d)==0:
        return []
    max_key = max(d.keys())
    return (max_key,d[max_key])

def test_max_key():
    assert max_key({'a':10, 'b':100, 'c': 27}) == ('c', 27)

'''
最大字典值
最大值的字典，可能有多对：
'''
def max_dict_value(d):
    if len(d) == 0:
        return []
    max_value = max(d.values())
    return [(k,v) for k,v in d.items() if v == max_value]

def test_max_dict_value():
    assert max_dict_value({'a':100, 'b':99, 'cde':100}) == [('a',100),('cde',100)]

'''
集合最值
找出集合中的最大、最小值，并装到元组中返回：
'''
def max_min_set(s):
    return (max(s), min(s))

def test_max_min_set():
    assert max_min_set((1,2,3,0,22,67,-10)) == (67, -10)

'''
单字符串
若组成字符串的所有字符仅出现一次，则被称为单字符串。
'''
def single_string1(s):
    return len(set(s)) == len(s)

def single_string2(s):
    for char in s:
        if s.count(char) > 1:
            return False
    return True

def test_single_string():
    assert single_string1("helloworld!") == single_string2("helloworld!") == False
    assert single_string1("asdfghjkl4567") == single_string2("asdfghjkl4567") == True

'''
更长集合
key 函数定义为按照元素长度比较大小，找到更长的集合：
'''
def longer_set(s1, s2):
    return max(s1, s2, key=lambda s: len(s))

def test_longer_set():
    assert longer_set((1,2,3,4), (2,6,7)) == (1,2,3,4)
    assert longer_set((1,2,3,4), (8,8,5,37)) == (1,2,3,4) # 返回第一个

'''
重复最多

在两个列表中，找出重叠次数最多的元素。默认只返回一个。
解决思路：
1、求两个列表的交集
2、遍历交集列表中的每一个元素，min(元素在列表 1 次数, 元素在列表 2 次数) ，就是此元素的重叠次数
3、求出最大的重叠次数
'''
def max_overlap_list(lst1, lst2):
    overlap = set(lst1).intersection(lst2)  # 求交集
    over_count = [(x, min(lst1.count(x), lst2.count(x))) for x in overlap]
    return max(over_count, key=lambda x: x[1])

def test_max_overlap_list():
    assert max_overlap_list([1,2,2,2,3,3],[2,2,3,2,2,3]) == (2,3)

'''
top n 键
找出字典前 n 个最大值，对应的键。
导入 Python 内置模块 heapq 中的 nlargest 函数，获取字典中的前 n 个最大值。
key 函数定义按值比较大小：
'''
from heapq import nlargest
def top_n(d,n):
    return nlargest(n,d,key=lambda k: d[k])

def test_top_n():
    assert top_n({'a': 10, 'b': 8, 'c': 9, 'd': 10}, 3) == ['a', 'd', 'c']

'''
一键对多值字典
一键对多个值的实现方法 1，按照常规思路，循序渐进：
'''
d = {}
lst = [(1,'asd'), (2,'qwerqwer'), (1,'12ras39')]
for k,v in lst:
    if k not in d:
        d[k] = []
    d[k].append(v)
print(d)
'''
以上方法，有一处 if 判断 ，确认 k 是不是已经在返回结果字典 d 中。不是很优雅！

可以使用 collections 模块中的 defaultdict，它能创建属于某个类型的自带初始值的字典。使用起来更加方便：
'''
from collections import defaultdict
d = defaultdict(list)
print(d)
for k,v in lst:
    d[k].append(v)
print(d)

'''
逻辑上合并字典
上面使用过一个合并字典的方法
'''
dic1 = {'x': 1, 'y': 2 }
dic2 = {'y': 3, 'z': 4 }
merged = {**dic1, **dic2}
print(merged)
'''
修改 merged['x']=10，dic1 中的 x 值不变，merged 是重新生成的一个“新字典”。
但是，collections 模块中的 ChainMap 函数却不同，它在内部创建了一个容纳这些字典的列表。
使用 ChainMap 合并字典，修改 merged['x']=10 后，dic1 中的 x 值改变。
如下所示：
'''
from collections import ChainMap
dict1 = {'x': 1, 'y': 2 }
dict2 = {'y': 3, 'z': 4 }
merged2 = ChainMap(dict1, dict2)
print(merged2)
merged2['x'] = 1111111
print(dict1)
print(merged2)