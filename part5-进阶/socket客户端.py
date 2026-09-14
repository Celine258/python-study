import socket
socket_client = socket.socket()
socket_client.connect(("localhost",8888))
while True:
    msg = input("请输入要发送的信息：")#.encode("utf-8")
    if msg == "exit":
        break
    socket_client.send(msg.encode("utf-8"))

    recv_data = socket_client.recv(1024).decode("utf-8")
    print(f"服务端回复的信息是：{recv_data}")

socket_client.close()