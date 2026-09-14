from pymysql import Connection
from data_define import Record
from file_define import TextFileReader,JsonFileReader
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="240567",
    autocommit=True #自动提交
)
#print(conn.get_server_info())

cursor = conn.cursor()
conn.select_db("py_sql")
text_file_reader = TextFileReader("D:/Python学习/part3/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/Python学习/part3/2011年2月销售数据JSON.txt")
jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()
all_data = jan_data + feb_data

#cursor.execute("create table test_mysql(id int,name varchar(10))")
#cursor.execute("select * from student ")
#results: tuple = cursor.fetchall()
#for i in results:
#    print(i)
for record in all_data:
    info = f"insert into orders(date,id,money,province) values('{record.date}','{record.ID}',{record.money},'{record.province}')"
    cursor.execute(info)
#conn.commit() #手动提交
conn.close()