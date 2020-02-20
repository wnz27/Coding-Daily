from random import randint

'''
// 用于向下取整
In [1]: 5//2
Out[1]: 2
In [2]: 5//4.5
Out[2]: 1.0

** 用于幂运算：
In [1]: 2**3
Out[1]: 8
'''

# 判断列表有无重复元素
'''
is_duplicated，使用 list 封装的 count 方法，依次判断每个元素 x 在 list 内的出现次数。
如果大于 1，则立即返回 True，表示有重复。
如果完成遍历后，函数没返回，表明 list 内没有重复元素，返回 False。
'''
def is_Duplicated(lst):
    for item in lst:
        if lst.count(item) > 1:
            return True
        return False

def test_is_Duplicated():
    test_list = [randint(0,4) for _ in range(15)]
    assert is_Duplicated(test_list) == True

# 列表翻转
'''
一行代码实现列表反转，非常简洁。
[::-1]，这是切片的操作。
[::-1] 生成逆向索引（负号表示逆向），步长为 1 的切片。
'''
def reverse(lst):
    return lst[::-1]

def test_reverse():
    assert reverse([1,2,3,4,5,6]) == [6,5,4,3,2,1]
    assert reverse([100]) == [100]
    assert reverse([]) == []

# 找出列表中的所有重复元素
def find_duplicate(lst):
    res = []
    for item in lst:
        if lst.count(item) > 1 and item not in res:
            res.append(item)
    return res

def test_find_duplicate():
    assert find_duplicate([4,2,67,4,4,2,2,9,10]) == [4,2]

# 斐波那契数列
# 一般实现
def fib_normal(n):
    if n <= 1:
        return n
    else:
        return fib_normal(n - 1) + fib_normal(n - 2)

# 利用字典实现
def fib_dict(n, dic):
    if n <= 1:
        return n
    else:
        if dic.get(str(n)):
            return dic.get(str(n))
        else:
            dic[str(n)] = fib_dict(n-1, dic) + fib_dict(n-2, dic)
            return dic.get(str(n))
    
# 迭代实现
def fib_generate(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a+b
    return a
# yield生成器
def fib_yield(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a+b

print(list(fib_yield(5)))


def test_fib():
    test_dict = {}
    assert fib_normal(10) == fib_dict(10,test_dict) == fib_generate(10)
    assert list(fib_yield(5)) == [0,1,1,2,3]

'''
最高频率

max 函数是 Python 的内置函数，所以使用它无需 import。
max 有一个 key 参数，指定如何进行值得比较。
下面案例，求出出现频次最多的元素：
'''
def max_frequency(lst):
    return max(lst, key = lambda v: lst.count(v))

def max_frequency_gen(lst):
    res = []
    first_maxfre = max(lst, key = lambda v: lst.count(v))
    res.append(first_maxfre)
    for item in lst:
        if lst.count(item) == lst.count(first_maxfre) and item not in res:
            res.append(item)
    return res

def test_max_fre():
    assert max_frequency([1,1,1,2,2,3,3,3,2]) == 1

def test_max_fre_gen():
    assert max_frequency_gen([1,1,1,2,3,4,5,5,4,3,4,3,5,]) == [1,3,4,5]

'''
最长的列表

带有一个 * 的参数为可变的位置参数，意味着能传入任意多个位置参数。
以下例子lists传进函数之后是一个元组
key 函数定义怎么比较大小：lambda 的参数 v 是 lists 中的一个元素。
'''
def max_len(*lists):
    return max(*lists, key=lambda v: len(v))

def test_max_len():
    assert max_len([1,2,3,4,5], [2,3,9], [2,3,4,5]) == [1,2,3,4,5]

'''
求表头
返回列表的第一个元素，注意，列表为空时，返回 None。
通过此例，学会使用 if 和 else 的这种简洁表达。
'''
def head(lst):
    return lst[0] if len(lst) > 0 else None

def test_head():
    assert head([]) == None and head([2,5,6]) == 2 and head([100]) == 100

'''
求表尾

求列表的最后一个元素，同样列表为空时，返回 None。
'''
def tail(lst):
    return lst[-1] if len(lst) > 0 else None

def test_tail():
    assert tail([]) == None and tail([3,7,8]) == 8 and tail([99]) == 99

'''
打印乘法表

外层循环一次，print()，换行；内层循环一次，打印一个等式。
print有一个end参数可以指定结尾，这样不用默认换行。
'''
def mul_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print('{} * {} = {}'.format(j, i, j * i), end='\t')
        print()
mul_table()

'''
元素对

t[:-1]：原列表切掉最后一个元素；
t[1:]：原列表切掉第一个元素；

zip(iter1, iter2)，实现 iter1 和 iter2 的对应索引处的元素拼接。
In [32]: list(zip([1,3],[4,7]))
Out[32]: [(1, 4), (3, 7)]

利用这个特性，我们实现一个列表中每个元素和后面一个元素组成对：
'''
def pair(lst):
    return list(zip(lst[:-1], lst[1:]))

def test_pair():
    assert pair([1,5,10]) == [(1,5), (5,10)]
    assert pair(range(0,10,3)) == [(0,3),(3,6),(6,9)]

'''
样本抽样

内置 random 模块中，有一个 sample 函数，实现“抽样”功能。

下面例子从 100 个样本中，随机抽样 10 个。
首先，使用列表生成式，创建长度为 100 的列表 lst；
然后，sample 抽样 10 个样本。
'''
from random import randint, sample

def my_sample():
    lst = [randint(0,50) for _ in range(100)]
    print(lst[:5])
    lst_sample = sample(lst, 10)
    print(lst_sample)
my_sample()

'''
重洗数据集

内置 random 中的 shuffle 函数，能冲洗数据。
shuffle 是对输入列表就地（in place）洗牌，节省存储空间。
'''
from random import shuffle
def shuffle_exmple():
    lst = [randint(0,50) for _ in range(10)]
    print(lst)
    shuffle(lst)
    print(lst)
shuffle_exmple()

'''
生成满足均匀分布的坐标点

random 模块，uniform(a,b) 生成 [a,b) 内的一个随机数。
如下，借助列表生成式，生成 100 个均匀分布的坐标点。
'''
from random import uniform
from pyecharts.charts import Scatter
import pyecharts.options as opts

def draw_uniform_points():
    x,y = [i for i in range(100)], [round(uniform(0,10), 2) for _ in range(100)]
    print(y)
    c = (
        Scatter()
        .add_xaxis(x)
        .add_yaxis('y', y)
    )
    c.render()
draw_uniform_points()
'''
生成了一个图像的html文件，在当前文件夹里。
'''