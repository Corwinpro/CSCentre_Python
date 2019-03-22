# We can send something inside generator with .send
# Example:
def g():
    res = yield
    print("Got {!r}".format(res))
    res = yield 42
    print("Got {!r}".format(res))


gen = g()  # On 0th instruction in g
next(gen)  # === gen.send(None)
gen.send("foobar")  # Got 'foobar', returns 42


def g2():
    try:
        yield 42
    except Exception as e:
        yield e


gen = g2()
next(gen)  # 42
gen.throw(ValueError, "something is wrong")  # ValueError: something is wrong
gen.throw(RuntimeError, "another error")
