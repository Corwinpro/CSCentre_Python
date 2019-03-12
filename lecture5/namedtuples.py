from collections import namedtuple

# 1.
# nametuple generates a class. In general, we may call the returned obj of namedtuple as we want
# namedtuple(typename, field_names, ...)
Person = namedtuple("Person", ["name", "age"])

# first arg is name, then age
p = Person("George", age=77)
print(p.name, p.age)

# 2.
# We can use special methods with namedtuples
p_dict = p._asdict()
print(p_dict)  # OrderedDict([('name', 'George'), ('age', 77)])

p_replaced = p._replace(name="Bill") # returns a new tuple with changed fields
print(p_replaced)

# 3.
# We should use namedtuples for everything. Anytime we want to use tuple, use nametuple.
# Otherwise we don't need a tuple.
# They are basically lightweighted classes