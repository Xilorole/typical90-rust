from sys import stdin
input = stdin.readline
N = int(input())
from collections import defaultdict
d = defaultdict(set)

for i in range(N-1):
  a, b = tuple(map(int,input().strip().split()))
  d[a-1] |= {b-1}
  d[b-1] |= {a-1}
def bfs(start):
  v = {0: (start,0)} # index: (node,dist)
  visited = set()
  cnt = 1
  for i in range(N-1):
    dist = v[i][1]
    near_nodes = d[v[i][0]] - visited
    for node in near_nodes:
      v[cnt] = (node, dist+1)
      cnt += 1
    visited |= {v[i][0]}
  return v[N-1]

node, dist = bfs(0)
node, dist = bfs(node)
print(dist+1)