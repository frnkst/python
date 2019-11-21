# --------------------------------------------------------------
# Ten million numbers in 99.85 seconds (native is 3.30 seconds)
#
# Things I learned:
#   - // operator, divides and cuts of the decimal
#   - concat lists: list_1 += list_2
#   - Recursion
#   - Merge sort is fast
#   - https://medium.com/@amirziai/merge-sort-walkthrough-with-code-in-python-e4f76d90a4ea
# --------------------------------------------------------------

import time
import numpy as np


def split(list):
    mid_point = len(list) // 2
    return list[:mid_point], list[mid_point:]


def merge_sorted_lists(list_left, list_right):
    # Special case: If one or both lists are empty
    if len(list_left) == 0:
        return len(list_right)
    if len(list_right) == 0:
        return list_left

    index_left = index_right = 0
    merged_list = []

    target_list_length = len(list_left) + len(list_right)
    while len(merged_list) < target_list_length:
        if list_left[index_left] < list_right[index_right]:
            merged_list.append(list_left[index_left])
            index_left += 1
        else:
            merged_list.append(list_right[index_right])
            index_right += 1

        if index_right == len(list_right):
            merged_list += list_left[index_left:]
            break
        elif index_left == len(list_left):
            merged_list += list_right[index_right:]
            break
    return merged_list


def merge_sort(list):
    if len(list) <= 1:
        return list
    else:
        left, right = split(list)
        return merge_sorted_lists(merge_sort(left), merge_sort(right))


# Quick check
unsorted_list = [7, 23, 1, 45, 6789, 46, 7]
sorted_list = merge_sort(unsorted_list)
natively_sorted = sorted(unsorted_list)
assert (sorted_list == natively_sorted), "The algorithm has not sorted the list correctly"


# Performance test
def performance_test(amount):
    print("--------")
    print("Sorting %s numbers" % amount)
    random_list = np.random.choice(100_000, amount, replace=True).tolist()
    start = time.perf_counter()
    sorted_list = merge_sort(random_list)
    print("Selection sort: \t %.2f s" % (time.perf_counter() - start))

    start = time.perf_counter()
    natively_sorted = sorted(random_list)
    print("Native sort: \t\t %.2f s" % (time.perf_counter() - start))
    assert (sorted_list == natively_sorted), "The algorithm has not sorted the list correctly"


for amount in [10_000, 100_000, 1_000_000, 10_000_000]:
    performance_test(amount)
