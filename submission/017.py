# only question 1

from sys import stdin
input = stdin.readline

N, M = list(map(int,input().split()))

t_dp = [0 for i in range(N+1)]
s_dp = [0 for i in range(N+1)]

q = [list(map(int,input().split())) for i in range(M)]

cnt = 0
for i in range(0, M-1):
  for j in range(i+1, M):
    l1, r1 = q[i]
    l2, r2 = q[j]
    if l1 < l2 < r1 < r2 :
      cnt += 1
    elif l2 < l1 < r2 < r1:
      cnt +=1
print(cnt)
