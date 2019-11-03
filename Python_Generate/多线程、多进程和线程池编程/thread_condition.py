#! -*- encoding=utf-8 -*-
import threading

'''
单纯用Lock是不行的，因为进入线程的顺序是不确定的
'''

# 条件变量， 用于复杂的线程间同步

# 行不通
# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="小爱")
#         self.lock = lock
    
#     def run(self):
#         self.lock.acquire()
#         print("{} : 在！".format(self.name))
#         self.lock.release()

#         self.lock.acquire()
#         print("{} : 好啊！".format(self.name))
#         self.lock.release()

# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="天猫精灵")
#         self.lock = lock
    
#     def run(self):
#         self.lock.acquire()
#         print("{} : 小爱同学".format(self.name))
#         self.lock.release()

#         self.lock.acquire()
#         print("{} : 我们来对古诗吧".format(self.name))
#         self.lock.release()

# 通过condition完成协同读诗

from threading import Condition
class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond
    
    def run(self):
        with self.cond:
            self.cond.wait()
            print("{} : 在！".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{} : 好啊！".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{} : 君住长江尾".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{} : 共饮长江水".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{} : 此恨何时已".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{} : 定不负相思意".format(self.name))

class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond
    
    def run(self):
        with self.cond:
            print("{} : 小爱同学".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{} : 我们来对古诗吧？".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{} : 我住长江头".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{} : 日日思君不见君".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{} : 此水几时休".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{} : 只愿君心似我心".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == "__main__":
    # lock = threading.Lock()
    # xiaoai = XiaoAi(lock)
    # tianmao = TianMao(lock)

    # tianmao.start()
    # xiaoai.start()

    # xiaoai.join()
    # tianmao.join()

    cond = Condition()
    xiaoai1 = XiaoAi(cond)
    tianmao1 = TianMao(cond)
    
    # tianmao1.start()
    # xiaoai1.start()
    '''
    天猫先start的时候就会出现僵局
    只打印这个：天猫精灵 : 小爱同学
    并一直等待
    我们先start了天猫，那么天猫先执行了notify，之后小爱start，
    因为之前执行过notify了，所以小爱的wait一直都不会被唤醒，所以就僵住了
    所以我们要先启动先有wait的线程，这样再执行天猫的时候，notify就可以
    唤醒已经在等待的wait，这样就可以顺利进行了
    '''
    xiaoai1.start()
    tianmao1.start()

    '''
    在不用with语句的时候，我们也可以使用self.cond.acquire
    但是不能忘记把它释放掉，self.cond.release

    1、启动顺序很重要
    2、在调用with cond之后才能调用wait或者notify方法，
    如果没这样做，会抛错误：
    Exception in thread 小爱:
    Traceback (most recent call last):
        File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/threading.py", line 932, in _bootstrap_inner
    天猫精灵 : 小爱同学
        self.run()
        File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/多线程、多进程和线程池编程/thread_condition.py", line 49, in run
        self.cond.wait()
        File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/threading.py", line 294, in wait
        raise RuntimeError("cannot wait on un-acquired lock")
        RuntimeError: cannot wait on un-acquired lock
    3、condition 有两层锁，一把底层锁，会在线程调用了wait方法的时候释放掉，
    上层的锁会在每次调用wait的时候分配一把并放入到condition的等待队列中，
    等待notify方法的唤醒。
    Condition需要再研究下源码
    '''

    tianmao1.join()
    xiaoai1.join()

