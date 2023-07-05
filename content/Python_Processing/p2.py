# -*- coding: utf-8 -*-
# @UpdateTime    : 2023/7/5 23:45
# @Author    : 27
# @File    : p2.py

import multiprocessing, time

def foo():
    name = multiprocessing.current_process().name
    print("Starting {}".format(name))
    if name == "background_process":
        for i in range(0, 5):
            print("---> {}".format(i))
        time.sleep(1)
    else:
        for i in range(5, 10):
            print("---> {}".format(i))
        time.sleep(1)


if __name__ == "__main__":
    start = time.perf_counter()
    process_with_name = multiprocessing.Process(name='background_process', target=foo)
    process_with_name.daemon = True
    process_with_default_name = multiprocessing.Process(name='No_background_process', target=foo)
    process_with_default_name.daemon = False
    process_with_name.start()
    process_with_default_name.start()
    process_with_name.join()
    process_with_default_name.join()
    end = time.perf_counter()
    print(f"func2 running time {end - start}")
    pass
