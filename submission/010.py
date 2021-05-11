from sys import stdin
input = stdin.readline

N = int(input())
C1 = [0 for i in range(N+1)]
C2 = [0 for i in range(N+1)]

for i in range(1, N+1):
  C, P = list(map(int,input().split()))
  C1[i] = C1[i-1]
  C2[i] = C2[i-1]
  if C == 1: C1[i] += P
  else: C2[i] += P
  
Q = int(input())
for q in range(Q):
  L, R = list(map(int,input().split()))
  print(f"{C1[R]-C1[L-1]} {C2[R]-C2[L-1]}")
