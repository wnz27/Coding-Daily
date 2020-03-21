#! -*- encoding=utf-8 -*-
'''
GIL: global interpreter lock   全局解释器锁（基于cpython）
python中一个线程对应于c语言中的一个线程
gil 使得同一时刻只有一个线程在一个cpu上执行字节码,无法将多个线程映射到多个cpu上

gil会根据执行的字节码行数以及时间片释放gil
gil在遇见io操作的时候也会主动释放，会把执行权给其他的线程
这个特性使得我们的python的多线程，在io操作频繁的情况下，它实际上是非常适用的。
所以gil在我们python多线程编程的时候非常适用
'''
import dis
# def add(a):
#     a = a + 1
#     return a

# print(dis.dis(add))

import threading

total = 0

def adda():
    # 1、do something1
    # 2、io操作
    # 3、do something3
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

thread1 = threading.Thread(target=adda)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)

'''
打印的值不稳定说明gil锁是会释放的，有可能是根据执行字节码行数？再或者是时间片来划分？
'''