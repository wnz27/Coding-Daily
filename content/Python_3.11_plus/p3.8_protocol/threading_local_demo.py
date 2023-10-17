'''
Author: 27
LastEditors: 27
Date: 2023-10-16 17:14:57
LastEditTime: 2023-10-16 17:24:29
FilePath: /Coding-Daily/content/Python_3.11_plus/p3.8_protocol/threading_local_demo.py
description: type some description
'''
from threading import local
# from typing import List


class MyLocal(local):
    number = 3333
    def __init__(self, group_id: str, **kw):
        self.__dict__.update(kw)
        self.group_id = group_id


def f():
    items = sorted(mydata.__dict__.items())
    log.append(items)
    mydata.number = 11
    log.append(mydata.number)


if __name__ == "__main__":
    group_id = 'group_id_curr'
    mydata = MyLocal(group_id=group_id, color='red')
    import threading
    print(mydata.group_id)
    print(mydata.color, mydata.number)
    # del mydata.color
    log = []
    t = threading.Thread(target=f)
    t.start()
    t.join()
    print(log)
    # print(mydata.color)

