# Method __call__ allows us to 'call' class instances
# like functions interface
import functools
import sys


class Identity:
    def __call__(self, x):
        return x


Identity()(42)  # ==> 42

# This is useful when we want to crete decorators with arguments
class trace:
    def __init__(self, handle):
        self.handle = handle

    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs, file=self.handle)
            return func(*args, **kwargs)

        return inner


@trace(sys.stderr)
def identity(x):
    return x
