# There is no ordering in regular dicts
from collections import OrderedDict

d = OrderedDict([("foo", "bar"), ("boo", 42)])
print(list(d))

# When we change values by key, the order doesn't change
d["boo"] = "???"
d["bar"] = "???"
print(list(d))  # ['foo', 'boo', 'bar']

