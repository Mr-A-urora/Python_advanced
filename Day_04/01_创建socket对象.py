"""
案例：演示socket对象的创建
"""
import socket

# 创建Socket对象
# 参1：Address Family, 地址族，即：Ipv4 还是 Ipv6，默认值：AF_INET(ipv4) AF_INET6(ipv6)
# 参2：Socket Type, Socket类型，即：TCP 还是 UDP，默认值：SOCK_STREAM(TCP) SOCK_DGRAM(UDP)
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket_obj)
