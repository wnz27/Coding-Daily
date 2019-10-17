#! -*- encoding=utf-8 -*-
import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield {}
    print("file end")

with file_open("27.txt") as f_opened:
    print("file processing")

'''
输出：
file open
file processing
file end
所以利用了生成器yield以更简洁的方式做出了上下文管理的效果
'''