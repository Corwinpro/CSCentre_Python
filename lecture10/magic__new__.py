# 1.
# __init__ is not a constructor
# __new__ takes class and arguments and create a class instance
# __init__ takes an instance and initializes it


class Noop:
    def __new__(cls, *args, **kwargs):  # is in face a static method
        print("Creating instance with {} and {}".format(args, kwargs))
        instance = super().__new__(cls)
        return instance

    def __init__(self, *args, **kwargs):
        print("Initializing instance with {} and {}".format(args, kwargs))


noop = Noop(42, attr="value")

# 2.
# A useless metaclass
from collections import OrderedDict


class UselessMeta(type):
    def __new__(metacls, name, bases, clsdict):
        print(type(clsdict))
        print(list(clsdict))
        cls = super().__new__(metacls, name, bases, clsdict)
        return cls

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()


class Something(metaclass=UselessMeta):
    attr = "foo"
    other_attr = "bar"
