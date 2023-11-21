import time
from multiprocessing import cpu_count, Pool
import random
import math

N = 5
data1 = [random.random() for i in range(10 ** N)]


def f(x):
    return math.sin(math.asin(math.cos(math.acos(x))))


if __name__ == '__main__':
    for counter in (2, 4, 6, 8, 10):
        tic = time.time()
        # counter = cpu_count()
        with Pool(counter) as p:
            data2 = p.map(f, data1)
        toc = time.time()
        dt = toc - tic
        print(counter)
        print(dt, dt / len(data1))
        print(data2[:10])
        print()

