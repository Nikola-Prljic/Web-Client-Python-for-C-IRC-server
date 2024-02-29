import asyncio
import websockets

def executeCmd(cmd):
    if cmd == "hello":
        return "yo :)"
    return cmd

async def echo(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        message = executeCmd(message)
        await websocket.send(message.upper())

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())