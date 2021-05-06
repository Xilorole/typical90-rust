from sys import stdin
input = stdin.readline
import bisect

N = int(input())
A = sorted(set(map(int,input().split())))
Q = int(input())
B = [int(input()) for q in range(Q)]

for b in B:
  idx = bisect.bisect_left(A, b)
  if idx == len(A):
    idx -= 1
  r = A[idx]
  if idx != 0:
    l = A[idx-1]
    print(min(abs(r-b),abs(l-b)))
  else:
    print(abs(r-b))