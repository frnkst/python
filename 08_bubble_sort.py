# Bubble sort
# 11.83 s for 10'000 random numbers (0.00 s when using native time sort ;)

import random
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

# Ten thousand numbers
random_list = random.sample(range(10_000), 10_000)

start = time.perf_counter()
sorted_list = bubble_sort(random_list)
print("Sorted with bubble sort in %.2f s" % (time.perf_counter() - start))

start = time.perf_counter()
natively_sorted = sorted(random_list)
print("Sorted with native time sort in %.2f s" % (time.perf_counter() - start))

print("The result is the same as natively sorted? %s" % (natively_sorted == sorted_list))
