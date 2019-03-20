"""
We can write this typical resource management pattern
r = acquire_resource()
... try:
...   do_something(r)
... finally:
...   release_resource(r)

using context manager
... with acquire_resource() as r:
...   do_something(r)

acquire_resource is a Context Manager and has two methods:
- __enter__: initializes the context, e.g. opens a file
    returns smth and writes it to the variable right to the 'as'
- __exit__: is called after 'with' execution. Has three arguments:
    exception_type, exception, traceback_object
If during the 'with' execution an exception was raised, we can catch it
if __exit__ returns True

"""
# 1.
# Semantics

with acquire_resource() as r:
    do_something(r)

# is semantically equivalent to

manager = acquire_resource()
r = manager.__enter__()
try:
    do_something(r)
finally:
    exc_type, exc_value, tb = sys.exc_info()
    suppress = manager.__exit__(exc_type, exc_value, tb)
    if exc_value is not None and not suppress:
        raise exc_value

# 2.
# Multiple with
with acquire_resource() as r, acquire_another_resource() as other:
    do_something(r, other)
