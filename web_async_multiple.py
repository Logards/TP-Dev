import os.path
from sys import argv
import re
import validators
import requests
import asyncio
import aiofiles
import aiohttp

args = argv[1]


async def file_exist(file_path=args):
    return os.path.isfile(file_path)


async def get_url_file(file_path=args):
    reg = "[,\n ]"
    if await file_exist():
        async with aiofiles.open(file_path) as file:
            content = await file.read()
            await file.flush()
        content = content.split(re.match(reg, content))
        return content


async def get_url_content():
    content = await get_url_file()
    cont_to_strip = "https://"
    for i in content:
        if validators.url(i):
            async with aiohttp.ClientSession() as session:
                async with session.get(i) as resp:
                    resp = await resp.read()
                    i = i.replace(cont_to_strip, "")
                    return [resp, i]


async def write_content():
    lst = await get_url_content()
    async with aiofiles.open(f"/tmp/web_{lst[1]}", "a") as out:
        await out.write(lst[0].decode())
        await out.flush()


async def main():
    tasks = [get_url_content(), write_content()]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
