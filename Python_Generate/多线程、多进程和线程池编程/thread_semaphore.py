#! -*- encoding:utf-8 -*-
'''
semaphore 适用于控制进入数量的锁
文件、读、写，写一般只是用于一个线程的写，读可以允许有多个
# 做爬虫，限制爬虫的并发数，限制爬虫进入一段代码的数量
'''
import threading
import time

class HtmlSpider(threading.Thread):
    def __init__(self,url,sem):
        super().__init__()
        self.url = url
        self.sem = sem
    def run(self):
        time.sleep(2)
        print('got html text success')
        self.sem.release()

class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem
    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider('https://www.baidu.com/{}'.format(i), self.sem)
            html_thread.start()


if __name__ == "__main__":
    sem = threading.Semaphore(3)
    '''
    semaphore源码是利用condition来实现的
    Queue的源码也是使用了很多condition来实现的，所以说queue是线程安全的
    '''
    url_producer = UrlProducer(sem)
    url_producer.start()


