MAX = 510000
MOD = 1_000_000_007
 
fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX
 
def cominit():
  fac[0] = fac[1] = 1
  finv[0] = finv[1] = 1
  inv[1] = 1
  for i in range(2, MAX):
    fac[i] = fac[i-1] *i %MOD
    inv[i] = MOD - inv[MOD%i] * (MOD //i) %MOD
    finv[i] = finv[i-1] * inv[i] % MOD
 
def C(n, k):
  if n < k : return 0
  if n < 0 or k < 0: return 0
  return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD
 
from math import ceil

cominit()
N = int(input())
for k in range(1, N+1):
  s= 0
  for a in range(1, ceil(N/k)+1):
    s += C(N-(a-1)*(k-1), a)
    s %= MOD
  print(s)
