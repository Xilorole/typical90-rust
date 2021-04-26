N = int(input())

def func(patterns, n):
  ret = [] 
  for pattern, cnt, length in patterns:
    if length == N:
      if cnt == 0:
	      ret += [pattern]
    else:
      if cnt > 0:
        ret += func(
          [(pattern+"(", cnt+1, length+1),
           (pattern+")", cnt-1, length+1)],
          n)
      else:
        ret += func([(pattern+"(", cnt+1, length+1)], n)
  return ret

if N%2 == 0:
  for p in func([("(", 1, 1)], N):
    print(p)