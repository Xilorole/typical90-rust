import numpy as np 

N,B,K = list(map(int,input().split()))
c = list(map(int,input().split()))
m = int(1e9) + 7

mat = np.zeros((B,B), dtype = np.int)

for j in range(B):
  for k in range(K):
    mat[j, (10*j+c[k])%B] += 1

def product(A, B, mod=m):
  I,J = A.shape
  J,K = B.shape
  out = np.zeros((I,K), dtype=np.int)
  for i in range(I):
    for j in range(J):
      for k in range(K):
        out[i,k] = (out[i,k] + A[i,j]*B[j,k]) % mod
  return out
        
d = {0: mat}
for i in range(1, int(np.log2(N))+1):
  d[i] = product(d[(i-1)], d[(i-1)]) 

def mat_power(N):
  ans = np.eye(B, dtype=np.int)
  for i in range(int(np.log2(N))+1, -1, -1):
    if N >= 2**i:
      ans = product(ans , d[i]) 
      N -= 2**i

  return ans
print(mat_power(N)[0][0])