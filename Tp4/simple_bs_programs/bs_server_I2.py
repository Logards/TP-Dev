import socket

host = ''
port = 13337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print(f"Un client vient de se co et son IP c'est {addr[0]}.")
while True:
    try:
        data = conn.recv(1024)
        data = data.decode()
        if not data: break
        if "meo" in data:
            print(f"Données reçues du client : {data}")
            envoie = "Meo a toi confrere.".encode()
            conn.sendall(envoie)
        elif "waf" in data:
            print(f"Données reçues du client : {data}")
            envoie = "ptdr t ki".encode()
            conn.sendall(envoie)
        else:
            print(f"Données reçues du client : {data}")
            envoie = "Mes respects humble humain.".encode()
            conn.sendall(envoie)

    except socket.error:
        print ("Error Occured.")
        exit(1)
conn.close()
exit()