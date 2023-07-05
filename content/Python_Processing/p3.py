# -*- coding: utf-8 -*-
# @UpdateTime    : 2023/7/6 00:01
# @Author    : 27
# @File    : p3.py.py
import multiprocessing, time

def foo():
    print("start function")
    for i in range(0, 10):
        print("--->{}".format(i))
        time.sleep(1)
    print("Finished function")


if __name__ == "__main__":
    p = multiprocessing.Process(target=foo)
    print("Process before exection:", p, p.is_alive())
    p.start()
    print("Process running:", p, p.is_alive())
    p.terminate()
    print("Process terminated:", p, p.is_alive())
    p.join()
    print("Process joined:", p, p.is_alive())
    print("Process exit code:", p, p.exitcode)
    pass





