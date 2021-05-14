N, M = list(map(int,input().split()))

from collections import defaultdict
from heapq import heappush, heappop

graph = defaultdict(set)
dist = dict()

dist_from_1 = defaultdict(lambda : float("inf"))
dist_from_N = defaultdict(lambda : float("inf"))

for i in range(M):
  a, b, c = list(map(int,input().split()))
  graph[a] |= {b}
  graph[b] |= {a}
  dist[(a,b)] = dist[(b,a)] = c
  
h = []
heappush(h, (0, 1)) # (dist-to-node, node-index)
while len(h) > 0:
  dist_to_node, node_idx = heappop(h)
  if dist_to_node < dist_from_1[node_idx]: # 更新されなかったら計算する必要もないのでスキップ
    dist_from_1[node_idx] = dist_to_node 
  else:
    continue
  for next_node in graph[node_idx]:
    if dist_to_node + dist[(node_idx, next_node)] < dist_from_1[next_node]:
      heappush(h, (dist_to_node + dist[(node_idx, next_node)] ,next_node))

heappush(h, (0, N)) # (dist-to-node, node-index)
while len(h) > 0:
  dist_to_node, node_idx = heappop(h)
  if dist_to_node < dist_from_N[node_idx]:
    dist_from_N[node_idx] = dist_to_node
  else:
    continue
  for next_node in graph[node_idx]:
    if dist_to_node + dist[(node_idx, next_node)] < dist_from_N[next_node]:
      heappush(h, (dist_to_node + dist[(node_idx, next_node)] ,next_node))
      

for i in range(1,N+1): print(dist_from_1[i] + dist_from_N[i])
