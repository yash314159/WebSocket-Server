import asyncio
import websockets

async def handle_ip_request(websocket, path):
    # Extract the client IP from the request
    ip = websocket.remote_address[0]
    await websocket.send(ip)

async def main():
    async with websockets.serve(handle_ip_request, "0.0.0.0", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
