import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.1.1.11', 13337))
sock.listen()
conn, addr = sock.accept()
while True:
    try:
        data = conn.recv(1024)
        if not data: break
        print(f"Donnéees reçues du client : {data}")
        if "GET /" in data.decode():
            envoie = "HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>".encode()
            sock.send(envoie)
    
    except socket.error:
        print ("Error Occured.")
        break
conn.close()
exit()