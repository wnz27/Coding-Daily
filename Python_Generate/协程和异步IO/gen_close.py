#! -*- encoding=utf-8 -*-
def gen_func():
    #1.可以产出值，2.可以接收值（调用方传递进来的值）
    try:
        yield "http://projectsedu.com"
    except GeneratorExit:
        raise StopIteration
        # pass
    yield 2
    yield 3
    return "fzk"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    # next(gen)
    '''
    这样的情况，try中的pass没有用，会抛异常：
    gen.close()
    RuntimeError: generator ignored GeneratorExit
    但是如果我们把try后面俩个yield语句去掉就会抛这个异常：
    next(gen)
    StopIteration
    相当于就跳过了try语句，pass起作用了


    以下我在mac和python3.65也不行，也是GeneratorExit的runtimeerror
    我们把pass改为StopIteration并把yield加上就不会抛GeneratorExit的异常了
    '''
    '''
    GeneratorExit继承自BaseException而不是Exception
    '''
    print("lalala")

    '''
    except 后面用Exception：
    next(gen)
    StopIteration
    '''
