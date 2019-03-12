from collections import deque

# 1.
# With deque, add and delete from both sides works as O(1),
# indexing is O(n)

q = deque([1, 2, 3])
q.appendleft(0)  # [0, 1, 2, 3]
q.append(4)  # [0, 1, 2, 3, 4]
q.popleft()  # returns 0. pop(0) works O(n)

# 2.
# We can specify max len
q = deque([1, 2], maxlen=2)
q.appendleft(0)  # [0, 1] (->2 leaves)
q.append(2) # [1,2] (0<- leaves)