# 1.
# We can easily create lists with '*'

chunks = [[0]] * 2

# The problem here is that if we do this:
chunks[0][0] = 42
print(chunks)  # [[42], [42]]
# We actually copy a link, not an element. Both elements point to the same object

# This is a better way, using lists generator:
chunks = [[0] for i in range(2)]

# 2.
# We can use append append to add to a list,
xs = [1, 2, 3]
xs.append(42)  # ==> [1,2,3,4]
# Additionally, we can use 'extend' that can take an iterable
xs.append({-1, -2})  # ==> [1,2,3,4,-2,-1]

# We can insert an element by index using insert
xs = [1, 2, 3]
xs.insert(0, 4)  # ==> [4,2,3,4]
xs.insert(-1, 42)  # ==> [4,2,3,4,42]

# 3.
# We can change list by slice
xs = [1, 2, 3]
xs[:2] = [0] * 2  # ==> [0, 0, 3]

# 4.
# In contrast to tuples, lists support inplace concatenation
xs, ys = [1, 2], [3]
id_xs = id(xs)
xs += ys  # sort of a similar to xs = xs.extend(ys)
print(id(xs) == id_xs)  # True

# Look at this:
xs = []


def f():
    # xs += [42] # doesn't work without non local
    xs.append(42)  # works


# 5.
# We can delete elements in list with del
xs = [1, 2, 3]
del xs[:2]  # xs is not [3]
del xs[:]  # xs is not []

# Sometimes we might want to get the removed item
xs = [1, 2, 3]
pop = xs.pop(1)  # pop is 2, xs is [1,3]

# Or remove the first appearence of an element in list
xs = [1, 1, 0]
xs.remove(1)  # xs becomes [1,0]

# 6.
# We can also reverse a list inplace
xs = [1, 2, 3]
xs.reverse()  # returns None. The list was reversed inplace!

# 7.
# Same applies for sort
xs.sort()  # returns None. The list was sorted inplace!

# sort also takes a key function
xs = [3, 2, 1]
xs.sort(key=lambda x: x % 2, reverse=True)  # xs becomes [3,1,2]

# An interesting example. We want to sort ascending on first component,
# and descending on second component
xs = [[1, 2], [1, 4]]
import functools


def my_comparator(x, y):
    if x[0] != y[0]:
        return x[0] - y[0]
    else:
        return y[1] - x[1]


xs.sort(key=functools.cmp_to_key(my_comparator))  # [[1, 4], [1, 2]]

