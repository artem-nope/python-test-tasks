import asyncio
import time


async def f(delay, message):
    await asyncio.sleep(delay)
    print(message)


async def main():
    print(f'Started at {time.strftime("%X")}')
    task1 = asyncio.create_task(f(2.5, 'Hello'))
    task2 = asyncio.create_task(f(2, 'World'))
    await task1
    await task2
    print(f'Finished at {time.strftime("%X")}')

if __name__ == '__main__':
    asyncio.run(main())


