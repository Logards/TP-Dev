import socket
import asyncio
import aioconsole
import json
import argparse


parser = argparse.ArgumentParser(description="Usage: allows you to communicate with a server")
parser.add_argument("-p", "--port", action="store", help="change the default port by the argument")
parser.add_argument("-a", "--address", action="store", help="change the default address by the argument")
args = parser.parse_args()


def get_pseudo():
    pseudo = input("Entrez votre pseudo : ")
    return f"Hello|{pseudo}"


async def message(writer, pseudo = None):
    while True:
        message = await aioconsole.ainput()
        writer.write(message.encode())
        await writer.drain()


async def receive(reader):
    while True:
        data = await reader.read(1024)
        if data == b"":
            print("Le serveur s'est barré au kazakhstan")
            exit()
        else:
            print(data.decode())


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
    reader, writer = await asyncio.open_connection(host, port)
    writer.write(get_pseudo().encode())
    await writer.drain()
    tasks = [message(writer), receive(reader)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())