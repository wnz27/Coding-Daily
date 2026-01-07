#! -*- encoding=utf-8 -*-
# Python生成器函数详解 - 演示yield关键字的使用和生成器的优势

# ==================== 基本生成器 ====================

def gen_func():
    """简单的生成器函数示例
    
    只要函数中包含yield关键字，该函数就是生成器函数。
    调用生成器函数会返回一个生成器对象，而不是执行函数体。
    
    Yields:
        int: 依次生戉10、1、2
    """
    yield 1
    yield 2

# ==================== 斐波那契数列的三种实现 ====================

def fib(index):
    """传统递归方式计算斐波那契数列
    
    Args:
        index: 要计算第几个斐波那契数
        
    Returns:
        int: 第 index 个斐波那契数
        
    Raises:
        IndexError: 当 index <= 0 时
        
    Note:
        递归方式的缺点：
        - 有大量的重复计算
        - 时间复杂度是O(2^n)，效率很低
        - 可能导致栈溢出
    """
    if index <= 0:
        raise IndexError("索引必须大于0")
    elif index <= 2:
        return 1
    else:
        return fib(index-2) + fib(index-1)

def fib2(index):
    """返回列表的方式计算斐波那契数列
    
    Args:
        index: 计算前 index 个斐波那契数
        
    Returns:
        list: 包含前 index 个斐波那契数的列表
        
    Note:
        优点：
        - 时间复杂度O(n)，比递归高效
        - 逻辑清晰，易于理解
        
        缺点：
        - 需要一次性分配所有内存
        - 内存占用高，对于大数据量不友好
        - 必须等全部计算完才能使用
    """
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a+b
        n += 1
    return re_list

def fib_yield(index):
    """使用生成器方式计算斐波那契数列
    
    Args:
        index: 生成前 index 个斐波那契数
        
    Yields:
        int: 依次生成每个斐波那契数
        
    Note:
        生成器的优势：
        1. 惰性求值（Lazy Evaluation）：
           - 只有在需要时才计算下一个值
           - 不需要一次性生成所有结果
           
        2. 内存效率高：
           - 不需要像列表那样存储所有值
           - 任何时刻只占用当前值的内存
           
        3. 支持无限序列：
           - 可以生成无限长序列
           - 用户可以随时停止迭代
           
        4. 性能提升：
           - 对于大数据集，性能大大提高
           - 适合流式处理
    """
    n, a, b = 0, 0, 1
    while n < index:
        yield b  # 使用yield返回当前值，并暂停执行
        a, b = b, a+b
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