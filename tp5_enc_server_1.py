import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.1.1.11', 13337))  
s.listen(1)
client, client_addr = s.accept()

s.listen(1)
print("merde")
conn, addr = s.accept()
print("salut a toi")

while True:
    header = conn.recv(4)
    if not header: break
    msg_len = int.from_bytes(header[0:4], byteorder='big')
    print(f"Lecture des {msg_len} prochains octets")
    chunks = []
    bytes_received = 0
    while bytes_received < msg_len:
        chunks = client.recv(min(msg_len - bytes_received, 1024)) 
        if not chunks: raise RuntimeError("Invalid chunk received sussy baka")
        chunks.append(chunks)
        bytes_received = len(chunks)
    message_received =  b"".join(chunks).decode('utf-8')
    print(f"Received from client {message_received}")
conn.close()
