import asyncio
import aioconsole
import json
import argparse
import websockets


parser = argparse.ArgumentParser(description="Usage: allows you to communicate with a server")
parser.add_argument("-p", "--port", action="store", help="change the default port by the argument")
parser.add_argument("-a", "--address", action="store", help="change the default address by the argument")
args = parser.parse_args()


def get_pseudo():
    pseudo = input("Entrez votre pseudo : ")
    return f"Hello|{pseudo}"


async def message(websocket: websockets.WebSocketClientProtocol):
    while True:
        message = await aioconsole.ainput("Que voulez vous dire : ")
        await websocket.send(message)


async def receive(websocket: websockets.WebSocketClientProtocol):
    while True:
        data = await websocket.recv()
        if data == "":
            print("Le serveur s'est barré au kazakhstan")
            exit()
        else:
            print(data)


async def main():
    f = open("config_client.json", "r")
    config = json.load(f)
    f.close()
    if args.port is not None:
        config["Port"] = int(args.port)
    if args.address is not None:
        config["Host"] = args.address
    host = config["Host"]
    port = config["Port"]
    uri = "ws://localhost:8888"
    async with websockets.connect(uri) as websocket:
        await websocket.send(get_pseudo())
        tasks = [message(websocket), receive(websocket)]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())