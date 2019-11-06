#! -*- encoding:utf-8 -*-
# 多线程
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED, as_completed, wait
# 多进程，与多线程完全一样的用法
from concurrent.futures import ProcessPoolExecutor
import time

# 多进程编程
'''
因为有一把GIL锁的存在，所以pyhton 的多线程无法充分利用cpu多核的优势
对于某些耗cpu的操作，我们用多线程编程就无法达到一个并行的操作
所以python中也提供了多进程编程，我们就可以利用多个cpu并发的特性去提高我们的运行效率
耗cpu的操作，用多进程编程
对于io操作，瓶颈不在于cpu，使用多线程编程
因为对于操作系统来说进程切换代价高于线程切换
操作系统去调度线程会比进程切换要容易，当我们同时运行几十个线程，对于操作系统来说它的切换性能是比进程高的
从切换上看，虽然差异不大，但是操作系统运行进程内存耗费很高，是绝对比线程高的，对于操作系统来说，
我们能开的线程数是要比进程数高的，就比如操作系统同时跑60个线程很轻松，但是跑60个进程就会很吃力了，
他就会耗费更多的内存，所以我们很多时候用的就是多线程，况且在很多时候，我们多线程稳定性是要比多进程高的
'''

'''
 1、对于耗费cpu的操作，计算都是耗费cpu的，图形处理，人工智能机器学的算法，
 挖矿（非常耗费cpu，耗费到cpu满足不了计算）这也是显卡流行的原因，因为gpu运算速度是高于cpu的
 多进程优于多线程
'''
def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

# 2、IO操作模拟函数
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    # 耗费cpu测试
    # # 多线程
    # with ThreadPoolExecutor(3) as executor:
    #     # 要获取已经成功的task的返回
    #     all_task = [executor.submit(fib, (num)) for num in range(25,40)]
    #     start_time = time.time()
    #     # as_completed 是一个生成器，会返回已经完成的任务
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("exe result {}".format(data))
    #     print("last time is:{}".format(time.time()-start_time))
    
    # # 多进程
    # with ProcessPoolExecutor(3) as executor:
    #     # 要获取已经成功的task的返回
    #     all_task = [executor.submit(fib, (num)) for num in range(25,40)]
    #     start_time = time.time()
    #     # as_completed 是一个生成器，会返回已经完成的任务
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("exe result {}".format(data))
    #     print("last time is:{}".format(time.time()-start_time))
    
    # 对于io操作来说，多线程优于多进程
    # 多线程
    with ThreadPoolExecutor(3) as executor:
        # 要获取已经成功的task的返回
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        # as_completed 是一个生成器，会返回已经完成的任务
        for future in as_completed(all_task):
            data = future.result()
            print("exe result {}".format(data))
        print("last time is:{}".format(time.time()-start_time))
    
    # 多进程
    with ProcessPoolExecutor(3) as executor:
        # 要获取已经成功的task的返回
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        # as_completed 是一个生成器，会返回已经完成的任务
        for future in as_completed(all_task):
            data = future.result()
            print("exe result {}".format(data))
        print("last time is:{}".format(time.time()-start_time))


