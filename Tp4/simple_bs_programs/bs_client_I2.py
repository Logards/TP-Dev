import socket

# On définit la destination de la connexion
host = '10.1.1.11'  # IP du serveur
port = 13337

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print("Que veux-tu envoyer au serveur : ")
    mess = input()
    s.connect((host, port))
    envoie = mess.encode()
    s.sendall(envoie)
    # On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
    data = s.recv(1024)
    s.close()
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    print(f"Le serveur a répondu {repr(data)}")
except ConnectionRefusedError or ConnectionError:
    print("Vous n'etes pas connecte")
    exit(1)
exit()