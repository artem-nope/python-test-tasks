import asyncio
import time


async def f(delay, message):
    await asyncio.sleep(delay)
    print(message)


async def main():
    print(f'Started at {time.strftime("%X")}')
    await f(2, 'Hello')
    await f(2, 'World')
    print(f'Finished at {time.strftime("%X")}')

if __name__ == '__main__':
    asyncio.run(main())


