import time
from functools import wraps

marker = "DEBUG:"


def log_time(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter() - start
        print("%s '%s' took %.4f seconds" % (marker, func.__name__, end))
        return value
    return wrapper_decorator


# This decorator has an optional parameter 'marker'. To set it, a new parameterized
# decorator needs to be created where it's being used:
#
# arguments_logger = partial(log_arguments, marker="Customized marker")
#
# Now either the generic decorator @log_arguments, or the parameterized one
# @arguments_logger can be used.
def log_arguments(func, marker=marker):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        print("%s '%s' was called with %s" % (marker, func.__name__, signature))
        value = func(*args, **kwargs)
        print("%s '%s' returned %s" % (marker, func.__name__, value))
        return value

    return wrapper_decorator


def slow_down(func, delay=1):
    def wrapper_decorator(*args, **kwargs):
        time.sleep(delay)
        return func(*args, **kwargs)

    return wrapper_decorator
