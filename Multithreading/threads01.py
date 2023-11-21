import time
from threading import current_thread, Thread
import random

N = 20
results = [0] * N


def thread_function(t: float, idx: int):
    print(f'{current_thread().name} is running...')
    while True:
        r = random.random()
        time.sleep(t)
        if r < t:
            results[idx] = r
            break
    print(f'{current_thread().name} is stopped.')


if __name__ == '__main__':
    print(current_thread().name)
    t_params = [random.uniform(0.1, 0.2) for _ in range(N)]
    threads = []
    for i, t in enumerate(t_params, start=1):
        threads.append(Thread(target=thread_function, args=[t, i - 1], name=f'<t{i}>'))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(results)
    print(f'{current_thread().name} is stopped.\n', end=' ')
