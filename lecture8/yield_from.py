# We had chain early on
def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item


# We can deligate execution to another generator
def new_chain(*iterables):
    for iterable in iterables:
        yield from iterable


# Now .send and .throw of parent generator will
# be deligated to the internal generator without
# any changes
