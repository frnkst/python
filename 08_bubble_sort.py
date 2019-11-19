# 20'000 numbers in 59.39 seconds (native is 0.00 seconds)

import numpy as np
import time


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(0, len(l) - 1):
            if l[j] >= l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]
    return l


# Simple test
unsorted_list = [7, 23, 1, 45, 6789, 46, 7]
sorted_list = bubble_sort(unsorted_list)
natively_sorted = sorted(unsorted_list)
print("The result is the same as natively sorted? %s" % (sorted_list == natively_sorted))


def performance_test(amount):
    print("--------")
    print("Sorting %s numbers" % amount)
    random_list = np.random.choice(100_000, amount, replace=True).tolist()
    start = time.perf_counter()
    sorted_list = bubble_sort(random_list)
    print("Bubble sort: \t %.2f s" % (time.perf_counter() - start))

    start = time.perf_counter()
    natively_sorted = sorted(random_list)
    print("Native sort: \t\t %.2f s" % (time.perf_counter() - start))
    assert (sorted_list == natively_sorted), "The algorithm has not sorted the list correctly"


for amount in [1_0, 10_000, 20_000]:
    performance_test(amount)
