"""
udp_server.py  udp服务端简单示例
"""

from socket import *

# 创建udp的套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0",8888))

# 接收一个消息
while True:
    # 注意接收到的addr是客户端的地址
    data,addr = udp_socket.recvfrom(2)
    print("从网络接收到了:",data.decode()) #转换为字符串


# 关闭套接字
udp_socket.close()


