N = int(input())
P = [list(map(int,input().split())) for i in range(N)]

from collections import defaultdict
from math import atan2, degrees, pi

degs = defaultdict(list)
for i, (px, py) in enumerate(P):
  for j, (qx, qy) in enumerate(P):
    if i != j:
      deg = atan2(qy-py, qx-px)
      if deg < 0:
        deg += 2 * pi
      degs[i] += [degrees(deg)]
        
import bisect
ans = 0
for i in range(N):
  sorted_degs = sorted(degs[i])
  for deg in degs[i]:
    j = bisect.bisect_right(sorted_degs, (180 + deg) % 360) % (N-1)
    ddeg1 = abs(deg - sorted_degs[j])
    ddeg1 = min(ddeg1, 360-ddeg1)
    
    ddeg2 = abs(deg - sorted_degs[j-1])
    ddeg2 = min(ddeg2, 360-ddeg2)
    
    ans = max(ddeg1, ddeg2, ans)

print(ans)
