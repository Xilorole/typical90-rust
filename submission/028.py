N = int(input())

M = 1000

dMAP = [[0 for i in range(M+1)] for j in range(M+1)]

for i in range(N):
  lx, ly, rx, ry = list(map(int,input().split()))
  dMAP[lx][ly] += 1
  dMAP[rx][ry] += 1
  dMAP[lx][ry] += -1
  dMAP[rx][ly] += -1

MAP = [[0 for i in range(M)] for j in range(M)]
for i in range(M):
  cnt = 0
  for j in range(M):
    cnt += dMAP[j][i]
    MAP[j][i] += cnt

ansMAP = [[0 for i in range(M)] for j in range(M)]
for j in range(M):
  cnt = 0
  for i in range(M):
    cnt += MAP[j][i]
    ansMAP[j][i] += cnt

from collections import Counter
c = Counter([i for j in ansMAP for i in j])
for i in range(1, N+1):
  print(c[i])
