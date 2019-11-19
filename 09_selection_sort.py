# 20'000 numbers in 13.96 seconds (native is 0.00 seconds)

import time
import numpy as np


def selection_sort(l):
    for i in range(len(l)):
        minimum_idx = i
        for j in range(i + 1, len(l)):
            if l[minimum_idx] > l[j]:
                minimum_idx = j
        l[i], l[minimum_idx] = l[minimum_idx], l[i]
    return l


# Simple test
unsorted_list = [7, 23, 1, 45, 6789, 46, 7]
sorted_list = selection_sort(unsorted_list)
print(sorted_list)
natively_sorted = sorted(unsorted_list)
print("The result is the same as natively sorted? %s" % (sorted_list == natively_sorted))


def performance_test(amount):
    print("--------")
    print("Sorting %s numbers" % amount)
    random_list = np.random.choice(100_000, amount, replace=True).tolist()
    start = time.perf_counter()
    sorted_list = selection_sort(random_list)
    print("Selection sort: \t %.2f s" % (time.perf_counter() - start))

    start = time.perf_counter()
    natively_sorted = sorted(random_list)
    print("Native sort: \t\t %.2f s" % (time.perf_counter() - start))
    assert (sorted_list == natively_sorted), "The algorithm has not sorted the list correctly"


for amount in [1_0, 10_000, 20_000, 50_000]:
    performance_test(amount)




