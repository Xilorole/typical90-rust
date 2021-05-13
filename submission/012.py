from sys import stdin
input = stdin.readline

H, W = list(map(int,input().split()))
Q = int(input())

# https://qiita.com/ofutonfuton/items/c17dfd33fc542c222396
class UnionFind():
  def __init__(self, n: int):
    self.par = [i for i in range(n)]
  
  def root(self, x: int) -> int:
    if self.par[x] == x: return x
    self.par[x] = self.root(self.par[x])
    return self.par[x]
  
  def unite(self, x:int, y:int):
    rx = self.root(x)
    ry = self.root(y)
    if (rx != ry) : self.par[rx] = ry
  
  def same(self, x:int, y:int):
    return self.root(x) == self.root(y)

uf = UnionFind(H*W)
def f(r,c) : return (r-1)*W+(c-1)

is_red = { (h,w):False for h in range(H+2) for w in range(W+2)}

for q in range(Q):
  query = input()
  if query [0] == "1":
    tag, r, c = tuple(map(int,query.split()))
    # グループの結合
    is_red[(r,c)] = True
    if is_red[(r-1,c)]: uf.unite(f(r,c), f(r-1,c))
    if is_red[(r+1,c)]: uf.unite(f(r,c), f(r+1,c))
    if is_red[(r,c-1)]: uf.unite(f(r,c), f(r,c-1))
    if is_red[(r,c+1)]: uf.unite(f(r,c), f(r,c+1))
      
  else:
    tag, r, c, r_, c_ = tuple(map(int,query.split()))
    if uf.same(f(r,c),f(r_,c_)) and is_red[(r,c)]:
      print("Yes")
    else:
      print("No")
