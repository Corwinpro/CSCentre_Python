# 1.
# We can choose subset in any collection, e.g. a tuple

person = ("George", "Carlin", "May", 12, 1937)

name, birthday = person[:2], person[2:]

print(name), print(birthday)
"""
('George', 'Carlin')
('May', 12, 1937)
"""

# We can avoid having magical constants and name slices

NAME, BIRTHDAY = slice(2), slice(2, None)

print(person[NAME]), print(person[BIRTHDAY])  # This will return the same thing as above

# 2.
# Tuples also work find with 'reversed' function. reversed takes a sequence and
# returns a new one, with the elemetns of the first on in reversed order.

print(tuple(reversed((1, 2, 3))))

# This is equivalent to (1,2,3)[::-1] slice. The reason to use reversed is because slice returns
# a copy of a collection. Reversed doesn't require additional memory

# 3.
# We can concatenate tuples, and it always results in a new tuple

xs, ys = (1, 2), (3,)
print(id(xs), id(ys))
print(id(xs + ys))  # != id(xs) | id(ys)

# 4.
# We can compare tuples like strings
print((1, 2, 3) < (1, 2, 4))  # True
print((1, 2, 3, 4) < (1, 2, 4))  # True
print((1, 2) < (1, 2, 42))  # True
