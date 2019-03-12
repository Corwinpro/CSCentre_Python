# A good use case for defaultdict is graphs
# Consider we want to store a graph node-leaves dict
g = {"a": {"b"}, "b": {"c"}}
node1 = g["a"]  # {"b"}

# How can we add connections ("b", "a") and ("c", "a")?
# g["b"].add("a")
# g["c"].add("a") ==> KeyError: 'c'
# since 'c' didn't exist

from collections import defaultdict

# the first argument is a factory
g = defaultdict(set, **{"a": {"b"}, "b": {"c"}})
g["c"].add("a")  # here we called a 'set' constructor
