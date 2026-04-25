"""
案例：文件上传案例，客户端代码
"""
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 10086))
# 关联目的地文件
with open('./data/客户端/绕口令.txt', 'rb') as src_f:
    while True:
        data = src_f.read(8192)
        client_socket.send(data)
        if len(data) == 0:
            break

client_socket.close()
