N, Q = list(map(int,input().split()))

S = {i: j for i, j in enumerate(map(int, input().split()))}

offset = -1
for i in range(Q):
  
  q, x, y = list(map(int,input().split()))
  
  x = (x+offset)%N
  y = (y+offset)%N
  
  if q == 1:
    # swap
    temp = S[x]
    S[x] = S[y]
    S[y] = temp
  elif q == 2:
    offset -= 1
  else:
    print(S[x])
