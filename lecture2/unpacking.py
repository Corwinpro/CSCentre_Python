# Unpacking examples
first, *rest = range(1, 5)  # 1, [2,3,4]
first, *rest, last = range(1, 5)  # 1, [2,3], 4
*_, (first, *rest) = [range(1, 5)] * 5  # first will be 1


for a, *b in [range(4), range(2)]:
    print(b)
# [1,2,3]
# [1]

default_setup = {"host": "0.0.0.0", "port": 8080}
{**default_setup, "port": 80}  # Rewrites the default value of 'port'
