import asyncio
import json
import argparse
import websockets

Clients = {}

parser = argparse.ArgumentParser(description="Usage: allows you to communicate with a server")
parser.add_argument("-p", "--port", action="store", help="change the default port by the argument")
parser.add_argument("-a", "--address", action="store", help="change the default address by the argument")
args = parser.parse_args()


# cette fonction sera appelée à chaque fois qu'on reçoit une connexion d'un client
async def handle_client_msg(websocket: websockets.WebSocketClientProtocol):
    global Clients
    while True:
        try:
            data = await websocket.recv()
            addr = (websocket.remote_address[0], str(websocket.remote_address[1]))
            if addr not in Clients:
                Clients[addr] = {}
                Clients[addr]["rw"] = websocket

            message = data
            if "Hello|" in message:
                pseudo = message.split("|")[1]
                Clients[addr]["pseudo"] = pseudo
                print(f"{pseudo} s'est connecté")
                for client in Clients:
                    if client != addr:
                        await Clients[client]["rw"].send(f"Annonce : {pseudo} a rejoint la chatroom")
            else:
                print(f"Message received from {Clients[addr]['pseudo']} : {message}")
                for client in Clients:
                    if client != addr:
                        print(f"suppose ti send to {Clients[client]['pseudo']}")
                        await Clients[client]["rw"].send(f"{Clients[addr]['pseudo']} a dit : {message}")

        except websockets.ConnectionClosedOK:
            print(f"{Clients[addr]['pseudo']} s'est déconnecté")
            for client in Clients:
                if client != addr:
                    await Clients[client]["rw"].send(f"Annonce : {Clients[addr]['pseudo']} a quitté la chatroom")
            del Clients[addr]
            break


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
    async with websockets.serve(handle_client_msg, host, port):
        print(f"Serving on : {host} : {port}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    # lancement du main en asynchrone avec asyncio.run()
    asyncio.run(main())
