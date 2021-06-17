K = int(input())
if K%9!=0:
  print(0)
else:
  l = [1 for i in range(K+1)]
  for k in range(1, K+1):
    l[k] = sum(l[max(0, k-9): k]) % 1_000_000_007
  print(l[K])
