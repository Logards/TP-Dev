import socket
import asyncio
import aioconsole


async def message(writer):
    while True:
        message = await aioconsole.ainput()
        writer.write(message.encode())
        await writer.drain()


async def receive(reader):
    while True:
        data = await reader.read(1024)
        print(data.decode())


async def main():
    reader, writer = await asyncio.open_connection(host="127.0.0.1", port=8888)
    tasks = [message(writer), receive(reader)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())