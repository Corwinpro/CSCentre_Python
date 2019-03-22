"""
Here we want to create a decorator which takes some arguments
It should work something like this:
deco = trace(some args...)
f = deco(f)
"""
import functools
import sys


def trace(handle):
    """
    This is a brute-force implementation of a decorator with argument,
    which has three levels of 'nesting'.
    trace() should return a decorator: a func that takes another func
    """

    def decorator(func):
        # A decorator takes a function that returns a wrap around it
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs, file=handle)
            return func(*args, **kwargs)

        return inner

    return decorator


"""
Instead of doing this every single time, we can create a decorator for decorators
Main logic:
with_arguments: deco -> wrapper
wrapper: arguments -> decorator
decorator: func -> deco(func, arguments)

with_arguments: deco -> deco(func, arguments)
"""


def with_arguments(deco):
    """
    with_arguments() is applied to a decorator 'deco' and returns a decorator
    with_arguments: deco -> deco
    """

    @functools.wraps(deco)
    def wrapper(*dargs, **dkwargs):
        def decorator(func):
            result = deco(func, *dargs, **dkwargs)
            functools.update_wrapper(result, func)
            return result

        return decorator

    return wrapper


"""
This is how it works. The new decorator with_arguments allows us to:

def func(): ...
def trace(func, arg): ...
trace = with_arguments(trace)
func = trace(arg)(func) <==>    @trace(arg)
                                def func():...
"""


@with_arguments
def trace(func, handle):
    """
    trace() takes a decorated function AND an argument
    """

    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs, file=handle)
        return func(*args, **kwargs)

    return inner


@trace(sys.stderr)
def identity(x):
    return x


"""
There's a better way how to handle the decorators with kw only arguments case.
A magical way.
"""


def trace(func=None, *, handle=sys.stdout):
    # This is called when we call trace with argument,
    # ...@trace(handle = sys.stderr)
    # In this case func default value will not be overwritten
    if func is None:
        return lambda f: trace(f, handle=handle)

    # Otherwise, when there exists a positional argument,
    # we actually apply the decorator, this happens
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs, file=handle)
        return func(*args, **kwargs)

    return inner


# And this is how this method works (with kwargs only):
@trace(handle=sys.stderr)
def identity(x):
    return x
