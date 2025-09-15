import asyncio
from aiocoap import *

async def main():

    protocol = await Context.create_client_context()

    request = Message(code=GET, uri="coap://127.0.0.1:5683/time", observe=0)
    pr = protocol.request(request)

    print(" Client subscribed to coap://127.0.0.1:5683/time")

    async for response in pr.observation:
        print("Notification:", response.payload.decode())

if __name__ == "__main__":
    asyncio.run(main())
