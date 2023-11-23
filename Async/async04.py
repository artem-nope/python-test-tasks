import asyncio
import time

N = 5


async def foo(i):
    await asyncio.sleep(1 + i)
    print(f'func {i}: {i}', time.strftime('%X'))
    await asyncio.sleep(N)
    print(f'func {i}: {i + N}', time.strftime('%X'))


if __name__ == '__main__':
    print(time.strftime('%X'))
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(foo(i=1)) for i in range(N)]
    wait_task = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_task)
    ioloop.close()

    # asyncio.run(main())
    time.sleep(1)
    print(time.strftime('%X'))