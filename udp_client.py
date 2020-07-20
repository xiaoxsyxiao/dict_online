"""
udp_client.py  客户端
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)

# 创建UDP套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 发数据
while True:
    msg = input(">>")
    udp_socket.sendto(msg.encode(),ADDR)

udp_socket.close()