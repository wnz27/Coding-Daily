'''
应用场景一：
检查某个类是否有某种方法
'''
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    
    def __len__(self):
        return len(self.employee)

company = Company(["tom", "bob"])
print(hasattr(company, "__len__"))  #company 这个实例是否有这个（__len__）函数
# print(len(company))

#我们再某些情况之下希望判定某个对象的类型，就需要利用抽象基类
from collections.abc import Sized
print(isinstance(company, Sized))

#我们需要强制某个子类必须实现某些方法
'''
假如我们实现了一个web框架，集成cache(redis, cache, memorycache)
需要设计一个抽象基类，指定子类必须实现某些方法,比如类似：
'''
# 如何去模拟一个抽象基类
'''
class CacheBase():
    def get(self, key): # 从缓存获取数据
        raise NotImplementedError
    def set(self, key, value): # 给缓存添加数据
        raise NotImplementedError
'''
'''
强制用户去自己实现这些统一的方法
'''
'''
class RedisCache(CacheBase):
    pass
'''
# 如果不实现这些方法，那么就会抛出上面定义的异常
'''
redis_cache = RedisCache()
redis_cache.set("key", "value")
'''
'''
Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/抽象基类.py", line 38, in <module>
    redis_cache.set("key", "value")
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/抽象基类.py", line 30, in set
    raise NotImplementedError
NotImplementedError
'''
# 只有在调用set方法的时候才会抛出异常，我们想要在子类没实现这些方法时
# 在子类实例化时候就抛出异常，我们需要怎么做，需要用到abc模块
import abc  # 全局abc
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key): # 从缓存获取数据
        pass
    @abc.abstractmethod
    def set(self, key, value): # 给缓存添加数据
        pass


class RedisCache(CacheBase):
    pass

redis_cache = RedisCache()
'''
如果没实现抽象方法，则会在初始化的时候报错
Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/抽象基类.py", line 67, in <module>
    redis_cache = RedisCache()
TypeError: Can't instantiate abstract class RedisCache with abstract methods get, set
'''