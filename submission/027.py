N = int(input())

names = set()
for i in range(N):
  s = input()
  if s not in names:
    print(i+1)
  names |= {s}
