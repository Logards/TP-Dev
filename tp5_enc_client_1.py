import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.11', 13337))
s.send('Hello'.encode())

data = s.recv(1024)
regex = "[+\-*]"
msg = input("Calcul à envoyer: ")
msg = msg.replace(' ', '')
operator = re.findall(regex, msg)
if not operator:
    raise ValueError
number = msg.split(f"{operator[0]}") 
for nb in number:
    if int(nb) > 4294967295:
        raise ValueError
msg_encode = msg.encode("utf-8")
msg_len = len(msg_encode)
header = msg_len.to_bytes(4, byteorder='big')
payload = header + msg_encode + "0".encode("utf-8")
s.send(payload)
s_data = s.recv(1024)
print(s_data.decode())
s.close()

