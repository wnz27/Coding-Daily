#! -*- encoding=utf-8 -*-

### 遇见的问题：
'''
回调模式编码复杂度高
同步编程的并发性不高
多线程编程需要线程间同步，我们使用lock，但是lcok会降低并发性能
所以我们想要解决就要
- 1、采用同步的方式去编写异步的代码
- 2、使用单线程去切换任务
    - 1、线程是由操作系统切换的，单线程切换意味着我们需要程序员自己去调度任务
    - 2、不再需要锁，因为我们是在单线程内切换，并发性就会高，还有一点是创建一个线程对于操作系统来说也是有较大消耗的，并且切换也会较慢，如果我们在单线程内切换函数，这个性能肯定远远高于线程之间的切换，这样肯定并发性更高。
'''

'''说明用代码，无法运行
def get_url(url):
    # do something 1，这里耗cpu
    html = get_html(url)    # 这里耗io
    # parse html
    urls = parse_url(html)
def get_url2():
    # do something 1，这里耗cpu
    html = get_html(url)    # 这里耗io
    # parse html
    urls = parse_url(html)
'''
'''
# 传统函数调用过程 A->B->C
如果是上面的情况，那么函数是在栈里的，那么也就是说我们到get_html之后
阻塞在那了等待结果顺着完成，而我们想要的情况是你这个去等数据了把函数暂停
我们就再去找另一个函数继续获取新的url。
所以指向了我们的需求：
'''
'''
我们需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的继续执行

这就出现了协程-->有多个入口的函数或者说叫-->可以暂停的函数
可以暂停的函数（并且可以向暂停的地方传入值）
'''


