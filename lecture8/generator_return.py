# We can use return in generators
# It means: "I have nothing else left, take this."
def g():
    yield 42
    return []


gen = g()
next(gen)  # 42
next(gen)  # StopIteration: []

# return != raise StopIteration
# Nothing will happen here, as we catch the exception
# return would raise anyway
def g2():
    try:
        yield 42
        raise StopIteration([])  # != return
    except Exception:
        pass


# When we might need this:
# if we want to use yield from as an expression


def g3():
    res = yield from g()
    print("Got {!r}".format(res))


gen = g3()
next(gen)  # 42
next(gen, None)  # 'Got []'

