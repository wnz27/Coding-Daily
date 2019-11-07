#! -*- encoding:utf-8 -*-
from multiprocessing import Process, Queue, Manager, Pool, Pipe
# from queue import Queue  这个Queue不能用在多进程
import time

# def producer(queue):
#     queue.put("a")
#     time.sleep(2)

# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)

# 共享全局变量通信
# def producer(a):
#     a += 1
#     time.sleep(2)

# def consumer(a):
#     time.sleep(2)
#     print(a) 

# if __name__ == "__main__":
    # queue = Queue(10)
    # my_producer = Process(target=producer, args=(queue,))
    # my_consumer = Process(target=consumer, args=(queue,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()

'''
会报错误：
TypeError: cannot pickle '_thread.lock' object
我们发现这个queue在多进程中用不了
我们要用multiprocessing里提供的Queue
'''
    # queue = Queue(10)
    # my_producer = Process(target=producer, args=(queue,))
    # my_consumer = Process(target=consumer, args=(queue,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()

    # 共享全局变量通信
    # a = 1
    # my_producer = Process(target=producer, args=(a,))
    # my_consumer = Process(target=consumer, args=(a,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()
'''
输出还是1
说明没有被更改
结论：
共享全局变量是不能适用于多进程编程的，可以使用与多线程
想想fork，就知道多进程间的数据之间是隔离的
'''
# multiprocessing中的queue不能用于pool进程池

# def producer(queue):
#     queue.put("a")
#     time.sleep(2)

# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)

# if __name__ == "__main__":
    # multiprocessing中的queue不能用于pool进程池
    # queue = Queue(10)
    # pool = Pool(2)

    # pool.apply_async(producer, args=(queue,))
    # pool.apply_async(consumer, args=(queue,))

    # pool.close()
    # pool.join()
'''
可以看到没有输出，我们就可以知道，这个multiprocessing的queue是不能
用于pool进程池通信的
要想通信可以使用Manager，它里面有个queue是可以用来通信的：
'''
    # pool中的进程间通信需要使用manager中的queue
    # queue = Manager().Queue(10)
    # pool = Pool(2)

    # pool.apply_async(producer, args=(queue,))
    # pool.apply_async(consumer, args=(queue,))

    # pool.close()
    # pool.join()

# 通过pipe实现进程间通信
'''
pipe的性能是高于queue的，因为queue是为了做同步加了很多锁
做这些同步的时候会降低这些性能
'''
# def producer(pipe):
#     pipe.send("fzknimahai")

# def consumer(pipe):
#     print(pipe.recv())

# if __name__ == "__main__":
#     recevie_pipe, send_pipe = Pipe()
#     # pipe只能适用于两个进程

#     my_producer = Process(target=producer, args=(send_pipe,))
#     my_consumer = Process(target=consumer, args=(recevie_pipe,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

# 共享内存操作
def add_data(p_dict, key, value):
    p_dict[key] = value

if __name__ == "__main__":
    progress_dict = Manager().dict()    # 内存共享，下面两个进程同时写入
    first_progress = Process(target=add_data, args=(progress_dict, "fzk", 27,))
    second_progress = Process(target=add_data, args=(progress_dict, "fzk2", 18,))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()
    print(progress_dict)