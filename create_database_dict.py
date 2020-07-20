import pymysql
import re

pattern = r'(\w+)\s+(.*)'

f = open('dict.txt', 'r')
l = re.findall(pattern, f.read())
print(l[0])
f.close()

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='皮娃子',
                     password='127007',
                     database='dict',
                     charset='utf8'
                     )
cur = db.cursor()

sql_insert = 'insert into word(word,mean) values(%s,%s)'

cur.executemany(sql_insert, l)
db.commit()

cur.close()
db.close()
