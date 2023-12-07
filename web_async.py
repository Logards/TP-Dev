import asyncio
import aiohttp
import aiofiles
from sys import argv

args = argv[1]


async def get_url(url=args):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp = await resp.read()
            # resp contient le contenu HTML de la page
            return resp.decode()


async def write_content(file: str):
    content = await get_url()
    async with aiofiles.open(file, "w") as out:
        await out.write(content)
        await out.flush()


loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(write_content("/tmp/web_page")),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()
