import time
from multiprocessing import cpu_count, Pool, current_process
import os

N = 20
data1 = [i for i in range(1, N + 1)]
data2 = [j for j in range(N, 0, -1)]


def f(a, b):
    res = a + b
    time.sleep(0.5)
    print(f'{os.getpid()}, {current_process().name}: {a=} {b=} {res=}\n', end='')
    return res


if __name__ == '__main__':
    tic = time.time()
    # counter = cpu_count()
    with Pool(4) as p:
        data3 = p.starmap(f, zip(data1, data2))
    toc = time.time()
    dt = toc - tic
    print(dt)
    print(data3)
    print(os.cpu_count())

