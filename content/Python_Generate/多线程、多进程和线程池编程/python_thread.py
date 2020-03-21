#! -*- encoding=utf-8 -*-
'''
操作系统能调度的最小单元是线程，以前是进程，但是因为进程对系统资源消耗很大，所以后期演变出了线程
线程事实上依赖于进程的
'''
'''
对于以io操作为主的应用来说，多线程和多进程性能差别不大。
对于操作系统来说，线程调度比进程调度要更加轻量级
'''
'''
多线程编程的方式
1、通过Thread类实例化
2、通过继承Thread来实现多线程
'''

import time
import threading
# 1、通过Thread类实例化
# def get_detail_html(url):
#     print("get detail html started")
#     time.sleep(2)
#     print("get detail html end!")

# def get_detail_url(url):
#     print("get detail url started")
#     time.sleep(4)
#     print("get detail url end!!!")

# if __name__ == "__main__":
#     thread1 = threading.Thread(target=get_detail_html, args=("",))
#     thread2 = threading.Thread(target=get_detail_url, args=("",))
#     # thread1.setDaemon(True)
#     thread2.setDaemon(True)
#     # setDaemon 守护线程，当我们的主线程退出之后，会直接把这些线程结束掉
#     start_time = time.time()
#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()
#     # join方法会阻塞线程，等待线程完成再去执行主线程
#     # 当主线程退出的手，子线程kill掉
#     print("last time: {}".format(time.time()-start_time))
#     # 可以观察到用join时候last time是两个线程最大的时间，也可以说明两个线程是并发进行的。

# 2、通过继承Thread来实现多线程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end!")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end!!!")      

'''
继承Thread的方法无疑自由度更高，我们可以自定义复杂的逻辑在run方法里去实现要在这个线程做的事情
'''

if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")

    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    # join方法会阻塞线程，等待线程完成再去执行主线程
    print("last time: {}".format(time.time()-start_time))
