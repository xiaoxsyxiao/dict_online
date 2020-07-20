import socket
import re

pattern = r'(\w+)\s+(.*)'

# 创建socket对象,使用UDP协议
sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定ip地址和端口
sockfd.bind(('0.0.0.0', 7777))
result = ''

# 3.使用列表存储全部数据
f = open('dict.txt', 'r')
l = re.findall(pattern, f.read())
f.close()

while True:
    data, addr = sockfd.recvfrom(1024)
    word = data.decode()
    print('接收到的单词为%s' % word)

    # 3.遍历列表元素进行匹配
    for item in l:
        if item and word == item[0]:
            result = item[1]
            break
    else:
        result = '未查询到该单词哟!'

    sockfd.sendto(result.encode(), addr)
