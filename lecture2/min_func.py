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
