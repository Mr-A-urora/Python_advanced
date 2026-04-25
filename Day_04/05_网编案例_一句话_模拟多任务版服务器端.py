"""
案例：网编入门案例，服务器端给客户端发送消息，客户端给出回执信息

服务器端开发流程：
    1. 创建服务器端Socket对象
    2. 绑定IP地址和端口号
    3. 设置最大监听数
    4. 等待客户端申请建立链接
    5. 给客户端发送消息
    6. 接收客户端的信息并打印
    7. 释放资源

细节：客户端和服务器端是通过 字节流(bytes) 的形式实现的
"""
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 10086))
server_socket.listen(5)

while True:
    try:
        accept_socket, client_info = server_socket.accept()
        accept_socket.send(b'Welcome to Socket!')
        data = accept_socket.recv(1024).decode('utf-8')
        print(f'服务器端收到来自{client_info}的信息：{data}')
        accept_socket.close()
    except:
        pass
    