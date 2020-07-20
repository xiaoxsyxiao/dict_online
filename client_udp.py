# 放过我吧!
import socket

ADDR = ("127.0.0.1", 7777)
# ADDR = ('176.140.6.136', 8866)
# ADDR = ('176.140.6.130', 8888)
socketfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input(">>")

    socketfd.sendto(str(len(msg)).encode(), ADDR)

    socketfd.sendto(msg.encode(), ADDR)

    if not msg:
        print('程序已退出')
        break
    print('等待消息接收中...')

    data, addr = socketfd.recvfrom(1024)
    res = data.decode()
    print('%s 单词的解释为: %s' % (msg, res))
