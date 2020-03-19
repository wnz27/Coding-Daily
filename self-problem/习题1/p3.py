'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-19 12:05:01
@LastEditTime: 2020-03-20 02:15:18
@FilePath: /Coding-Daily/self-problem/习题1/p3.py
@description: type some description
'''
'''
3. 请实现一个 Python 装饰器类：缓存函数执行结果，支持指定存储方式和过期时间
指定存储方式和过期时间，这个。。。。暂时没啥思路啊
这个即使以字符串形式传进来数据库名称，但是具体的存储也要依赖导入的库和配置信息？
所以咋整嘞。。。。。
'''
from abc import ABCMeta, abstractmethod
import time
import threading
# 先模拟存储方式？先做个统一设置和清理缓存的接口？？
class HandleDB:
    @abstractmethod
    def clearCache():
        pass
    @abstractmethod
    def setCache():
        pass
# 真正处理数据的类继承这个接口？定义一个
class MySQLDB(HandleDB):
    def setCache(self, cache):
        print("mysql存储的缓存为:", cache)

    def clearCache(self):
        print("mysql已经把缓存清除")
# 再定义一个？
class MyRedisDB(HandleDB):     
    def setCache(self, cache):
        print("redis存储的缓存为:", cache)
    
    def clearCache(self):
        print("redis已经把缓存清除")

# 使用__call__方法构建装饰器
class CacheFuncResult:
    def __init__(self, func, self_pattern="mysql", exp=5):
        '''
        接收缓存方式和过期时间
        实例化一个执行缓存和清除缓存的对象
        '''
        self.func = func
        self.cache_container = self.set_cache_container(self_pattern.lower())
        self.clock = exp
    def __call__(self, *args, **kwargs):
        print("缓存方式为：", self.cache_container)
        print("缓存过期时间为：", self.clock)
        print("传进来的参数为:------>", *args, **kwargs)
        result = self.func(*args, **kwargs)     # 暂存函数执行结果
        self.cache_container.setCache(result)   # 增加缓存
        threading.Timer(self.clock, self.expiretion_clear).start()  # 非阻塞的定时器清除缓存
        return result
    def expiretion_clear(self):
        self.cache_container.clearCache()
        
    def set_cache_container(self, self_pattern):
        if self_pattern == "mysql":
            return MySQLDB()
        elif self_pattern == "redis":
            return MyRedisDB()
        else:
            raise ValueError("we are now can't support this pattern!")

def my_example(haha):
    print("我的参数是：", haha)
    return haha

# 写完这个发现这样的装饰器调用方式有点儿不习惯其实，但如果不传参可以用传统的调用方式
my_example = CacheFuncResult(my_example,self_pattern="mysql", exp=5)

my_example("272727heiheiheihei")
print("lalalalal")  # 测试异步
        
