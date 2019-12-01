import time
import numpy as np
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter() - start
        print("The function '%s' took %.4f seconds to execute" % (func.__name__, end))
        return value
    return wrapper_decorator


@timer
def insertion_sort(list):
    for index in (range(1, len(list))):
        key = list[index]
        position = index
        while position > 0 and key < list[position - 1]:
            list[position] = list[position - 1]
            position -= 1
        list[position] = key
    return list


print("Sorting %s numbers" % 10_000)
random_list = np.random.choice(100_000, 10_000, replace=True).tolist()
sorted_list = insertion_sort(random_list)
