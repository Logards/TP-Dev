import asyncio
import websockets


async def hello(websocket):
    while True:
        name = await websocket.recv()
        print(f"<<< {name}")
        greeting = f"Hello voici ce que tu m'as envoyé : {name} !"
        await websocket.send(greeting)
        print(f">>> {greeting}")


async def main():
    async with websockets.serve(hello, "localhost", 8888):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
