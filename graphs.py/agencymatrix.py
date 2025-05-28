n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

M = []
for i in range(n):
  M.append([0] * n)

for u, v in A:
  M[u][v] = 1

for row in (M):
  print(row)