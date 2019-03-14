class Counter:
    """I just count."""

    all_counters = []

    def __init__(self, initial=0):
        Counter.all_counters.append(self)
        self.value = initial

    def increment(self):
        self.value += 1

    def get(self):
        return self.value


# This is a mixin class. We won't use its instances,
# but only use it as a parent class.


def dummy_get_lock():
    return 0


class ThreadSafeMixin:
    """
    We expect the the class we mix in ThreadSafeMixin to
    has .increment() and .get() implemented, and these
    methods will be called with super()
    """

    get_lock = dummy_get_lock

    def increment(self):
        with ThreadSafeMixin.get_lock():
            super().increment()

    def get(self):
        with ThreadSafeMixin.get_lock():
            return super().get()


class ThreadSafeCounter(ThreadSafeMixin, Counter):
    pass


# We can do the same thing with decorator
def thread_safe(cls):
    orig_increment = cls.increment
    orig_get = cls.get

    def increment(self):
        with self.get_lock():
            orig_increment(self)

    def get(self):
        with self.get_lock():
            return orig_get(self)

    cls.get_lock = dummy_get_lock
    cls.increment = increment
    cls.get = get

    return cls

