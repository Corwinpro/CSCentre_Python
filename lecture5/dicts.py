# 1.
# Dict initialization
d = dict(foo="bar")
d_ = dict(d)  # is a shallow copy!

# We can copy and add a dict:
d_ = dict(d, boo="baz")

# We can create a dict with some a priory known keys
d_ = dict.fromkeys(["foo", "bar"])  # {'foo': None, 'bar': None}
d_ = dict.fromkeys("abc", 0)  # {'a': 0, 'b': 0, 'c': 0}

# These expressions are not equivalent:
d1 = dict.fromkeys("abcs", [])  # all keys share the same key
d2 = {ch: [] for ch in "abcd "}

# 2.
# Dictionary projections
# We can use len() and 'in' with these projections
d_ = dict.fromkeys(["foo", "bar"], 42)
keys = d.keys()  # dict_keys(['foo', 'bar'])
values = d.values()  # dict_values([42, 42])
items = d.items()  # dict_items([('foo', 42), ('bar', 42)])

# .keys also implements some set features
keys_ = d.keys() & {"foo"}  # {'foo'}

# 3.
# If we for some reasons want to change a dict inplace, create a copy first:
for k in set(d):
    del d[k]
# now d == {}

# 4.
# .get allows us to set default value is key not in dict
# .get only requires one time access to hash table
d = {"foo": "bar"}
d.get("boo", 42)  # 42

# 5.
# Adding elements to dict
# .setdefault changes a value if it doesn't exist
d.setdefault("foo", "????")  # 'bar' - already in the dict
d.setdefault("boo", 42)  # 42

# we can also use .update. It takes any iterable
d = {}
d.update(["foo", "bar"], boo=42)  # {'boo': 42, 'foo': 'bar'}

# 6.
# dicts also have .pop
d.pop("foo") # 'bar'