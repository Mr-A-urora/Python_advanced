"""
案例：文件上传案例，服务器端代码
"""
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 10086))
server_socket.listen(5)

count = 0
while True:
    count += 1
    try:
        accept_socket, client_info = server_socket.accept()

        with open('./data/服务器端/my_' + str(count) + '.jpg', 'wb') as dest_f:
            while True:
                bys = accept_socket.recv(8192)   # 8192字节 = 8kb
                # 判断是否读取到数据，无数据（说明客户端断开连接）结束即可
                if len(bys) == 0:
                    break
                dest_f.write(bys)

        accept_socket.close()

    except:
        pass
