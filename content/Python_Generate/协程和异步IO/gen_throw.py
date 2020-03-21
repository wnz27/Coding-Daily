#! -*- encoding=utf-8 -*-
def gen_func():
    #1.可以产出值，2.可以接收值（调用方传递进来的值）
    try:
        yield "http://projectsedu.com"
    except Exception as e:
        pass
    yield 2
    yield 3
    return "fzk"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "download error")
    '''
    运行结果：
    yield "http://projectsedu.com"
    Exception: download error
    说明这里抛出的是前一个地方的异常
    '''
    print(next(gen))
    '''
    输出：
    http://projectsedu.com
    3
    '''
    gen.throw(Exception, "download error")
    '''
    输出：
    yield 3
    Exception: download error
    在yield3的位置抛出异常
    '''

    
   
