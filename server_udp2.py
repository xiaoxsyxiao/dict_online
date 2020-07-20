import socket
import re

pattern = r'(\w+)\s+(.*)'

# 创建socket对象,使用UDP协议
sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定ip地址和端口
sockfd.bind(('0.0.0.0', 6666))
result = ''

while True:
    data, addr = sockfd.recvfrom(1024)
    word = data.decode()
    if data == '':
        break
    print('接收到的单词为%s' % word)


    # f = open('dict.txt', 'r')
    # # 1.使用findall方法+for方法对每一行匹配
    # for item in f:
    #     res = re.findall(pattern, item)
    #     if res and res[0][0] == word:
    #         result = res[0][1]
    #         break
    # else:
    #     result = '未查询到该单词哟!'
    # f.close()

    f = open('dict.txt', 'r')
    # 2. 对全文件内容匹配,使用finditer生成可迭代对象,然后进行遍历
    l = re.finditer(pattern, f.read())
    for item in l:
        if word == item.group(1):
            result = item.group(2)
            break
    else:
        result = '未查询到该单词哟!'
    f.close()

    sockfd.sendto(result.encode(), addr)
