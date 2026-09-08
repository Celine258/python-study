from pymysql import Connection
import pymysql
import json
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="240567"
)
cursor = conn.cursor(pymysql.cursors.DictCursor)#
conn.select_db("py_sql")
cursor.execute("select DATE_FORMAT(date,'%Y‑%m‑%d') as date,id,money,province from orders ")#注意日期格式

result = cursor.fetchall()
#with open("D:/Python学习/part3/mysql/data.txt","w",encoding="utf-8") as f:
#    for info in result:
#    #print(info)
#        line = json.dumps(info,ensure_ascii=False)
#        print(line)
#        f.write(line + "\n")
for line in result:
    info = json.dumps(line,ensure_ascii=False)
    print(info)

conn.close()