import socket
host ='127.0.0.1'
port = 5001
obj = socket.socket()
obj.connect((host,port))
message = input("enter the message you want to send: ")

while message!="q":
    obj.send(message.encode())
    data = obj.recv(1024).decode()
    print("recived from server: "+data)
    message = input("enter the message you want to send: ")
obj.close()