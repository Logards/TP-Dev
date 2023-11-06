import argparse
import socket
import logging

logging.basicConfig(filename="/var/log/bs_client.log", level=logging.INFO)
host = ''
parser = argparse.ArgumentParser(description="Usage: allows you to communicate with a server")
parser.add_argument("-p", "--port", action="store", help="change the default port by the argument")
args = parser.parse_args()
if args.port is None:
    port = 13337
elif int(args.port) < 0 or int(args.port) > 65535:
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    exit(1)
elif int(args.port) < 1025 :
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    exit(2)
else:
    port = int(args.port)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
logging.info(f"Le serveur tourne sur {s.getsockname()[0]}:{port}")
conn, addr = s.accept()
print(f"Un client vient de se co et son IP c'est {addr}.")
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
