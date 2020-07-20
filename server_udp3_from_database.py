import socket
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='皮娃子',
                     password='127007',
                     database='dict',
                     charset='utf8'
                     )
cur = db.cursor()

# 创建socket对象,使用UDP协议
sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定ip地址和端口
sockfd.bind(('0.0.0.0', 7777))
result = ''

# 3.使用列表存储全部数据


while True:
    count, addr1 = sockfd.recvfrom(1024)

    data, addr = sockfd.recvfrom(int(count.decode()))

    word_get = data.decode()
    if not data:
        break
    print('接收到的单词为%s' % word_get)

    sql_select = 'select mean from word where word = "%s"' % word_get

    try:
        cur.execute(sql_select)
        mean_get = cur.fetchone()
        result = mean_get[0]

    except Exception as e:
        result = '未查询到该单词哟!'

    sockfd.sendto(result.encode(), addr)

print('服务端已关闭')
