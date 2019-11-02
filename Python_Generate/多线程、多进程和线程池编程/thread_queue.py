#! -*- encoding=utf-8 -*-
# 通过queue的方式进行线程同步
from queue import Queue

# 线程间通信
import time
import threading


'''
可以把通信变量放在另一个py文件里，引用进来使用。
当变量过多的时候方便维护
但是引入的时候引用文件，不要引入变量
'''

def get_detail_html(queue):
    # 模拟爬去文章详情页
    while True:
        url = queue.get()          
        '''
        queue本身是一个线程安全的, 多个线程对queue进行get操作的时候不会出现错误
        内部实现里使用了deque，这个deque在字节码层面已经实现了线程安全
        qsize,返回队列长度
        full， 判断队列已满，如果满了那么put方法是会阻塞在那里的，直到有空闲空间为止，才能成功
        emoty，判断队列是否为空
        这些方法都是线程安全的
        put_nowait
        get_nowait 这俩是异步方法
        put方法：
        def put(self,item, block=True, timeout=None)
        block是否阻塞，默认是阻塞的，timeout设置的话是到这个时间之后还没有空位那么就直接返回
        '''
        # for url in detail_url_list:
        print("get detail {url}started".format(url=url))
        time.sleep(2)
        print("get detail html end!")

def get_detail_url(queue):
    # 模拟爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end!!!")

'''
2、线程通信方式 - 队列
'''

if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)      # queue过大会对内存有影响
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue, ))
    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_queue, ))
        thread_detail_html.start()
    
    start_time = time.time()
    # detail_url_queue.task_done()
    # detail_url_queue.join()     # 等待task_done,否则是不会退出的
    thread_detail_url.start()
    thread_detail_url.join()
    print("last time: {}".format(time.time()-start_time))
    
