import multiprocessing as mp
import random
import time


def fill_list_with_rnd_floats(li: mp.Array, even: bool):
    for i in range(0 if even else 1, len(li), 2):
        li[i] = (random.random() * 2 - 1.0)
    print('Done!', even)


if __name__ == '__main__':
    n = 500
    mylist = mp.Array('d', n)
    print(mylist[:], len(mylist))

    tic = time.time()
    p1 = mp.Process(target=fill_list_with_rnd_floats, args=(mylist, True))
    p2 = mp.Process(target=fill_list_with_rnd_floats, args=(mylist, False))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    toe = time.time()
    print(mylist[:])
    print('BYE!')
    print(f'Multiprocessing time: {toe - tic}')

    tic = time.time()
    lst = [0] * n
    for i in range(len(lst)):
        lst[i] = (random.random() * 2 - 1.0)
    toe = time.time()
    print(f'For time: {toe - tic}')
