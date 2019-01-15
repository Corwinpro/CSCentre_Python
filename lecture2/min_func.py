# Arguments
def min(*args):
    res = float("inf")
    for arg in args:
        if arg < res:
            res = arg
        return res


def bounded_min(first, *args, lo=float("-inf"), hi=float("inf")):
    res = hi
    for arg in (first,) + args:
        if arg < res and lo < arg < hi:
            res = arg
    return max(res, lo)


# Fabric of bounded_min function
def make_min(*, lo, hi):
    def inner(first, *args):
        res = hi
        for arg in (first,) + args:
            if arg < res and lo < arg < hi:
                res = arg
        return max(res, lo)

    return inner


bounded_min = make_min(lo=0, hi=225)
print(bounded_min(-5, 12, 13))

# Unpacking examples
first, *rest = range(1, 5)  # 1, [2,3,4]
first, *rest, last = range(1, 5)  # 1, [2,3], 4
*_, (first, *rest) = [range(1, 5)] * 5  # first will be 1

for a, *b in [range(4), range(2)]:
    print(b)
# [1,2,3]
# [1]

default_setup = {"host": "0.0.0.0", "port": 8080}
{**default_setup, "port": 80}  # Rewrites the default value of 'port'


# Nonlocal objects
def cell(value=None):
    def get():
        return value

    def set(update):
        nonlocal value
        value = update

    return get, set


get, set = cell()
print(get())
set(42)
print(get())
