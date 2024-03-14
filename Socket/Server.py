import socket

s = socket.socket()

s.bind(('localhost',9990))

s.listen(3)
print("Server is waiting.........")
while True:
    client_socket,client_address=s.accept()
    no1 = int(client_socket.recv(1024).decode())
    no2 = int(client_socket.recv(1024).decode())
    print("From Server client is {},{},{}".format(client_address,no1,no2))
    client_socket.send(bytes("Welcome to Socket Programing..... {}".format(no1+no2),"utf-8"))
    client_socket.close()
