# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/4/3 01:33
__author__ = '27'

import time, functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ", ".join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result

    return clocked


@functools.lru_cache()  # 必须像常规函数那样调用 lru_cache。这一行中有一对括 号:@functools.lru_cache()。这么做的原因是，lru_cache 可以接受配置参数，稍后说明。
@clock  # 这里叠放了装饰器:@lru_cache() 应用到 @clock 返回的函数上。(离函数近的先起作用)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))
