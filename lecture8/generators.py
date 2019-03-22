# Generator is a function with yield operator
# Generator is an iterator built with yield

# 1.
def g():
    print("Started")
    x = 42
    yield x
    x += 1
    yield x
    print("Done")


type(g)  # <class 'function'>
gen = g()  # <class 'generator'>
next(gen)  # Started \n 42
next(gen)  # 43

# 2.
# generator example: unique
def unique(iterable, seen=None):
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


xs = [1, 1, 2, 3]
unique(xs)  # <generator object unique at ...>
list(unique(xs))  # [1, 2, 3]
1 in unique(xs)  # True

# 3.
# map generator
def map(func, iterable, *rest):
    for args in zip(iterable, *rest):
        yield func(*args)


xs = range(5)
map(lambda x: x * x, xs)  # <generator object map at ...>
list(map(lambda x: x * x, xs))  # [0, 1, 4, 9, 16]
9 in map(lambda x: x * x, xs)  # True

# 4.
# chain
def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item


xs = range(3)
ys = [42]
chain(xs, ys)  # <generator object chain at ...>
list(chain(xs, ys))  # [0, 1, 2, 42]
42 in chain(xs, ys)  # True

# 5.
# infinite generator count and enumerate
def count(start=0):
    while True:
        yield start
        start += 1


next(count())  # 0
counter = count()
next(counter)  # 0
next(counter)  # 1


def enumerate(iterable, start=0):
    return zip(count(start), iterable)


next(enumerate(count(42)))  # (0, 42)

# 6.
# close raises a special exception GeneratorExit
def g():
    try:
        yield 42
    finally:
        print("Done")


gen = g()
next(gen)
gen.close()  # Done

