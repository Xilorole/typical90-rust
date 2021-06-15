from math import gcd
a,b = tuple(map(int,input().split()))
g = gcd(a, b)

if a*b//g > 1_000_000_000_000_000_000:
  print("Large")
else:
  print(a*b//g)
