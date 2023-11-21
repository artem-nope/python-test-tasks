import time
from threading import current_thread, Thread
import random

N = 2_000_000
M = 20
results = [0] * N


class MyThread(Thread):
    def __init__(self, n):
        Thread.__init__(self)
        self.n = n
        self.file_name = f'{current_thread().name}.txt'

    def run(self):
        print(f'{current_thread().name} is running...')
        with open(self.file_name, 'w') as f:
            for _ in range(self.n):
                r = random.random()
                f.write(str(r))
                f.write('\n')
        print(f'{current_thread().name} is stopped.')


if __name__ == '__main__':
    t_start = time.time()
    print(current_thread().name)
    threads = [MyThread(N) for i in range(M)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print(f'{current_thread().name} is stopped.\n', end='')
    t_end = time.time()
    print(f'Program worked {(t_end - t_start):.3f} sec')
    t_start = time.time()
    with open(f'{current_thread().name}.txt', 'w') as f:
        for _ in range(M * N):
            r = random.random()
            f.write(str(r))
            f.write('\n')
    t_end = time.time()
    print(f'Program worked {(t_end - t_start):.3f} sec')
