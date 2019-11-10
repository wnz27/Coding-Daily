#! -*- encoding=utf-8 -*-

# 通过非阻塞io实现http请求
# select + 回调 + 事件循环
'''
好处！！！！
并发性高
现在使用单线程
'''

import socket
from urllib.parse import urlparse
import select
from selectors import DefaultSelector, EVENT_READ,EVENT_WRITE 
'''
selectore源码也是用select实现的，并且包装的更加好用
所以基本使用selector即可，
并且它可以根据平台去选择，select在windows，然后linux是epoll，
至于选择poll还是epoll，都是自己实现好的
还有一个注册机制
'''

# 使用select完成http请求，try|except参考setblock文件的过长，《通过非阻塞io实现http请求》这个文件

selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False

class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)
    
    def readable(self, key):
        '''
        d = self.client.recv(1024)
        会报错：
        BlockingIOError: [Errno 35] Resource temporarily unavailable
        解决：
        '''
        d = self.client.recv(1024)
        if d:
            print(d)
            self.data += d
        else:
            selector.unregister(key.fd) # 如果空说明读完了
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self,url):
        # 通过socket请求html
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc       # 获取主域名 host
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/" 
        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))         # 接收tuple
        except BlockingIOError as e:
            pass

        # 注册到selector当中,fileno是文件描述符
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

def loop():
    # 事件循环，不停地请求socket的状态并调用对应的回调函数
    # 1、select本身是不支持register模式
    # 2、socket状态变化以后的回调是由程序员完成的
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)
    # 回调+事件循环+select（poll/epoll）

if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()

