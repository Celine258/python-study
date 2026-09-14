import socket#程序之间通讯之间的工具
socket_server = socket.socket()#创建socket对象
socket_server.bind(("localhost",8888))#绑定ip地址和端口
socket_server.listen(1)#表示接受的连接数量
#result = socket_server.accept()#等待连接
conn , address = socket_server.accept()#accept返回的是二元元组（客户端和服务端的链接对象，客户端地址信息）
#如果无链接则卡在这一行不向下执行
print(f"接受到链接，客户端的信息是{address}")

#接受客户端信息
#使用的是客户端和服务端链接的对象
while True:
    data:str = conn.recv(1024).decode("UTF-8")
    #recv接受的参数是缓冲区的大小
    #recv返回的是字节数组bytes，可使用decode方法通过UTF-8编码转化为字符串类型
    print(f"接受的信息是：{data}")

    msg = input("请输入要发送给客户端的信息：")#.encode("UTF-8")#解码为字节数组
    if msg == "exit":
        break
    conn.send(msg.encode("UTF-8"))

conn.close()
socket_server.close()
