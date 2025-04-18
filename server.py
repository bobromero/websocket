import asyncio
import websockets


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
            print(f"Received: {message}")
            response = f"Server received: {message}"
            await websocket.send(response)
        except websockets.ConnectionClosed:
            break


async def main():
    async with websockets.serve(handler, "localhost", 8000):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
