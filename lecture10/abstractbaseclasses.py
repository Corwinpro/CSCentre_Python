import abc


class Iterable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __iter__(self):
        pass


class Something(Iterable):
    pass


try:
    Something()
except TypeError:
    print(
        "TypeError: Can't instantiate abstract class Something with abstract methods __iter__"
    )

# The problem is that we only know about the problem after we create an instance of a class
