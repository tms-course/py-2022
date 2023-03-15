import os

import asyncio
import aiohttp
from async_timeout import timeout

PDFS_DIR = './pdfs'

async def download(session: aiohttp.ClientSession, url: str) -> None:
    async with timeout(1.5):
        async with session.get(url) as res:
            filename = os.path.basename(url)

            with open(os.path.join(PDFS_DIR, filename), 'wb') as file:
                while True:
                    chunk = await res.content.read(1024)

                    if not chunk:
                        break

                    file.write(chunk)

            await res.release()


async def main():
    urls = [
        'http://www.irs.gov/pub/irs-pdf/f1040.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040a.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040ez.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040es.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040sb.pdf',
    ]

    if not os.path.exists(PDFS_DIR):
        os.mkdir(PDFS_DIR)

    async with aiohttp.ClientSession() as session:
        for url in urls:
            await download(session, url)

if __name__ == '__main__':
    asyncio.run(main())