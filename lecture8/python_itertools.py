# 1.
# islice : i means iterator.
from itertools import islice

# islice takes an iterable plus a regular slice arguments
xs = range(10)
list(islice(xs, 3))  # == xs[:3] [0, 1, 2]
list(islice(xs, 3, None))  # xs[3:] [3, 4, 5, 6, 7, 8, 9]
list(islice(xs, 3, 8, 2))  # xs[3:8:2] [3, 5, 7]
list(islice(xs, None, None, 2))  # [0, 2, 4, 6, 8]

# 2.
# Infinite iterators
# For convenience lets implement a function which takes a positive number n
# and a iterable, and return a list of first n elements from the iterable
def take(n, iterable):
    return list(islice(iterable, n))


from itertools import count, cycle, repeat

take(3, count(0, 5))  # [0, 5, 10]
take(4, cycle([1, 2, 3]))  # [1, 2, 3, 1]
take(2, repeat(42))  # [42, 42]
take(3, repeat(42, 2))  # [42, 42] not infinite

# 3.
# dropwhile and take while drop and take iterable when predicat is True
from itertools import dropwhile, takewhile

list(dropwhile(lambda x: x < 5, range(10)))  # [5, 6, 7, 8, 9]
list(takewhile(lambda x: x < 5, range(10)))  # [0, 1, 2, 3, 4]

# 4.
# chain: can be used to merge files
from itertools import chain

take(5, chain(range(2), range(5, 10)))  # [0, 1, 5, 6, 7]

# we can concatenate iterator of iterators with chain.from_iterable
it = (range(x, x ** x) for x in range(2, 4))
take(5, chain.from_iterable(it))  # [2, 3, 3, 4, 5]

# chain.from_iterable is different from chain(*it):
# unpacking evaluates the arguments, and what if x is infinite?

# 5.
# tee creates N independent copies of an iterable
from itertools import tee

it = range(3)
a, b, c = tee(it, 3)  # a, b, c are independent

# This code creates problems:
it = iter(range(3))  # range is an iterable, and iter() creates a iterator
a, b = tee(it, 2)
used = list(it)
list(a), list(b)  # ([], []) - we have already used iterable it with 'used'!

# 6.
# combinatorics
from itertools import product, permutations, combinations, combinations_with_replacement

list(product("AB", repeat=2))  # [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
list(permutations("AB"))  # [('A', 'B'), ('B', 'A')]
list(combinations("ABC", 2))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
list(combinations_with_replacement("ABC", 2))  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

