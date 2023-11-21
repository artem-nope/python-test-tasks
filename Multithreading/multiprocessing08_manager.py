import time
from multiprocessing import cpu_count, Pool, current_process, Manager
import os
from itertools import repeat

N = 20
data1 = [i for i in range(1, N + 1)]
manager = Manager()
my_dict = manager.dict()


def f(a, d):
    res = round(a ** 0.5, 3)
    time.sleep(0.5)
    # print(f'{os.getpid()}, {current_process().name}: {a=} {b=} {res=}\n', end='')
    key = current_process().name
    if key not in d:
        d[key] = [a]
    else:
        d[key] = d[key] + [a]
    return res


if __name__ == '__main__':

    tic = time.time()
    # counter = cpu_count()
    with Pool(4) as p:
        data3 = p.starmap(f, zip(data1, repeat(my_dict)))
    toc = time.time()
    dt = toc - tic
    print(dt)
    print(data3)
    for k, v in my_dict.items():
        print(f'{k}: {v}')