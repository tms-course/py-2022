import asyncio
import aiohttp
from codetiming import Timer

async def task(name: str, work_queue: asyncio.Queue) -> None:
    timer = Timer(text=f'Task {name} elapsed time: {{:.1f}}')

    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f'Task {name} getting URL: {url}')

            timer.start()
            async with session.get(url) as res:
                await res.text()
            timer.stop()


async def main() -> None:
    work_queue = asyncio.Queue()
    urls = [
        'http://google.com',
        'http://onliner.by',
        'http://yandex.by',
        'http://habr.com',
        'http://realt.by',
    ]

    for url in urls:
        await work_queue.put(url)

    with Timer(text='\nTotal elapsed time: {:.1f}'):
        await asyncio.gather(
            asyncio.create_task(task('One', work_queue)),
            asyncio.create_task(task('Two', work_queue)),
        )

if __name__ == '__main__':
    asyncio.run(main())