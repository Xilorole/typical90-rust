import sys
sys.setrecursionlimit(10**6+2)

N = int(input())

from collections import defaultdict

edges = defaultdict(set)
query = []
for i in range(N-1):
  w, v = tuple(map(int,input().split()))
  query.append((w,v))
  
  edges[w].add(v)
  edges[v].add(w)

d = dict()
def nodes_on_right(l, r):
  if (l,r) in d:
    return d[(l,r)]
  elif (r,l) in d:
    return d[(r,l)]
   
  ans = 1
  for node in edges[r] - {l}:
    ans += nodes_on_right(r, node)
  d[(r,l)] = d[(l,r)] = ans
  return ans

ans = 0
for w,v in query:
  m = nodes_on_right(w,v)
  ans += m*(N-m)
print(ans)
