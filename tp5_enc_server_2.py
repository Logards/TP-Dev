import socket

def int_to_bytes(integer):
    return integer.to_bytes((integer.bit_length() + 7) // 8, 'big')

def bytes_to_int(bytes):
    return int.from_bytes(bytes, 'big')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.1.1.11', 13337))
sock.listen()


while True:
    client, client_addr = sock.accept()
    # On lit les 4 premiers octets qui arrivent du client
    # Car dans le client, on a fixé la taille du header à 4 octets
    header = client.recv(1)
    if not header:
        break

    # On lit la valeur
    msg_len = int.from_bytes(header[0:4], byteorder='big')

    print(f"Lecture des {msg_len} prochains octets")

    # Une liste qui va contenir les données reçues
    chunks = []

    bytes_received = 0
    while bytes_received < msg_len:
        # Si on reçoit + que la taille annoncée, on lit 1024 par 1024 octets
        chunk = client.recv(min(msg_len - bytes_received,
                                1024))
        if not chunk:
            raise RuntimeError('Invalid chunk received bro')

        # on ajoute le morceau de 1024 ou moins à notre liste
        chunks.append(chunk)

        # on ajoute la quantité d'octets reçus au compteur
        bytes_received += len(chunk)

    # ptit one-liner pas combliqué à comprendre pour assembler la liste en un seul message
    message_received = b"".join(chunks).decode('utf-8')
    print(chunks)
    print(f"Received from client {message_received}")
    result = eval(message_received)
    result = str(result).encode()
    print(f"Result: {result}")
    client.send(result)
    client.close()
sock.close()
