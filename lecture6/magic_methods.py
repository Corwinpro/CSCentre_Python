# 1.
# __getattr__ is called only when there's no such class attribute


class Noop:
    pass


# Noop().foo ==> AttributeError


class Noop2:
    def __getattr__(self, name):
        return name  # identity


# Noop2().foo ==> 'foo'

# 2.
# __setattr__ and __getattr__ are called for all attributes


class Guarded:
    guarded = []

    def __setattr__(self, name, value):
        assert name not in self.guarded
        return super().__setattr__(name, value)


# We can still hack the guarded behavior if we write by
# __dict__ of a class, since __setattr__ won't be called
class GuardedNoop(Guarded):
    guarded = ["foo"]

    def __init__(self):
        self.__dict__["foo"] = 42


# 3.
# getattr, setattr, delattr work conceptually the same as __*__ methods


class Noop3:
    some_attr = 42


noop = Noop3()
getattr(noop, "some_attr")  # ==> 42
getattr(noop, "some_other_attr", 100500)  # ==> 100500, default value like .get in dicts

# setattr is usefull when the attribute name is a string
setattr(noop, "some_other_attr", 100501)
delattr(noop, "some_other_attr")
