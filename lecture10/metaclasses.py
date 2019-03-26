# 1.
# Metaclasses generate classes


class Something:
    attr = 42


Something  # <class __main__.Something>
type(Something)  # <class 'type'>

# This is equivalent to
name, bases, attrs = "Something", (), {"attr": 42}
Something = type(name, bases, attrs)
Something  # <class __main__.Something>
type(Something)  # <class 'type'>

some = Something()
some.attr  # 42

# 2.
# How to use them?
# Default metaclass is type. We can change that.
class Meta(type):
    def some_method(cls):
        return "foobar"


class SomethingElse(metaclass=Meta):
    attr = 42


type(SomethingElse)  # <class '__main__.Meta'>
SomethingElse.some_method  # <bound method Meta.some_method of <class >>
try:
    SomethingElse().some_method
except AttributeError as e:
    print(
        "some_method is method of SomethingElse as a instance of Meta. We can't call it from SomethingElse instance"
    )

# 3.
# Creating classes and how Metaclass is built-in into it
class Base:
    pass


class A(Base, metaclass=Meta):
    def __init__(self, attr):
        self.attr = attr

    def do_something(self):
        pass


# First, we create a dict for class
clsdict = Meta.__prepare__("A", (Base,))
body = """
def __init__(self, attr):
    self.attr = attr

def do_something(self):
    pass
"""
# Second, call exec. After calling exec() the dict clsdict has all methods and attributes of the class
exec(body, globals(), clsdict)
# Third, create class object by calling meta class:
A = Meta("A", (Base,), clsdict)
# Done! We produced a class
