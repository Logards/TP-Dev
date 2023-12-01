import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.11', 13337))
def int_to_bytes(integer):
    return integer.to_bytes((integer.bit_length() + 7) // 8, 'big')

def bytes_to_int(bytes):
    return int.from_bytes(bytes, 'big')

regex = "[+\-*]"
msg = input("Calcul à envoyer: ")
msg = msg.replace(' ', '')
operator = re.findall(regex, msg)
if not operator:
    raise ValueError
number = msg.split(operator[0]) 
for nb in number:
    if int(nb) > 4294967295:
        raise ValueError
msg_encode = int_to_bytes(int(number[0]))
msg_encode += operator[0].encode()
msg_encode += int_to_bytes(int(number[1]))
print(msg_encode)
s.send(msg_encode)
s_data = s.recv(1024)
print(s_data.decode())
s.close()

