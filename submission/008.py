N = int(input())
mod = int(1e9) + 7
S = input()
A = [0] * len("atcoder")

for s in S:
  for i, ch in enumerate(reversed("atcoder")):
    if s == ch:
      if i == len("atcoder") - 1:
        A[0] += 1
      else:
        A[-i-1] += A[-i-2]
    A[i] = A[i] % mod
print(A[-1])