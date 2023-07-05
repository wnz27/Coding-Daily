# -*- coding: utf-8 -*-
# @UpdateTime    : 2023/7/5 23:41
# @Author    : 27
# @File    : p1.py.py

import multiprocessing, time


def myFunc(i):
    print("calling myFunc from process n: %s" % i)
    for j in range(0, i):
        print("out from myFunc is: %s" % j)


def myFunc2():
    name = multiprocessing.current_process().name
    print("Starting process name = {}".format(name))
    time.sleep(3)
    print("Exiting process name = {}".format(name))


if __name__ == "__main__":
    print(123)

    # myFunc
    # for i in range(6):
    #     process = multiprocessing.Process(target=myFunc, args=(i,))
    #     process.start()
    #     process.join()

    # myFunc2
    start = time.perf_counter()
    process_with_name = multiprocessing.Process(name='myFunc2 process', target=myFunc2)
    process_with_default_name = multiprocessing.Process(target=myFunc2)
    process_with_name.start()
    process_with_default_name.start()
    process_with_name.join()
    process_with_default_name.join()
    end = time.perf_counter()
    print(f"func2 running time {end - start}")
    pass

