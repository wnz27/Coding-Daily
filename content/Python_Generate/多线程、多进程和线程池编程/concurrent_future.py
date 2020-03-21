#! -*- encoding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future

'''
Future：未来对象，task的返回容器

'''

'''
相对底层的包，编写多线程和多进程的包
'''
# 线程池，为什么要用线程池
'''
类似以下需求
主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
当一个线程完成的时候我们主线程能立即知道
futures可以让多线程和多进程编码接口一致
'''
import time
# import psutil

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times

# 约定线程池的大小为cpu核数的两倍 （经验上的最佳实践）
excutor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中，submit有一个返回值, 立即返回，非阻塞的
# task1 = excutor.submit(get_html, (3))   # 后一个参数是函数要的参数
# task2 = excutor.submit(get_html, (2))

# # done方法用于判定某个人物是否完成
# print(task1.done())
# print(task2.cancel())
# '''
# 我们可以看到cancel返回的是false，因为我们线程池注册了2，所以可以同时执行两个任务，
# 那么提交进去基本是同时执行的，如果任务是执行中和执行完成，它是取消不了的，所以这里在被执行取消不了
# 如果我们把线程池允许的数量写1，那么只有task1进入线程池，这样task2还没有被执行，所以可以取消成功
# '''
# time.sleep(4)
# print(task1.done())
# # result是阻塞方法，得到执行的返回结果
# print(task1.result())

# 要获取已经成功的task的返回
urls = [1,2,4]
all_task = [excutor.submit(get_html, (url)) for url in urls]
# wait(all_task)
'''
wait用于阻塞，会等到all_task所有任务完成才执行下面语句
可以接收第二个参数，指定什么时候不等待
'''
wait(all_task, return_when=FIRST_COMPLETED) # 第一个任务执行完就不阻塞了
print("main")
# # as_completed 是一个生成器，会返回已经完成的任务
# for future in as_completed(all_task):
#     data = future.result()
#     print("get page {}".format(data))

# 通过executor获取已经完成的task的值, 这里不是excutor.submit返回值的类型，而是直接返回任务执行的结果
# for result in excutor.map(get_html, urls):
#     print(result)
#     print("get page {}".format(result))


