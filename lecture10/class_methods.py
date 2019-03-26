# 1.
# Function are descriptors
class Something:
    def do_something(self):
        pass


Something.do_something  # <function Something.do_something at ...>
Something().do_something  # <bound method Something.do_something at ...>

# How this works? Descriptors!
from types import MethodType


class Function:
    def __get__(self, instance, owner):
        if instance is None:  # calling Class.function
            return self
        else:  # calling Class().function
            return MethodType(self, instance, owner)


# 2.
# @staticmethod
# This is how it works:
class staticmethod:
    def __init__(self, method):
        self._method = method

    def __get__(self, instance, owner):
        return self._method  # We ignore instance


# 3.
# @classmethod
# It is an alternative constructor. It takes whatever *args and **kwargs
import functools


class classmethod:
    def __init__(self, method):
        self._method = method

    def __get__(self, instance, owner):
        return functools.partial(self._method, owner)


class A:
    @classmethod
    def do_smth(cls):
        print("Called with", cls)


A().do_smth()  # we go to get descriptor.__get__

# 4.
# @property
class property:
    def __init__(self, get=None, set=None, delete=None):
        self._get = get
        self._set = set
        self._delete = delete

    def __get__(self, instance, owner):
        if self._get is None:
            raise AttributeError("unreadable attribute")
        return self._get(instance)

    # same __set__ and __delete__
