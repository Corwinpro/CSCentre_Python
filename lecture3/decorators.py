# Trace just prints out the function and the args of this function
def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return inner


# These two approaches are equivalent
@trace
def foo():
    return 42


# is the same as dooing this:
def foo():
    return 42


foo = trace(foo)
# Here by foo we get something that trace returns

# Let's apply the trace decorator to an identity function
@trace
def identity(x):
    "I do nothing useful."
    return x


identity(42)
# will return 42 and print 'identity (42,) {}'

"""
There is a problem here.
If we just created a function 'identity' without the @trace decorator,
we would be able to see this:
identity.__name__, identity.__doc__ == 'identity', 'I do nothing useful.'
Although with this form of the decorator we will get:
identity.__name__, identity.__doc__ == 'trace', None

We can use a functools module to update the initial function attributes:
"""
import functools


def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    functools.update_wrapper(inner, func)
    return inner


# Or, this also can be done with a functools.wraps decorator itself
def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return inner


# Now we want to be able turn on and off the trace decorator.
trace_enabled = True


def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return inner if trace_enabled else func


# This happends during the byte code compilation so the def inner thing won't happen if trace_enabled is false

"""
Next step, we can add arguments to the decorator.
@trace(sys.stderr) ===  def identity(x):
def identity(x):            return x
    return x	        deco = trace(sys.stderr)
                        identity = deco(identity)
"""


def square(func):
    return lambda x: func(x * x)


def add(func):
    return lambda x: func(x + 42)


@square
@add
def id(x):
    print(x)
    return x
