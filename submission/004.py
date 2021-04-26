# pypy

H,W = list(map(int,input().split()))
A = [list(map(int,input().split())) for i in range(H)]
AH = [sum(A[i]) for i in range(H)]
AW = [sum(A[h][w] for h in range(H)) for w in range(W)]

for h in range(H):
  print(" ".join([str(AH[h]+AW[w]-A[h][w]) for w in range(W)]))