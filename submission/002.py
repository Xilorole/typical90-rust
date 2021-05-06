N = int(input())

def check(candidate):
  cnt = 0
  for char in candidate:
    if char == "1":
      cnt += 1
    else:
      cnt -= 1
    if cnt < 0:
      return False
  if cnt == 0:
    return True
  else:
    return False

for i in range(2 ** N-1,-1,-1):
  candidate = f"{i:020b}"[-N:]
  if check(candidate):
    print(candidate.replace("1","(").replace("0",")"))
