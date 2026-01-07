#! -*- encoding=utf-8 -*-
# Python线程间通信 - 使用Queue实现线程安全的数据交换

'''
Queue（队列）线程同步机制：

1. 为什么使用Queue？
   - Queue内部已经实现了线程同步
   - 不需要手动加锁
   - 适合生产者-消费者模式

2. Queue的主要方法：
   - put(item)：放入元素
   - get()：获取元素
   - qsize()：返回队列大小
   - empty()：判断是否为空
   - full()：判断是否已满
   - task_done()：通知任务完成
   - join()：等待所有任务完成

3. Queue的线程安全性：
   - 内部使用deque实现
   - 在字节码层面已实现线程安全
   - 多个线程同时操作不会出错
'''

from queue import Queue
import time
import threading

print("=" * 50)
print("线程间通信 - Queue示例")
print("=" * 50)


print("""
代码组织技巧：

当项目中有多个线程需要通信时：
1. 可以把通信变量（如Queue）放在单独的py文件中
2. 其他模块import这个文件来使用
3. 当变量过多时方便维护
4. 注意：引入时引用文件，不要直接引入变量

示例：
    # config.py
    from queue import Queue
    task_queue = Queue()
    
    # worker.py
    import config
    config.task_queue.put(item)  # ✓ 正确
    
    # 错误做法：
    from config import task_queue  # ✗ 不推荐
""")

def get_detail_html(queue):
    """消费者 - 模拟爬取文章详情页
    
    Args:
        queue: 任务队列，存放待处理的URL
        
    Note:
        - 这是一个消费者线程
        - 从队列中不断获取URL并处理
        - queue.get()会阻塞直到有数据
    """
    while True:
        url = queue.get()  # 从队列获取URL（阻塞操作）
        print("""
Queue的主要方法详解：

1. 线程安全性：
   - queue本身是线程安全的
   - 多个线程同时get()/put()不会出错
   - 内部使用deque，在字节码层面已实现线程安全

2. qsize()：
   - 返回队列当前大小
   - 注意：返回值可能不准确（多线程环境下）

3. full()：
   - 判断队列是否已满
   - 如果满了，put()会阻塞直到有空间

4. empty()：
   - 判断队列是否为空
   - 如果空了，get()会阻塞直到有数据

5. put(item, block=True, timeout=None)：
   - item：要放入的元素
   - block：是否阻塞，默认True
   - timeout：超时时间，到时间后如果还没空位则抛异常

6. get(block=True, timeout=None)：
   - 参数同put()
   - 超时后如果还没数据则抛异常

7. put_nowait(item) / get_nowait()：
   - 非阻塞版本的put/get
   - 相当于put(item, False)和get(False)
   - 如果不能立即完成就抛异常
        """)
        print(f"get detail {url} started")
        time.sleep(2)
        print(f"get detail html end for {url}!")

def get_detail_url(queue):
    """生产者 - 模拟爬取文章列表页
    
    Args:
        queue: 任务队列，用于存放生产的URL
        
    Note:
        - 这是一个生产者线程
        - 不断生产URL并放入队列
        - queue.put()会阻塞直到队列有空间
    """
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put(f"http://projectsedu.com/{i}")
        print("get detail url end!!!")

print("""
线程通信方式总结：

1. 共享变量 + 锁：
   - 需要手动管理锁
   - 容易出错
   - 代码复杂度高

2. Queue队列（推荐）：
   - 内置线程安全
   - 代码简洁
   - 适合生产者-消费者模式
""")

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("开始生产者-消费者模式演示")
    print("=" * 50)
    
    # 创建任务队列
    detail_url_queue = Queue(maxsize=1000)
    # maxsize: 队列最大大小
    # 注意：queue过大会对内存有影响，需要根据实际情况设置
    
    # 创建生产者线程
    thread_detail_url = threading.Thread(
        target=get_detail_url,
        args=(detail_url_queue,)
    )
    
    # 创建10个消费者线程
    print("\n创建10个消费者线程...")
    for i in range(10):
        thread_detail_html = threading.Thread(
            target=get_detail_html,
            args=(detail_url_queue,)
        )
        thread_detail_html.start()
    
    start_time = time.time()
    
    # task_done() 和 join() 的使用：
    # detail_url_queue.task_done()  # 每完成一个任务调用一次
    # detail_url_queue.join()        # 等待所有task_done，否则不会退出
    
    thread_detail_url.start()
    thread_detail_url.join()
    
    print(f"\nlast time: {time.time()-start_time:.2f}s")
    
    print("""
    
    生产者-消费者模式总结：
    
    1. 模式特点：
       - 1个生产者线程：生产URL
       - 10个消费者线程：处理URL
       - 通过Queue进行通信
    
    2. 优势：
       - 解耦：生产和消费逻辑分离
       - 缓冲：Queue作为缓冲区
       - 灵活：可以调整消费者数量
    
    3. 适用场景：
       - 爬虫：爬取列表和详情
       - 消息处理：接收和处理消息
       - 任务调度：分发和执行任务
    """)
    
