#! -*- encoding=utf-8 -*-

# 不建议继承list和dict

# 试一下继承
class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

my_dict = Mydict(one=1)
print(my_dict)
'''
输出：{'one': 1}
并没有调用父类的set方法
'''
# 但我们使用下面这种方法：
my_dict["one"] = 1
print(my_dict)
'''
我们发现这里更改了
输出：{'one': 2}
某些情况，用c语言写的某些方法，不会ß去调用父代的方法，所以不建议去继承dict
'''

from collections import UserDict

class Mydict2(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

my_dict2 = Mydict2(one=1)
print(my_dict2)
# 这个输出就是：{'one': 2}
'''
所以实在想继承dict就去继承UserDict而不要继承dict
'''

from collections import defaultdict

my_dict3 = defaultdict(dict)
my_value = my_dict3["fzk"]
print(my_value)     # 输出为空：{}