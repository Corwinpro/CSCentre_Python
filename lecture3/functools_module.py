import functools


# functools lru_cache stores last maxsize calls results
# If maxsize == None, it becomes a simple memoized


@functools.lru_cache(maxsize=64)
def ackermann(m, n):
    if not m:
        return n + 1
    elif not n:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(3, 4))
print(ackermann.cache_info())

"""
Another useful functools function is singledispatch.
It creates a generic function, in our example it is obj -> binary string.
"""


@functools.singledispatch
def pack(obj):
    type_name = type(obj).__name__
    assert False, "Unsupported type: " + type_name


@pack.register(int)
def _(obj):
    return b"I" + hex(obj).encode("ascii")


@pack.register(list)
def _(obj):
    return b"L" + b",".join(map(pack, obj))


functools.reduce(lambda acc, x: acc * x, [1, 2, 3, 4])

