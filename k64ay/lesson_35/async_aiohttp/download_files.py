import os

import aiohttp
import asyncio
from async_timeout import timeout

PDFS_DIR = './pdfs'

async def download(session: aiohttp.ClientSession, url: str) -> str:
    async with timeout(1.5):
        """Cancels inner block if time is out otherwise nothing happens"""
        
        async with session.get(url) as res:
            filename = os.path.basename(url)

            with open(os.path.join('pdfs', filename), 'wb') as f_handle:
                while True:
                    chunk = await res.content.read(1024)

                    if not chunk:
                        break

                    f_handle.write(chunk)

                return await res.release()
            
async def main() -> None:
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