# Coroutines


def grep(pattern):
    print("Looking for {!r}".format(pattern))
    while True:
        line = yield
        if pattern in line:
            print(line)


gen = grep("Gotcha!")
next(gen)  # Looking for Gotcha!
gen.send("Not the line we want.")
gen.send("The one we want. Gotcha!")  # The one we want. Gotcha!

# One ugly thing here is calling next(gen)
# We can use decorator to solve this

import functools


def coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        next(gen)
        return gen

    return inner


grep = coroutine(grep)
gen = grep("Gotcha!")
gen.send("One more line to catch. Gotcha!")  # One more line to catch. Gotcha!
