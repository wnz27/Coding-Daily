#! -*- encoding=utf-8 -*-
# Python异常处理和with上下文管理器详解

'''
Python异常处理机制：

1. try-except-else-finally 结构：
   - try: 尝试执行可能出错的代码
   - except: 捕获和处理异常
   - else: 当没有异常时执行
   - finally: 无论是否有异常都会执行

2. finally 的特殊性：
   - 一定会执行，用于资源清理
   - 即使有return也会执行
   - finally中的return会覆盖try/except中的return

3. with 上下文管理器：
   - 更优雅的资源管理方式
   - 自动处理资源的获取和释放
   - 需要实现__enter__和__exit__方法
'''

print("=" * 50)
print("1. 异常处理基础")
print("=" * 50)

# 示例1：捕获特定异常
print("\n示例1：捕获特定异常")
try:
    print("code started")
    raise KeyError("Test KeyError")
except KeyError as e:
    print(f"key error: {e}")

print("""
注意：
- 如果抛出的异常类型与except不匹配，异常会向上传递
- 例如：raise IndexError 但except KeyError，会报错
""")

# else的用法，可以捕捉到前面没有捕捉到的异常
try:
    print("code started")
    raise KeyError
except KeyError as e:
    print("key error")
else:
    print("other error")
finally:  # 不管你有没有运行前面，都会运行里面的代码
    print("finally")

    # 所以finally的用处就是比如打开文件，那不管中间过程有没有异常
    # 有多少异常，都需要把文件close掉，所以finally就显得很有用了
    # 实现了一种资源的释放，比如打开数据库连接后断开，等等等都可以
    '''
    raise IndexError时输出：
    code started
    finally
    Traceback (most recent call last):
    File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/with_test.py", line 26, in <module>
        raise IndexError
    IndexError
    raise KeyError时输出：
    code started
    key error
    finally
    '''
def exe_try():
    try:
        print("code started")
        raise KeyError
        return 1
    except KeyError as e:
        print("key error")
        return 2
    else:
        print("other error")
        return 3
    finally:  # 不管你有没有运行前面，都会运行里面的代码
        print("finally")
        return 4

# 上下文管理器   with  上下文管理器协议：与魔法函数挂钩
'''
上下文管理器：
__enter__
__exit__
'''
class Sample():
    def __enter__(self):
        # 获取资源
        print("enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")
    def do_something(self):
        print("doing something")

with Sample() as sample:
    sample.do_something()
    '''
    输出：
    enter
    doing something
    exit
    '''
    '''
    这个执行顺序是我们使用with语句后python解释器自动完成的
    所以我们可以在__exit__里面释放资源
    在__enter__里面获取资源
    然后在自己定义的方法里面使用资源！
    '''

# 测试
# if __name__ == "__main__":
#     result = exe_try()
#     print(result)

    '''
    如果有finally语句，则会return finally里的return，
    如果没有finally，或者finally里没有return，就会返回调用地方的语句
    该例子里面如果把return 4注释掉则会返回2
    '''

    '''
    python的with语句就是为了简化try、except语句这种写法而诞生的
    '''