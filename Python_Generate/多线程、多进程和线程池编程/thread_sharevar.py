#! -*- encoding=utf-8 -*-
# 线程间通信
import time
import threading

detail_url_list = []
'''
可以把通信变量放在另一个py文件里，引用进来使用。
当变量过多的时候方便维护
但是引入的时候引用文件，不要引入变量
'''

def get_detail_html(detail_url_list):
    # 模拟爬去文章详情页
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()     # 线程不安全
            # for url in detail_url_list:
            print("get detail {url}started".format(url))
            time.sleep(2)
            print("get detail html end!")

def get_detail_url(detail_url_list):
    # 模拟爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end!!!")

'''
1、线程通信方式 - 共享变量
用一个全局变量来通信



'''

if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list, ))
    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_list, ))
        thread_detail_html.start()
    
