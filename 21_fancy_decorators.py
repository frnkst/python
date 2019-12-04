# Primer on decorators: https://realpython.com/primer-on-python-decorators/

from lib.fancy_decorators import log_time, log_arguments, slow_down
from functools import partial


@log_time
@log_arguments
def count_to_10(m, optional="test"):
    for i in range(0, 10):
        print(i)


arguments_logger = partial(log_arguments, marker="Customized marker")
@arguments_logger
def count_to_11(m, optional="optional parameter", another_one=42):
    for i in range(0, 11):
        print(i)


@slow_down
def count_to_5():
    for i in range(0, 5):
        print(i)


slow_down_by_five_seconds = partial(slow_down, delay=5)
@slow_down_by_five_seconds
def count_to_5_slowed_down_by_5():
    for i in range(0, 5):
        print(i)


count_to_10(5, optional="optional parameter")
count_to_11("this is a input parameter", optional="optional parameter", another_one=43)
count_to_5()
count_to_5_slowed_down_by_5()



