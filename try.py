import asyncio
import websockets

async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)

async def main():
    url = "wss://cekirdektenyetisenler.kartaca.com/ws"
    async with websockets.connect(url) as ws:
        await handler(ws)
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
