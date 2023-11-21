import multiprocessing


N = 1_000_000


# Without lock
# function to withdraw from account
def withdraw(balance):
    for _ in range(N):
        balance.value = balance.value - 1


# function to deposit to account
def deposit(balance):
    for _ in range(N):
        balance.value = balance.value + 1


def perform_transactions():
    # initial balance (in shared memory)
    balance = multiprocessing.Value('i', 100)

    # creating new processes
    p1 = multiprocessing.Process(target=withdraw, args=(balance,))
    p2 = multiprocessing.Process(target=deposit, args=(balance,))
    p3 = multiprocessing.Process(target=withdraw, args=(balance,))
    p4 = multiprocessing.Process(target=deposit, args=(balance,))

    # starting processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # wait until processes are finished
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    # print final balance
    print("Final balance = {}".format(balance.value))


if __name__ == '__main__':
    for _ in range(10):
        # perform same transaction process 10 times
        perform_transactions()
