import time
from threading import current_thread, Thread
from multiprocessing import Process
import random

N = 2_000_000
M = 10
results = [0] * N


def thread_function(n: int, name: str):
    print(f'{name}  is running...')
    with open(f'{name}.txt', 'w') as f:
        for _ in range(n):
            r = random.random()
            f.write(str(r))
            f.write('\n')
    print(f'{name} is stopped.')


if __name__ == '__main__':
    t_start = time.time()
    print(current_thread().name)
    threads = []
    for i in range(M):
        threads.append(Thread(target=thread_function, args=[N, f'<thread{i + 1}>']))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f'Multithreading: {current_thread().name} is stopped.\n', end='')
    t_end = time.time()
    print(f'Program multithreading worked {(t_end - t_start):.3f} sec')

    t_start = time.time()
    print(current_thread().name)
    threads = []
    for i in range(M):
        threads.append(Process(target=thread_function, args=[N, f'<process{i + 1}>']))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f'Multiprocessing: {current_thread().name} is stopped.\n', end='')
    t_end = time.time()
    print(f'Program multiprocessing worked {(t_end - t_start):.3f} sec')


    t_start = time.time()
    with open(f'Main thread: {current_thread().name}.txt', 'w') as f:
        for _ in range(M * N):
            r = random.random()
            f.write(str(r))
            f.write('\n')
    t_end = time.time()
    print(f'Program main thread worked {(t_end - t_start):.3f} sec')
