n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
from collections import defaultdict

D = defaultdict(list)
for u, v in A:
  D[u].append(v)

source = 0

from collections import deque

seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
  node = q.popleft()
  print(node)
  for nei_node in D[node]:
    if nei_node not in seen:
      seen.add(nei_node)
      q.append(nei_node)