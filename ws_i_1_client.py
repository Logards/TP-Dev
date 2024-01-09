import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8888"
    async with websockets.connect(uri) as websocket:
        mess = input("Que veux tu dire ? : ")

        await websocket.send(mess)
        print(f">>> {mess}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())
