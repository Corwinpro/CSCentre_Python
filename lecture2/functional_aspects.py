identity = lambda args: args

# Map only returns a map object
# it basically does nothing
map(identity, range(4))

print(list(map(identity, range(4))))

print(set(map(lambda x: x % 7, [1, 9, 16, -1, 2, 5])))

print(list(map(lambda x, n: x ** n, [2, 3], range(1, 8))))

# Filter takes a function with predicat (truthy - value)
# and a collection
# and returns a filter object

f = filter(lambda x: x % 2 != 0, range(10))
print(list(f))

# We can pass None as a predicat
# Filter then will return only truthy values
xs = [0, None, [], {}, set(), "", 42]
print(list(filter(None, xs)))

# Zip 'zips' collections
l = list(zip("abc", range(3), [42j, 42j, 42j]))
print(l)

# And zip doesn't add 'extra' elements
print(list(zip("abs", range(10))))

# Generating dicts
date = {"year": 2019, "month": "January", "date": ""}
print({k: v for k, v in date.items() if v})

