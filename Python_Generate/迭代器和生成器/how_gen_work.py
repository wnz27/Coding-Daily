#! -*- encoding=utf-8 -*-
# pyhton 中函数的工作原理
import inspect
frame = None
def foo():
    bar()
def bar():
    global frame
    frame = inspect.currentframe()

'''
python.exe这个是C语言的解释器。它会用一个叫做PyEval_EvalFramEx的C语言函数
去执行foo函数，这个函数在运行python的函数的时候，它首先会创建一个栈帧（stack frame）
这个栈帧实际上是一个上下文，它也是一个对象，体现python一切皆对象，把函数变成字节码对象
在栈帧对象的上下文里运行函数的字节码，函数字节码全局是唯一的。
当foo调用子函数bar，又会创建一个栈帧，
所有的栈帧都是放在堆内存上，而不是放在栈内存上，堆内存有个特性是
只要你不释放他，他就会一直在我们的内存当中。
这个特性决定了栈帧可以独立于调用者存在。
我们调不调用，它都在那儿，只要我们指向它的栈帧就可以控制它，这就意味着我们对函数的控制可以很精确

'''
# 我们用dis可以产看字节码是什么样的
import dis
print(dis.dis(foo))
foo()
# 函数运行完成
print(frame.f_code.co_name)     # 拿到定义地方的函数的栈帧
caller_frame = frame.f_back     # 拿到调用地方的函数的栈帧
print(caller_frame.f_code.co_name)
print('*' * 80)
'''
以上过程我们可以看到，虽然foo函数运行完成，我们依然可以拿到函数的栈帧
这和静态语言不一样，静态语言函数调用的时候是一个栈的形式，函数调用完了，
整个栈就销毁了。
整个函数调用类似一个递归操作：
调用foo时，创建一个栈帧，调用bar时，又创建一个栈帧
栈帧对象：
f_back -> 该函数调用者的栈帧对象
f_code -> 该函数字节码对象PyCodeObject
'''
def gen_func():
    yield 1
    name = "fzk"
    age = 27
    yield 44
    birthday = "19920825"
    return "yuner"
'''
pyhton编译函数字节码的时候会发现yield关键词，他就知道这不是一个普通函数，
而是一个生成器函数，他会生成一个标记标记这个函数，当我们来调用这个函数的时候，
他就会返回一个生成器对象，这个生成器对象对pyFrameObject栈帧对象做了一个封装。
这个生成器对象是这样的：
[Heap memory 堆内存]
PyGenObject:
gi_frame
gi_code

gi_frame -> PyFrameObject（和上面的不太一样）: f_lasti（指向我们最近执行函数代码的字节码的位置） 和 f_locals（拿到最后一次yield前的所有赋值操作的字典）
gi_code -> PyCodeObject: gen_fn's bytecode
'''
gen = gen_func()
print(dis.dis(gen))
print('*'* 80)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
# next(gen)
# print(gen.gi_frame.f_lasti)
# print(gen.gi_frame.f_locals)

# list使用c语言实现的，看不到源码，而且做了很多优化，很多方法不允许我们覆盖
# 可以研究下UserList，所以写自己的list的时候可以继承UserList，我们可以自定义
from collections import UserList
'''
UserList 继承MutableSequence，
MutableSequence继承自Sequence
Sequence里面的__iter__方法源码如下：
def __iter__(self):
    i = 0
    try:
        while True:
            v = self[i]
            yield v
            i += 1
    except IndexError:
        return

i 记录了数组里的位置
self[i] 则会调用sequence的__getitem__方法
'''