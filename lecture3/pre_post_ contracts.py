"""
Pre and post decorators allow us to condition the inputs and outputs of functions
"""
# from contracts import pre, post
import math
import functools


def pre(cond, message):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)

        return inner

    return wrapper


@pre(lambda x: x >= 0, "negative argument")
def checked_log(x):
    pass


def post(cond, message):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            assert cond(result), message
            return result

        return inner

    return wrapper


is_not_nan = post(lambda r: not math.isnan(r), "not a number")


@is_not_nan
def smth():
    pass
