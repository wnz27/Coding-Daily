#! -*- encoding=utf-8 -*-
import dis      # 看字节码
# def add(a):
#     a = a + 1
#     return a

# print(dis.dis(add))

import threading
from threading import Lock, RLock
'''
RLock 可重入的锁，为了避免出现下面这种情况死锁
lock.acquire()
lock.acquire()
使用RLock在同一个线程里面可以连续多次调用acquire，
一定要注意acquire的次数要和release的次数相等
'''
'''
锁的问题是获取锁和释放锁都需要时间
1、用锁会影响性能
2、锁会引起死锁
死锁：哲学家吃饭
各自持有资源等对方释放 
'''

total = 0
lock = Lock()
rLock = RLock()
def adda():
    # 1、do something1
    # 2、io操作
    # 3、do something3
    global total
    global rLock
    for i in range(10, 20):
        rLock.acquire()
        rLock.acquire()
        total += 1
        print(i)
        rLock.release()
        rLock.release()

def desc():
    global total
    global lock
    for i in range(10):
        lock.acquire()
        total -= 1
        print(i)
        lock.release()

thread1 = threading.Thread(target=adda)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)

def add1(a):
    a += 1
'''
字节码解读：
32           0 LOAD_FAST                0 (a)
              2 LOAD_CONST               1 (1)
              4 INPLACE_ADD
              6 STORE_FAST               0 (a)
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
None
1、 load a
2、 load 1
3、 +
4、 把加的结果赋值给a赋值给a
因为执行任意一行字节码的时候gil都有可能被释放并被切换到另一个线程的
'''

def desc1(a):
    a -= 1
'''
字节码解读
35           0 LOAD_FAST                0 (a)
              2 LOAD_CONST               1 (1)
              4 INPLACE_SUBTRACT
              6 STORE_FAST               0 (a)
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
None
1、 load a
2、 load 1
3、 -
4、 把减的结果赋值给a赋值给a
因为执行任意一行字节码的时候gil都有可能被释放并被切换到另一个线程的
'''
'''
所以基于这个gil释放的解读，我们可以理解到如果两个方法的字节码步骤来回切换
就会出现a的数值不统一的问题。
电商网站很多人同时购买时候库存的减少可能出现上述的问题
'''

# print(dis.dis(add1))
# print(dis.dis(desc1))

'''
打印的值不稳定说明gil锁是会释放的，有可能是根据执行字节码行数？再或者是时间片来划分？
'''