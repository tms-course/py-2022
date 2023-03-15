import asyncio
from time import time

async def first(x: int) -> None:
    print(x**2)
    await asyncio.sleep(3)
    print('first завершилась')
    
async def second(x: int) -> None:
    print(x**.5)
    await asyncio.sleep(3)
    print('second завершилась')


async def main():
    task1 = asyncio.create_task(first(4))
    task2 = asyncio.create_task(second(4))
    await
    await task1
    await task2
    
start = time()
asyncio.run(main())
print('Выполнилось за {:2.4f} секунд'.format(time() - start))

    