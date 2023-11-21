import time
from multiprocessing import cpu_count, Pool, current_process
import os
from itertools import repeat

N = 20
data1 = [i for i in range(1, N + 1)]
b = 0.5


def f(a, b):
    res = a ** b
    time.sleep(0.5)
    print(f'{os.getpid()}, {current_process().name}: {a=} {b=} {res=}\n', end='')
    return round(res, 3)


if __name__ == '__main__':
    tic = time.time()
    # counter = cpu_count()
    with Pool(20) as p:
        data3 = p.starmap(f, zip(data1, repeat(b)))
    toc = time.time()
    dt = toc - tic
    print(dt)
    print(data3)
    print(os.cpu_count())