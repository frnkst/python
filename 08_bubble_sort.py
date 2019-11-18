# Bubble sort
# 12.29 ms for 10'000 random numbers (0.00 ms when using time sort ;)

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

# A hundred thousand numbers
random_list = random.sample(range(10_000), 10_000)

start = time.time()
sorted_list = bubble_sort(random_list)
print("Sorted with bubble sort in %.2f ms" % (time.time() - start))

start = time.time()
natively_sorted = sorted(random_list)
print("Sorted with time sort in %.2f ms" % (time.time() - start))

print("The result is the same as natively sorted? %s" % (natively_sorted == sorted_list))
