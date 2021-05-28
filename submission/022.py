a,b,c = list(map(int,input().split()))
import math
d = math.gcd(a,math.gcd(b,c))
print(a//d-1+c//d-1+b//d-1)
