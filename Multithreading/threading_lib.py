import time
from threading import current_thread, Thread
import random


def thread_function(t):
    print(f'{current_thread().name} is running...')
    while True:
        r = random.random()
        time.sleep(t)
        if r < t:
            break
    print(f'{current_thread().name} is stopped.')


if __name__ == '__main__':
    print(current_thread().name)
    t1 = Thread(target=thread_function, args=[0.1], name='<t1>')
    t1.start()
    print(f'{current_thread().name} is stopped.')