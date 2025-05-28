n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
from collections import defaultdict

D = defaultdict(list)
for u, v in A:
  D[u].append(v)

print(D)
print(D[3])