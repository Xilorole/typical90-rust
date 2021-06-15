N , Q = list(map(int,input().split()))
d = []
for i in range(N):
  x,y = list(map(int,input().split()))
  d.append((x-y, x+y))

Xmin = min(_d[0] for _d in d)
Ymin = min(_d[1] for _d in d)
Xmax = max(_d[0] for _d in d)
Ymax = max(_d[1] for _d in d)

points = [
  (Xmin, max(y for x, y in d if x == Xmin)),
  (Xmin, min(y for x, y in d if x == Xmin)),
  (Xmax, max(y for x, y in d if x == Xmax)),
  (Xmax, min(y for x, y in d if x == Xmax)),
  (min(x for x, y in d if y == Ymin), Ymin),
  (max(x for x, y in d if y == Ymin), Ymin),
  (min(x for x, y in d if y == Ymax), Ymax),
  (max(x for x, y in d if y == Ymax), Ymax)]

for _ in range(Q):
  q = int(input()) - 1
  x, y = d[q]
  print(max([(abs(x+y-_x-_y)+abs(y-x-_y+_x))//2 for _x,_y in points]))
