import socket
from sys import argv
import os


def lookup():
    return socket.gethostbyname(argv[2])


def ping():
    response = os.system('ping -c 1 ' + str(argv[2]) + " >> /dev/null")
    if response == 0:
        return "UP !"
    else:
        return "DOWN !"


def ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

mess = ""
commande = str(argv[1])
if commande == "ip":
    mess = ip()
elif commande == "ping":
    mess = ping()
elif commande == "lookup":
    mess = lookup()
else:
    mess = (f"{argv[1]} s'il te plaît avant de taper n'importe quoi regarde les commandes dispos :)")
print(mess)
