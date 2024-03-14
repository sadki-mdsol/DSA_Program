import socket

client_socket = socket.socket()

client_socket.connect(('localhost',9990))

print("Connected to server........")

no1 = input("Please enter number 1")

client_socket.send(bytes(no1,"utf-8"))

no2 = input("Please enter number 2")

client_socket.send(bytes(no2,"utf-8"))

received = client_socket.recv(1024).decode()

print("Received from server ",received)