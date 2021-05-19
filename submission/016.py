N = int(input())
A, B, C = list(map(int,input().split()))
 
maisu = 9999
for a_cnt in range(10000):
  for b_cnt in range(10000 - a_cnt):
    S = (N - A*a_cnt - B*b_cnt)
    if S < 0:
      break
    if S % C == 0:
      maisu = min(maisu, a_cnt + b_cnt + S//C)
print(maisu)
