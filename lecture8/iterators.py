"""
Iterators protocol has two methods:
- __iter__ : returns class instance, that realises the the iterator protocol
- __next__: returns next iterator's element. If there's no such element, raises StopIteration
"""

# 1.
# iter and next
# iter takes an iterable and returns an iterator (calls __iter__)
# It can also takes a function and calls this function, until it returns a special value

from functools import partial


def do_something(x):
    pass


def iter_example(path):
    """
    This is an example how to use iter and create an iterator
    """
    with open(path, "rb") as handle:
        read_block = partial(handle.read, 64)
        # "" is EOF here and we stop reading when we reach it
        for block in iter(read_block, ""):
            do_something(block)


# next takes an iterator and calls __next__
# it can have a default value for StopIteration exception
next(iter([1, 2, 3]))  # ==> 1
next(iter([]), 42)  # ==> 42

# 2.
# for
# These two bits are conceptually equivalent

xs = [1, 2, 3]
for x in xs:
    do_something(x)
# and
it = iter(xs)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    do_something(x)

# 3.
# in and not in
# these methods use __contains__.
# __contains__ is implemented using iterators

# 4.
# __getitem__
# Python has a simplified version of iterator protocol implementation
# using __getitem__ method
# If we define __getitem__, suddenly the instance has __iter__
class Identity:
    def __getitem__(self, idx):
        if idx > 5:
            raise IndexError
        return idx


id = Identity()
list(id)  # ==> [0, 1, 2, 3, 4, 5]
5 in id  # == id.__contains__(5), True
42 not in id  # True

# This is a 'default' iterator implementation
class seq_iter:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            res = self.instance[self.idx]
        except IndexError:
            raise StopIteration
        self.idx += 1
        return res
