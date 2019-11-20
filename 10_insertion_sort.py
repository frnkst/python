# 20'000 numbers in 16.83 seconds (native is 0.00 seconds)

import time
import numpy as np


def insertion_sort(list):
    for index in (range(1, len(list))):
        key = list[index]
        position = index
        while position > 0 and key < list[position - 1]:
            list[position] = list[position - 1]
            position -= 1
        list[position] = key
    return list


# Quick check
unsorted_list = [7, 23, 1, 45, 6789, 46, 7]
sorted_list = insertion_sort(unsorted_list)
natively_sorted = sorted(unsorted_list)
assert (sorted_list == natively_sorted), "The algorithm has not sorted the list correctly"


# Performance test
def performance_test(amount):
    print("--------")
    print("Sorting %s numbers" % amount)
    random_list = np.random.choice(100_000, amount, replace=True).tolist()
    start = time.perf_counter()
    sorted_list = insertion_sort(random_list)
    print("Selection sort: \t %.2f s" % (time.perf_counter() - start))

    start = time.perf_counter()
    natively_sorted = sorted(random_list)
    print("Native sort: \t\t %.2f s" % (time.perf_counter() - start))
    assert (sorted_list == natively_sorted), "The algorithm has not sorted the list correctly"


for amount in [10, 100, 1_000, 10_000, 20_000, 50_000]:
    performance_test(amount)
