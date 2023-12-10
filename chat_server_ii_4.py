import asyncio
import json
import argparse
Clients = {}

parser = argparse.ArgumentParser(description="Usage: allows you to communicate with a server")
parser.add_argument("-p", "--port", action="store", help="change the default port by the argument")
parser.add_argument("-a", "--address", action="store", help="change the default address by the argument")
args = parser.parse_args()


# cette fonction sera appelée à chaque fois qu'on reçoit une connexion d'un client
async def handle_client_msg(reader, writer):
    global Clients
    while True:
        # les objets reader et writer permettent de lire/envoyer des données auux clients

        # on lit les 1024 prochains octets
        # notez le await pour indiquer que cette opération peut produire de l'attente
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')
        if addr not in Clients:
            Clients[addr] = {}
            Clients[addr]["r"] = reader
            Clients[addr]["w"] = writer

        # si le client n'envoie rien, il s'est sûrement déco
        if data == b'':
            print(f"{Clients[addr]['pseudo']} s'est déconnecté")
            for client in Clients:
                if client != addr:
                    sender = Clients[client]["w"]
                    sender.write(f"Annonce : {Clients[addr]['pseudo']} a quitté la chatroom".encode())
                    await sender.drain()
            del Clients[addr]
            break

        # on décode et affiche le msg du client
        message = data.decode()
        if "Hello|" in message:
            pseudo = message.split("|")[1]
            Clients[addr]["pseudo"] = pseudo
            print(f"{pseudo} s'est connecté")
            for client in Clients:
                if client != addr:
                    sender = Clients[client]["w"]
                    sender.write(f"Annonce : {pseudo} a rejoint la chatroom".encode())
                    await sender.drain()
        else:
            print(f"Message received from {addr[0]}:{addr[1]} : {message}")
            for client in Clients:
                if client != addr:
                    sender = Clients[client]["w"]
                    sender.write(f"{Clients[addr]['pseudo']} a dit : {message}".encode())
                    ## une ligne qui attend que tout soit envoyé (on peut donc l'await)
                    await sender.drain()


async def main():
    # on crée un objet server avec asyncio.start_server()
    ## on précise une fonction à appeler quand un paquet est reçu
    ## on précise sur quelle IP et quel port écouter
    f = open("config_server.json", "r")
    config = json.load(f)
    f.close()
    host = config["Host"]
    port = config["Port"]
    if args.port is not None:
        port = int(args.port)
    if args.address is not None:
        host = args.address
    server = await asyncio.start_server(handle_client_msg, host, port)
    # ptit affichage côté serveur
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    # on lance le serveur
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    # lancement du main en asynchrone avec asyncio.run()
    asyncio.run(main())
