import asyncio
import datetime
from aiocoap import *
from aiocoap import resource

class TimeResource(resource.ObservableResource):
    def __init__(self):
        super().__init__()

    async def render_get(self, request):

        payload = datetime.datetime.now().strftime("%H:%M:%S").encode("utf-8")
        return Message(payload=payload)

    async def notify(self):

        while True:
            await asyncio.sleep(2)
            self.updated_state()

async def main():

    root = resource.Site()
    time_res = TimeResource()
    root.add_resource(['time'], time_res)


    asyncio.create_task(time_res.notify())

    bind = ("127.0.0.1", 5683)
    await Context.create_server_context(root, bind=bind)

    print("CoAP server is running at coap://127.0.0.1:5683/time (observable)")
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())
