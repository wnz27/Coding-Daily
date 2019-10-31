#! -*- encoding=utf-8 -*-

# 生成器函数，函数里只要有yield关键字
def gen_func():
    yield 1
    yield 2

# 传统递归做法
def fib(index):
    if index <= 0:
        raise IndexError
    elif index <= 2:
        return 1
    else:
        return fib(index-2) + fib(index-1)

# 返回列表
def fib2(index):
    re_list = []
    n,a,b = 0,0,1
    while n<index:
        re_list.append(b)
        a,b = b, a+b
        n += 1
    return re_list

# 生成器做法
def fib_yield(index):
    n,a,b = 0,0,1
    while n<index:
        yield b
        a,b = b, a+b
        n += 1

for data in fib_yield(10):
    print(data)

# 斐波那契 1 1 2 3 5 8
# yield为惰性求值， 延迟求值提供了可能
# 惰性求值，计算的时候才产生值，性能大大提高

def func():
    return 1

if __name__ == "__main__":
    print("*" * 80)
    gen = gen_func()
    for value in gen:
        print(value)
    print("*" * 80)
    re = func()
    print(gen)
    '''
    输出：<generator object gen_func at 0x10652d430>
    我们发现返回的是一个生成器对象
    这个对象产生在pyhton编译字节码的时候就产生了。
    python运行之前会将代码变成字节码，
    编译的时候会发现函数里面是yield，所以就会把这个函数生成个对象
    这个对象怎么才能访问这里面的值呢？用到迭代器。
    生成器对象事实上实现了迭代器协议的。
    '''
    print(re)
    '''
    输出：1
    这里就是返回的一个值1
    '''
    print("*" * 80)
    print(fib(10))
    print(fib2(10))
    print("*" * 80)
    print(fib_yield(10))
    print("*" * 80)
    print("*" * 80)
    import dis
    lalala = fib_yield(10)
    print(dis.dis(lalala))
    print("*" * 80)
    print(next(lalala))
    print(lalala.gi_frame.f_lasti)
    print("*" * 80)
    print(next(lalala))
    print(lalala.gi_frame.f_lasti)
    print("*" * 80)
    print(next(lalala))
    print(lalala.gi_frame.f_lasti)
    print("*" * 80)
    print(next(lalala))
    print(lalala.gi_frame.f_lasti)
    print("*" * 80)
    print(next(lalala))
    print(lalala.gi_frame.f_lasti)
    print("*" * 80)
    print(next(lalala))
    print(lalala.gi_frame.f_lasti)
    print("*" * 80)
    print(next(lalala))
    print(lalala.gi_frame.f_lasti)
    print("*" * 80)
    print(next(lalala))
    print(lalala.gi_frame.f_lasti)
    print("*" * 80)
    print(next(lalala))
    print(lalala.gi_frame.f_lasti)
    print("*" * 80)
    print(next(lalala))
    print(lalala.gi_frame.f_lasti)
#################################################################
# 区别底下输出看看规律：
    print("*" * 80)
    print("*" * 80)
    print(next(fib_yield(10)))
    print("*" * 80)
    print(next(fib_yield(10)))
    print("*" * 80)
    print(next(fib_yield(10)))
    print("*" * 80)
    print(next(fib_yield(10)))
    print("*" * 80)
    print(next(fib_yield(10)))
    print("*" * 80)
    print(next(fib_yield(10)))
    print("*" * 80)
    print(next(fib_yield(10)))
    print("*" * 80)
    print(next(fib_yield(10)))
    print("*" * 80)
    print(next(fib_yield(10)))
    print("*" * 80)
    print(next(fib_yield(10)))