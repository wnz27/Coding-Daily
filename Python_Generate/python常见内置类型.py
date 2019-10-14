'''
对象的三个特征：身份，类型，值
身份既是对象在内存当中的地址，可以用id这个函数来查看
'''
# None
a = None
b = None
print(id(a))
print(id(b))
print(id(a) == id(b))
'''
输出：
4393642536
4393642536
True
'''
'''
None 全局只有一个
'''

# 数值类型：
'''
int float complex(复数) bool
'''

# 迭代类型

# 序列类型：
'''
list
bytes、bytearray、memoryview（二进制序列）
range
tuple
str
array
'''

# 映射(dict)

# 集合
'''
set
frozenset (不可修改set)
'''
'''
ps：
set和dict在python中的实现原理几乎是一致的,效率都会非常高
'''

# 上下文管理类型   with

# 其他类型
'''
模块类型
class和实例
方法类型
代码类型
object对象
type类型
ellipsis类型(省略号类型)
notimplemented类型(在面向对象高级的设计的时候会用到)
'''