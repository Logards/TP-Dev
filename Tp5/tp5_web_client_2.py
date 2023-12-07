import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.11', 13337))

mess = "GET /"
s.send(mess.encode())
s_data = s.recv(1024)
print(s_data.decode())