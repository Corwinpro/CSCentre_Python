# 1.
# Basic operations with sets

xs, ys, zs = {1, 2}, {2, 3}, {3, 4}
set.union(xs, ys, zs)  # xs | ys | zs {1,2,3,4}
set.intersection(xs, ys, zs)  # xs & ys & zs set{}
set.difference(xs, ys, zs)  # xs - ys - zs {1}

# 2.
# Comparison methods
xs.isdisjoint(ys)  # False, has joint element 2
xs <= ys  # Falss
xs < xs  # False
xs | ys >= xs  # True xs AND ys includes xs

# 3.
# Adding elements to set
seen = set()
seen.add(42)  # {42}
seen.update([1, 2])  # {1, 2, 42}

# update can take lots of things
seen.update([], [1], [2], (3, 4))  # {1, 2, 3, 4, 42}

# 4.
# We can remove elements
seen.remove(4)  # If element doesn't exist, throws an error
seen.remove(100500)  # Only removes if an element exists

# 5.
# We can't make a set of sets, like {set(), set()} ==> unhashable type: 'set'
# We can use frozen sets instead. They are immutable
frozen = {frozenset(), frozenset()}
