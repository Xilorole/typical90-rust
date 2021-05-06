N = int(input())

def check(candidate):
  cnt = 0
  for char in candidate:
    if char == "(":
      cnt += 1
    else:
      cnt -= 1
    if cnt < 0:
      return False
  if cnt == 0:
    return True
  else:
    return False

for i in range(1<<N):
  candidate = "".join(["(" if (i & (1 << j)) == 0 else ")" for j in range(N-1, -1, -1) ])
  if check(candidate):
    print(candidate)
