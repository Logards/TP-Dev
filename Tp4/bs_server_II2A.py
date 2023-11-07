import argparse
import socket
import logging
from colorlog import ColoredFormatter

formatter = ColoredFormatter(
    log_colors={
        'Info': 'white',
        'Warning': 'yellow'
    }
)

logging.basicConfig(filename="/var/log/bs_server/bs_server.log", format='%(asctime)s %(message)s', level=logging.INFO)
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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
logging.info(f"Le serveur tourne sur {ip_address}:{port}")
conn, addr = s.accept()
print(f"Un client {addr[0]} s'est connecté.")
while True:
    try:
        data = conn.recv(1024)
        data = data.decode()
        if not data: break
        logging.info(f"Le client {addr[0]} a envoyé {data}.")
        envoie = "Hey mon frère !".encode()
        conn.sendall(envoie)
        logging.info(f"Réponse envoyée au client {addr[0]} : {envoie.decode()}.")

    except socket.error:
        print ("Error Occured.")
        exit(1)
conn.close()
exit()
