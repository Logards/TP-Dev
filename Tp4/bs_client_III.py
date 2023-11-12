import socket
import psutil
import os
import logging
import re

import colorlog

def ip():
    if(os.name=="posix"):
        return(psutil.net_if_addrs()[list(psutil.net_if_addrs().keys())[1]][0][1])
        # print(psutil.net_if_addrs()['wlp2s0'][0][1])
    else:
        return(psutil.net_if_addrs()['Wi-Fi'][1][1])

logger = colorlog.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('/var/log/bs_client/bs_client.log', 'w', 'utf-8')
file_handler.setLevel(logging.INFO)
stream_handler = colorlog.StreamHandler()
stream_handler.setLevel(logging.ERROR)

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s %(levelname)s %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'white',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
op_regex = "[+\-*]"
nb_regex = "-?([0-9]{1,5}|100000)"

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# On définit la destination de la connexion
host = '10.1.1.11'  # IP du serveur
port = 13337

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mess = input()
    if type(mess) is not str:
        raise TypeError("Tu te crois ou, moi je veux une string")
    if re.match(nb_regex, mess) and re.match(op_regex, mess):
        s.connect((host, port))
        logging.info(f"Connexion réussie à {ip()}:{port}.")
        envoie = mess.encode()
        logging.info(f"Message envoyé au serveur {host} : {mess}.")
        s.sendall(envoie)
        data = s.recv(1024)
        s.close()
        logging.info(f"Réponse reçue du serveur {host} : {repr(data)}.")
except ConnectionRefusedError or ConnectionError:
    print("Vous n'etes pas connecte")
    exit(1)
exit()