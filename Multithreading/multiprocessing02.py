import multiprocessing
import time


def square_list(mylist, result, square_sum):
    """
    function to square a given list
    """
    # append squares of mylist to result array
    for idx, num in enumerate(mylist):
        result[idx] = num * num

    # square_sum value
    square_sum.value = sum(result)

    # print result Array
    print("Result(in process p1): {}".format(result[:]))

    # print square_sum Value
    print("Sum of squares(in process p1): {}".format(square_sum.value))


if __name__ == '__main__':
    # input list
    mylist = [1, 2, 3, 4]

    tic = time.time()
    # creating Array of int data type with space for 4 integers
    result = multiprocessing.Array('i', len(mylist))

    # creating Value of int data type
    square_sum = multiprocessing.Value('i')

    # creating new process
    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

    # starting process
    p1.start()

    # wait until process is finished
    p1.join()
    toe = time.time()

    print(f'Multiprocessing time: {toe - tic}')
    # print result array
    print("Result(in main program): {}".format(result[:]))

    # print square_sum Value
    print("Sum of squares(in main program): {}".format(square_sum.value))

    tic = time.time()
    res = []
    for i in range(len(mylist)):
        res.append(mylist[i] ** 2)
    toe = time.time()
    print(f'For time: {toe - tic}')
    print(res)
