N, L = list(map(int,input().split()))
K = int(input())
A = [0] + list(map(int,input().split()))+[L]
A = [A[i+1]-A[i] for i in range(N+1)]

def check(M):
  """greedy search"""
  stack = 0
  count = 0
  for a in A:
    stack += a
    if stack >= M:
      stack = 0
      count += 1
  else:
    if stack >= M:
      count += 1  
      
  if count >= K+1:
    return True
  else:
    return False

r = (0, L+1)

while r[1] - r[0] > 1:
  l = r[1] - r[0]
  candidate = (r[1]+r[0])//2
  # print(candidate,check(candidate),search_range[0],search_range[-1])
  if check(candidate):
    r = (candidate, r[1])
  else:
    r = (r[0], candidate)
if check(r[1]):
  print(r[1])
else:
  print(r[0])