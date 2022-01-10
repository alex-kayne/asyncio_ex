import asyncio
import aiohttp
from time import time

def write_image(data, i):
    filename = f'file -{i}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session, i):
    async with session.get(url) as response:
        data = await response.read()
        write_image(data, i)

async def main():
    url = "https://loremflickr.com/320/240"
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            print(i)
            task = asyncio.create_task(fetch_content(url, session, i))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time()
    #asyncio.run(main())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_until_complete(asyncio.sleep(1))
    loop.close()
    print(time() - t0)
