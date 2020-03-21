#! -*- encoding:utf-8 -*-
import os
import time
# fork 只能用于linux/unix中
# pid = os.fork()
# print("fzk")
# if pid == 0:
#     print('子进程 {}, 父进程是：{}'.format(os.getpid(), os.getppid()))
# else:
#     print('我是父进程：{}'.format(pid))

# time.sleep(2)
'''
打印输出是：
fzk
我是父进程：63299
fzk
子进程 63299, 父进程是：63298
解释：
fork会生成一个子进程，生成完之后，依然会按照代码执行当前进程（父进程）
然后fork的子进程会把父进程的所有数据和代码原样拷贝一份到自己里面
并且运行一遍，在子进程运行的时候它的pid是等于0的
由此可见子父进程之间数据是完全隔离的
sleep的好处是
如果我们没有sleep，那么父进程会直接执行完退出，那么这个时候
子进程并没有执行完，就无法退出，sleep了之后，等子进程执行完，
父进程还没结束，然后父进程结束之后也就会把子进程kill掉
'''

from concurrent.futures import ProcessPoolExecutor
import multiprocessing

# 多进程编程
def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n

# 也同样可以继承
# class MyProgress(multiprocessing.Process):
#     def run(self):


if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print(progress.pid)
    # print("main progress end")

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))

    # 等待所有任务完成
    '''
    pool.join()
    print(result.get())
    这样会出错：
    Traceback (most recent call last):
    File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/多线程、多进程和线程池编程/multiprocessing_test.py", line 58, in <module>
    pool.join()
    File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/multiprocessing/pool.py", line 661, in join
    raise ValueError("Pool is still running")
    ValueError: Pool is still running
    '''
    # 我们要这么写
    '''
    pool.close()
    pool.join()
    print(result.get())
    '''
    '''
    我们要先把pool关闭不接受任务，再去停止
    '''

    # imap，按照添加顺序
    # for result in pool.imap(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))

    # imap_unordered,按照完成顺序
    for result in pool.imap_unordered(get_html, [1,5,3]):
        print("{} sleep success".format(result))

    pool.close()
    pool.join()
