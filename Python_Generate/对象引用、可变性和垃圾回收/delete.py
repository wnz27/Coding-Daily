#! -*- encoding=utf-8 -*-
# python h中垃圾回收的算法是采用引用计数
a = 1
b = a
# 这时候1这个创建出来的对象有两个变量指向它，它的计数器就是2
# 如果这时候使用
del a
# 那么a的引用计数就会减一，而不是把对象直接回收

a = object()
b = a
del a
print(b)
print(a)
# b可以打印出来，a打印不出来

# cpython2.0 不再局限于只是采用引用计数，有优化（题外话）
class A:
    def __del__(self):
        '''
        可以自己实现del的逻辑，比如需要释放某些资源
        '''
        pass
