# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/1 18:23
__author__ = '27'


def simple_coroutine():  # 协程使用生成器函数定义:定义体中有 yield 关键字。
    print('-> coroutine started')
    x = yield  # 如果协程只从客户那里接收数据，那么产出的值是None，这个值是隐式指定的，因为yield关键字右边没有表达式
    print('-> coroutine received:', x)


my_coro = simple_coroutine()  # 调用函数得到生成器对象
print(my_coro)  # <generator object simple_coroutine at 0x1012956d0>
next(my_coro)   # 因为生成器还没启动，没在yield处暂停，所以一开始无法发送数据。
my_coro.send(42)    # 调用这个方法后，协程定义体中的yield会计算出42，现在，协程会恢复，一直运行到下一个yield表达式，或者终止。
# 然后控制权流动到协程定义体的末尾，导致协程生成器向往常一样抛出StopIteration异常。

'''
协程可以身处四个状态中的一个。当前状态可以使用 inspect.getgeneratorstate(...) 函数确定，该函数会返回下述字 符串中的一个。
'GEN_CREATED'
  等待开始执行。
'GEN_RUNNING'
  解释器正在执行。      只有在多线程应用中才能看到这个状态。此外，生成器对象在自己身上调用getgeneratorstate 函数也行，不过这样做没什么用。
'GEN_SUSPENDED'
  在 yield 表达式处暂停。 
'GEN_CLOSED'   
  执行结束。
因为 send 方法的参数会成为暂停的 yield 表达式的值，所以，仅当协程处于暂停状态时才能调用 send 方法|传值|，例如 my_coro.send(42)。
不过，如果协程还没激活(即，状态是 'GEN_CREATED')，情况就不同了。
因此，始终要调用 next(my_coro) 激活协程——也可以调用 my_coro.send(None)，效果一样。
如果创建协程对象后立即把 None 之外的值发给它，会出现下述错误:
>>> my_coro = simple_coroutine() 
>>> my_coro.send(1729)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: can't send non-None value to a just-started generator
不能把非空的值传给刚建立好的生成器。

最先调用 next(my_coro) 函数这一步通常称为“预激”(prime)协程 
(即，让协程向前执行到第一个 yield 表达式，准备好作为活跃的协 程使用)。
'''


