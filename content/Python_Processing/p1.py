# -*- coding: utf-8 -*-
# @UpdateTime    : 2023/7/5 23:41
# @Author    : 27
# @File    : p1.py
# @Description   : Python多进程编程示例 - 演示multiprocessing模块的基本使用

import multiprocessing
import time


def myFunc(i):
    """简单的进程函数示例
    
    Args:
        i: 迭代次数
        
    Note:
        每个进程都会执行这个函数，打印从0到i-1的数字
    """
    print(f"calling myFunc from process n: {i}")
    for j in range(0, i):
        print(f"output from myFunc is: {j}")


def myFunc2():
    """带有进程名称和延时的进程函数
    
    演示如何获取和显示当前进程的名称。
    使用time.sleep()模拟耗时操作。
    
    Note:
        - multiprocessing.current_process().name 可获取当前进程名
        - 进程名可以自定义，也可以使用默认名称
    """
    name = multiprocessing.current_process().name
    print(f"Starting process name = {name}")
    time.sleep(3)  # 模拟耗时操作
    print(f"Exiting process name = {name}")


if __name__ == "__main__":
    print("=" * 50)
    print("Python多进程示例")
    print("=" * 50)
    
    # ==================== 示例1：基本进程使用 ====================
    # 以下代码演示如何创建和启动多个进程
    # for i in range(6):
    #     # 创建进程对象
    #     process = multiprocessing.Process(target=myFunc, args=(i,))
    #     process.start()  # 启动进程
    #     process.join()   # 等待进程结束
    #
    # 注意：这里用join()会导致进程串行执行，失去了并行的意义
    
    # ==================== 示例2：并行执行多个进程 ====================
    start = time.perf_counter()  # 记录开始时间
    
    # 创建两个进程，一个指定名称，一个使用默认名称
    process_with_name = multiprocessing.Process(
        name='myFunc2 process',  # 自定义进程名
        target=myFunc2
    )
    process_with_default_name = multiprocessing.Process(
        target=myFunc2  # 使用默认进程名（Process-N格式）
    )
    
    # 启动进程（并行执行）
    process_with_name.start()
    process_with_default_name.start()
    
    # 等待两个进程都结束
    process_with_name.join()
    process_with_default_name.join()
    
    end = time.perf_counter()  # 记录结束时间
    print(f"\nmyFunc2 running time: {end - start:.2f} seconds")
    
    print("\n" + "=" * 50)
    print("多进程执行完成")
    print("=" * 50)
    print("""
    多进程的重要概念：
    
    1. Process对象：
       - target: 要执行的函数
       - args: 传递给函数的参数
       - name: 进程名称（可选）
    
    2. start()：
       - 启动进程
       - 不会阻塞主程序
    
    3. join()：
       - 等待进程结束
       - 会阻塞主程序，直到进程执行完成
    
    4. 并行执行：
       - 先start()所有进程，再统一join()
       - 这样进程会并行执行
       - 本例中两个进程并行，总时间约3秒，而不是6秒
    """)

