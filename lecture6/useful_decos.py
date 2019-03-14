import functools


def singleton(cls):
    instance = None

    @functools.wraps(cls)
    def inner(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return inner


@singleton
class Noop:
    """Doing nothing"""

    pass


print(id(Noop()), id(Noop()))  # same IDs for two instances

import warnings


def deprecated(cls):
    orig_init = cls.__init__

    @functools.wraps(cls.__init__)
    def new_init(self, *args, **kwargs):
        warnings.warn(cls.__name__ + " is deprecated.", category=DeprecationWarning)
        orig_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls


@deprecated
class Counter:
    def __init__(self, initial=0):
        self.value = initial


c = Counter() # throws a deprecation warning
