#! -*- encoding=utf-8 -*-
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))         # 接收tuple

while True:
    re_data = input()
    client.send(re_data.encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf8"))

# client.send("fzkfzkfzk".encode("utf8"))           # 接收bytes类型的
# data = client.recv(1024)
# print(data.decode("utf8"))
# client.close()