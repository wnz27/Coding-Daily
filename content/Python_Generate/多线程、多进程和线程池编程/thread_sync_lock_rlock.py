#! -*- encoding=utf-8 -*-
# Python线程同步 - Lock和RLock的使用和区别

'''
线程同步问题详解：

1. 为什么需要锁？
   - 多线程访问共享资源时可能出现竞争
   - 导致数据不一致性问题
   - 需要锁来保证原子性操作

2. Lock（普通锁）：
   - 最基本的线程同步原语
   - acquire()：获取锁
   - release()：释放锁
   - 同一线程不能连续两次acquire（会死锁）

3. RLock（可重入锁）：
   - 同一线程可以多次acquire
   - acquire和release次数必须相等
   - 避免嵌套调用时的死锁

4. 锁的问题：
   - 获取和释放锁需要时间，影响性能
   - 可能引起死锁（哲学家吃饭问题）
   - 需要谨慎使用，避免过度使用
'''

import threading
from threading import Lock, RLock

print("=" * 50)
print("Lock 和 RLock 的区别")
print("=" * 50)
print("""
RLock（可重入锁）的用途：

问题场景：
    lock.acquire()
    lock.acquire()  # 死锁！同一线程不能连续两次获取Lock

解决方案：使用RLock
    rlock.acquire()
    rlock.acquire()  # 可以！RLock允许同一线程多次获取
    rlock.release()
    rlock.release()  # 注意：acquire和release次数必须相等

关键点：
- acquire()的次数必须等于release()的次数
- 常用于递归调用或嵌套调用的场景
- 避免因嵌套锁导致的死锁问题
""")

print("""
锁的主要问题：

1. 性能影响：
   - 获取锁和释放锁都需要时间
   - 会降低程序的并发性能
   - 过度使用锁可能导致性能下降

2. 死锁（Deadlock）：
   - 哲学家吃饭问题：每个人都持有一只筷子，等待另一只
   - 多个线程互相等待对方释放资源
   - 需要谨慎设计，避免循环等待

3. 避免死锁的方法：
   - 始终按相同顺序获取多个锁
   - 使用超时机制
   - 使用死锁检测算法
   - 尽量减少锁的使用
""")

# 全局变量
total = 0
lock = Lock()      # 普通锁
rLock = RLock()    # 可重入锁
def adda():
    """增加操作 - 演示RLock的使用
    
    注意：
    1. 这里演示了RLock可以连续获取两次
    2. 必须调用两次release()来释放
    3. 如果是Lock，第二次acquire()就会死锁
    """
    global total
    global rLock
    for i in range(10, 20):
        # RLock允许同一线程多次获取锁
        rLock.acquire()  # 第一次获取
        rLock.acquire()  # 第二次获取（如果是Lock就会死锁）
        total += 1
        print(f"adda: {i}, total: {total}")
        rLock.release()  # 第一次释放
        rLock.release()  # 第二次释放

def desc():
    """减少操作 - 演示普通Lock的使用"""
    global total
    global lock
    for i in range(10):
        lock.acquire()
        total -= 1
        print(f"desc: {i}, total: {total}")
        lock.release()

# 创建和启动线程
print("\n开始执行线程...")
thread1 = threading.Thread(target=adda)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()
print(f"\n最终结果: {total}")

print("\n" + "=" * 50)
print("为什么需要锁？Python字节码分析")
print("=" * 50)

def add1(a):
    """简单的加法操作"""
    a += 1
    return a

print("""
Python字节码分析：

a += 1 这条简单的语句对应的字节码：

    LOAD_FAST                0 (a)     # 1. 加载变量 a
    LOAD_CONST               1 (1)     # 2. 加载常数 1
    INPLACE_ADD                        # 3. 执行加法
    STORE_FAST               0 (a)     # 4. 将结果存回 a
    LOAD_CONST               0 (None)  # 5. 加载None
    RETURN_VALUE                       # 6. 返回

线程安全问题：
1. Python在执行任意一条字节码时，GIL都可能被释放
2. 当GIL被释放时，可能切换到另一个线程
3. 如果两个线程同时修改同一个变量，会导致数据不一致

例子：
线程1执行到第3步（INPLACE_ADD）时，GIL被释放
线程2开始执行，也读取了a的值，并计算
两个线程的计算结果可能互相覆盖，导致数据丢失

解决方案：使用锁来保证原子性
锁确保了在一个线程完成整个操作之前，其他线程不能介入。
""")

# 使用dis模块查看字节码（可选）
# import dis
# print("\nadd1函数的字节码：")
# print(dis.dis(add1))

def desc1(a):
    """简单的减法操作"""
    a -= 1
    return a

print("""
总结：

1. Lock和RLock的选择：
   - 一般情况使用Lock，性能更好
   - 需要嵌套锁时使用RLock
   - RLock略有性能损耗，但更安全

2. 使用锁的最佳实践：
   - 尽量减小锁的粒度（锁住最少的代码）
   - 避免在锁内部执行IO操作
   - 使用with语句自动管理锁
   - 考虑使用更高级的同步原语（如Queue、Condition）

3. 替代方案：
   - 使用Queue进行线程间通信
   - 使用线程本地存储（threading.local）
   - 使用进程代替线程（避免GIL）
   - 使用异步编程（asyncio）
""")
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