import socket

# On définit la destination de la connexion
host = '10.1.1.11'  # IP du serveur
port = 13337

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
s.connect((host, port))
envoie = int("10000").encode(encoding="ascii")
s.sendall(envoie)
# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024)

# On libère le socket TCP
s.close()

# Affichage de la réponse reçue du serveur
print(f"Le serveur a répondu {repr(data)}")
exit()
