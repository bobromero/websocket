import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")
        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")


def main():
    while True:
        asyncio.run(hello())


if __name__ == "__main__":
    main()
