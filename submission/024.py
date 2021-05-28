N, K =list(map(int, input().split()))
A=list(map(int, input().split()))
B=list(map(int, input().split()))

diff = sum([abs(A[i]-B[i]) for i in range(N)])
if diff <= K and diff%2 == K%2:
  print("Yes")
else:
  print("No")
