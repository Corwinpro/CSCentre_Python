from collections import Counter

# Counter can count anything hashable
# It is a special version of dict
c = Counter(["foo", "foo", "foo", "bar"])
print(c)  # Counter({'foo': 3, 'bar': 1})

c["foo"] += 1  # Counter({'foo': 4, 'bar': 1})

c.pop("foo")  # returns 4
boo = c["boo"]  # 0, doesn't raise exceptions

# negative countered elements are ignored
c = Counter(foo=4, bar=-1)

# We can access elements
list(c.elements())  # ['foo', 'foo', 'foo', 'foo']
most_common = c.most_common(1)  # [('foo', 4)]

# We can update Counter
c.update(["bar"])  # c becomes Counter({'foo': 4, 'bar': 0})

# and subtract as well
c.subtract({"foo": 2})  # Counter({'foo': 2, 'bar': 0})

# We can use counters as multisets
c1 = Counter(foo=4, bar=-1)
c2 = Counter(foo=2, bar=2)

c3 = c1 + c2  #  Counter(foo=6, bar=1)
c4 = c1 - c2  # Counter(foo=2)
c5 = c1 & c2  # Counter(foo=2), min(c1[k], c2[k])
c6 = c1 | c2  # Counter(foo=4, bar=2), max(c1[k], c2[k])

# Any binary operation results in a Counter with positive valued frequencies
