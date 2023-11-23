import asyncio
import time


async def foo():
    await asyncio.sleep(1)
    print('1 foo', time.strftime('%X'))
    await asyncio.sleep(2)
    print('3 foo', time.strftime('%X'))


async def bar():
    await asyncio.sleep(2)
    print('2 bar', time.strftime('%X'))
    await asyncio.sleep(2)
    print('4 bar', time.strftime('%X'))


if __name__ == '__main__':
    print(time.strftime('%X'))
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()
    time.sleep(1)
    print(time.strftime('%X'))


