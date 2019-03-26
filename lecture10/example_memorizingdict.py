from collections import deque


class MemorizingDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._history = deque(maxlen=10)

    def __setitem__(self, key, value):
        self._history.append(key)
        return super().__setitem__(key, value)

    def get_history(self):
        return self._history


d = MemorizingDict({"foo": 42})
# ^ _history wasn't even initialized when we __init__ base dict
d.setdefault("bar", 24)
# ^ This bit here doesn't call set item because dict is a C-language structure and doesn't know anything about our methods
d["baz"] = 100500
print(d.get_history())  # deque(['baz'], maxlen=10)

# We have lost two previous keys.

# Summing up. we need to inheret from collections.abc MutableMapping
from collections import abc

issubclass(list, abc.Sequence)  # True
isinstance({}, abc.Hashable)  # False - it is mutable


def flatten(obj):
    for item in obj:
        if isinstance(item, abc.Iterable):
            yield from flatten(item)
        else:
            yield item


list(flatten([[1, 2], 3, [], [4]]))  # [1, 2, 3, 4]
