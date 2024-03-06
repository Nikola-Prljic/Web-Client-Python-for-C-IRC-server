"""#############################################################
   # A brige between a websocket connection into a tcp server  #
"""#############################################################

import asyncio
import websockets
import client.split_msg as split_msg

async def websocket_handler(websocket, path):
    tcp_reader, tcp_writer = await asyncio.open_connection('localhost', 8080)

    async def forward_messages():
        try:
            while True:
                message = await websocket.recv()
                message += "\n"
                tcp_writer.write(message.encode())
                await tcp_writer.drain()
                print(message)
        except websockets.exceptions.ConnectionClosedOK:
            pass

    async def receive_tcp_responses():
        try:
            while True:
                response = await tcp_reader.read(100)
                response = split_msg.splitMsg(response).handelData()
                if "ping" not in response:
                    await websocket.send(response)
                    print(response)
        except asyncio.CancelledError:
            pass

    await asyncio.gather(forward_messages(), receive_tcp_responses())

async def main():
    async with websockets.serve(websocket_handler, "localhost", 8765):
        await asyncio.Future()  # Run forever

asyncio.run(main())

import signal

def handler(signum, frame):
    print(" exit")
    exit(0)

signal.signal(signal.SIGINT, handler)