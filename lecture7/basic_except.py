def something_dangerous():
    pass


def something_else_dangerous():
    pass


# 1.
# We go down the except tree and compare the exception we got
# with given types.
# The first argument in except should be comparable with exception
try:
    something_dangerous()
except (ValueError, ArithmeticError):
    pass
except TypeError as e:
    pass

# We can try to catch an exception, do something with it once.
# and if it still exists - just forget about it

try:
    something_dangerous()
except Exception as e:
    try:
        something_else_dangerous()
    except type(e):  # here we try to catch exception from something_else_dangerous
        pass

# 2.
# BaseException is a base class for exception
# Never inheret from BaseException!
print(
    BaseException.__subclasses__()
)  # [<class 'Exception'>, <class 'GeneratorExit'>, <class 'SystemExit'>, <class 'KeyboardInterrupt'>]

"""
3.
AssertionError: is for mistakes that shouldn't exist
We should never catch them

Import error: when we import modules

NameError: when a variable is not defined

AttributeError: when there's no obj attribute with this name to read
or (with __slots__) write

KeyError, IndexError: no element in container

ValueError: when other errors are not applicable
"""

# 4.
# User defined exceptions
class NotesException(Exception):
    """
    This is a basic class for my notes exceptions
    """

    pass


class ScriptException(NotesException):
    """
    This is class for scripts in my lecture notes
    """

    def __str__(self):
        return "script test failed"


# 5.
# What we have in exceptions?
try:
    1 + "42"
except Exception as e:
    caught = e

print(
    caught.args, caught.__traceback__
)  # ("unsupported operand type(s) for +: 'int' and 'str'",) <traceback object at 0x103b0bb48>

import traceback

traceback.print_tb(
    caught.__traceback__
)  # File "lecture7/basic_except.py", line 76, in <module>

"""
6.
raise is to throw exception
raise TypeError("type mismatch") ==> TypeError: type mismatch
                 ^ this is arg

Exceptions chaining:
raise from
We use it when an exception appeared from another exception
try:
  send_email()
except SocketError as e:
  raise RuntimeError("No email sent") from e

SocketError: ...
RuntimeError: "No email sent"
"""

# 7.
# finally
import sys


def write_something(handle):
    pass


try:
    handle = open("example.txt", "wt")
    try:
        write_something(handle)
    finally:
        handle.close()  # We free the resource after use regardless of any exception
except IOError as e:
    print(e, file=sys.stderr)  # We can have an exception while opening the file

# 8.
# else
# If everything is alright and no exception was thrown
def report_success(handle):
    print("Everything is alright with {}".format(handle))


try:
    handle = open("example.txt", "wt")
    # The problem of reporting success here is that we
    # don't want to add extra logic in this block
except IOError as e:
    print(e, file=sys.stderr)
else:
    report_success(handle)

