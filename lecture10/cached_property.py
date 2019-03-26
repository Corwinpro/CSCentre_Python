# Sometimes calling __get__ is expensive, so we want to cache this data
# For this reason we have NonDataDescriptors


class cached_property:
    def __init__(self, method):
        self._method = method

    def __get__(self, instance, owner):
        if instance is None:
            return self  # if we call A.f - return descriptor itself
        value = self._method(instance)
        setattr(instance, self._method.__name__, value)
        return value


class A:
    @cached_property
    def f(self):
        print("Computed")
        return 42


a = A()
a.f  # 'Computed', 42
a.f  # 42
