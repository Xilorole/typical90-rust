N = int(input())
from collections import defaultdict
tree = defaultdict(set)

for i in range(N-1):
  a, b = list(map(int,input().split()))
  tree[a] |= {b}
  tree[b] |= {a}

odd = set()
even = set()
queue = [(1,0)]
for i in range(N-1):
  q, dist = queue[i]
  if dist %2 == 0:
    even |= {q}
  else:
    odd |= {q}
  for node in tree[q] - even - odd:
    queue.append((node, dist+1))
if len(even) > len(odd):
  print(" ".join(map(str,list(even)[:N//2])))
else:
  print(" ".join(map(str,list(odd)[:N//2])))
