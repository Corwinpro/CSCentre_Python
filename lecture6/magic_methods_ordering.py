# According to docs, we need to implement all 6 comparison operators
# A cheat here: functools

import functools

# Only two methods are now required
@functools.total_ordering
class Counter:
    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value
