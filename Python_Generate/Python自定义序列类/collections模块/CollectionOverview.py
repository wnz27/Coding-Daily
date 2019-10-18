#! -*- encoding=utf-8 -*-
from collections import *

# 抽象基类 类似java的interface
from collections.abc import *

'''
# collectiongs模块

- collections模块介绍
    - 常用数据结构
    - 抽象基类

- tuple功能
    - 不可变、iterable
    - 拆包
    - tuple不可变性不是绝对的
    - tuple比list好的地方
        - immutable的重要性
            - 性能优化
                - 指出元素全部为immutable的tuple会作为常量在编译时确定，因此产生了如此显著的速度差异
            - 线程安全 (不可修改当然是线程安全)
            - 可以作为dict的key （可哈希的对象才能作为dict的key，immutable对象是可哈希的）
            - 拆包特性
        - 如果要拿C语言来类比，Tuple对应的是struct，而List对应的是array

- namedtuple详解

- defaultdict功能

- deque功能

- Counter功能

- OrderedDict功能

- ChainMap功能

'''
