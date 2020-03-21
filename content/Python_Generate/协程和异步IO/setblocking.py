#! -*- encoding=utf-8 -*-

# 通过非阻塞io实现http请求
import socket
from urllib.parse import urlparse

def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc       # 获取主域名 host
    path = url.path
    if path == "":
        path = "/" 
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)       
    '''
    设置这个blocking是会抛异常的：
    Traceback (most recent call last):
    File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/协程和异步IO/select_poll_epoll_io_test.py", line 38, in <module>
    get_url("http://www.baidu.com")
    File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/协程和异步IO/select_poll_epoll_io_test.py", line 20, in get_url
    client.connect((host, 80))         # 接收tuple
    BlockingIOError: [Errno 36] Operation now in progress
    
    虽然抛了异常，但是连接请求已经发出去了，那在下面我们用try来优化一下
    '''
    try:
        client.connect((host, 80))         # 接收tuple
    except BlockingIOError as e:
        pass
    '''
    这时候会抛另一个异常：
    OSError: [Errno 57] Socket is not connected
    套接字没有链接并且没有提供地址，发送或接受数据的请求没有被接受
    那我们继续优化下面：
    '''
    '''
    不停的询问链接是否建立好，需要while循环不停的去检查状态
    做计算任务或者再次发起其他的连接请求
    '''
    while True:
        try:
            # 发送数据，注意格式
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass
    '''
    我们再次发现这个异常：
    d = client.recv(1024)
    BlockingIOError: [Errno 35] Resource temporarily unavailable
    所以我们在这个位置再做优化
    '''
    # 为了防止取的数据不足
    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        '''
        这时候就会发现数据没有问题了
        '''
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

if __name__ == "__main__":
    get_url("http://www.baidu.com")


