#! -*- encoding=utf-8 -*-

#1、生成器不止可以产出值，还可以接收值
def gen_func():
    #1.可以产出值，2.可以接收值（调用方传递进来的值）
    html = yield "http://projectsedu.com"
    print(html)
    yield 2
    yield 3
    return "fzk"


#1.启动生成器的方式有两种，next(), send()

'''
在调用send发送非None值之前，我们必须启动一次生成器，
方式有两种：
1、gen.send(None)
2、next(gen)
send方法可以传递值进入生成器内部,
同时还可以重启生成器执行到下一个yield的位置
'''

if __name__ == "__main__":
    
    # 方法一
    gen = gen_func()
    url = next(gen)
    print(url)
    # download url
    html = "fzk"
    print(gen.send(html))
    '''
    send方法可以传递值进入生成器内部,
    同时还可以重启生成器执行到下一个yield的位置
    '''
    
    # 方法二
    gen = gen_func()
    url = gen.send(None)
    print(url)
    # download url
    html = "fzk"
    print(gen.send(html))

    '''
    def gen_func():
        yield 1
        yield 2
        yield 3
        return "fzk"
    '''
    # gen = gen_func()
    # # gen1 = gen_func()
    # # print(id(gen), id(gen1))  # 不是一个生成器
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen)k