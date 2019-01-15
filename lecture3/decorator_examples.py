import functools
import time
import warnings


def timethis(func=None, *, n_iter=100):
    if func is None:
        return lambda f: timethis(f, n_iter=n_iter)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, end=" ... ")
        acc = float("inf")
        for i in range(n_iter):
            tick = time.perf_counter()
            result = func(*args, **kwargs)
            acc = min(acc, time.perf_counter() - tick)
        print(acc)
        return result

    return inner


# result = timethis(sum)(range(10))


def profiled(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.ncalls += 1
        return func(*args, **kwargs)

    inner.ncalls = 0
    return inner


@profiled
def identity(x):
    return x


# identity(42); print(identity.ncalls)


def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True

    inner.called = False
    return inner


@once
def initialize_settings():
    print("Setting initialized.")


# initialize_settings(); initialize_settings()


def memoized(func):
    cache = {}

    @functools.wraps(func)
    def inner(*args, **kwargs):
        # We can't use dict here for arguments. Dict is not hashable
        # This won't work
        # key = args, kwargs
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return inner


def depricated(func):
    # The problem here is that the warning will appear when the module is loaded
    # Not the function call
    code = func.__code__
    warnings.warn_explicit(
        func.__name__ + "is depricated.",
        category=DeprecationWarning,
        filename=code.co_filename,
        lineno=code.co_firstlineno + 1,
    )
    return func
