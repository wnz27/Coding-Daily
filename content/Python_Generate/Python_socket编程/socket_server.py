#! -*- encoding=utf-8 -*-
import socket
import threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))         # 接受一个tuple！！！！！(地址, 端口)
server.listen()

def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        data_value = data.decode("utf8")
        if data_value == "exit":
            break
        print(data.decode("utf8"))
        re_data = input()
        sock.send(re_data.encode("utf8"))
    sock.close()
        
# 获取从客户端发送的数据
# 一次获取1K的数据
while True:
    sock, addr = server.accept()
    # 用线程去处理新接收的连接（用户）
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))      # 传的函数名称，千万不要穿函数调用！
    client_thread.start()
    data = sock.recv(1024)
    print(data.decode("utf8"))
    re_data = input()
    sock.send(re_data.encode("utf8"))

# data = sock.recv(1024)        # 单位是字节, data 是一个bytes类型
# print(data.decode("utf8"))
# sock.send("hello {}".format(data.decode("utf8")).encode("utf8"))
'''
AF_INET: AddressFamily          IPv4
AF_INET6: AddressFamily         IPv6
SOCK_STREAM: SocketKind         TCP
SOCK_DGRAM: SocketKind          UDP
'''
# server.close()
# sock.close()